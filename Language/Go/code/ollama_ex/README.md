# ollama 실습
ollama
- 로컬 머신에서 LLM을 실행할 수 있게 해주는 플랫폼
- 다양한 오픈소스 LLM을 다운받아 실행 가능

ollama 서버를 띄운 뒤, localhost로 질문을 보내면 응답을 받음

![image](./sendandres.png)

- 재밌었던 점 : 한 번에 하나의 응답에만 답변을 함 -> 동시에 여러 메세지를 보내면 먼저 보낸 메세지에 대한 응답이 종료된 뒤 다음 메세지 응답을 받는 식(queue에 저장하는듯)

## 코드분석
### fs
파일 구조
```
.
├── config.go       // config 관련 인터페이스. 파일시스템 관련 설정값 관리
├── ggml            // ggml 파일 관련 포매팅 담당
│   ├── ggml.go     // ggml 포맷 파일 핸들링
│   ├── ggml_test.go
│   ├── gguf.go     // gguf 포맷 파일 핸들링
│   └── type.go     // ggml, gguf 관련 공동 타입 정의
└── util
    └── bufioutil   // 버퍼 기반 읽기 최적화 유틸리티
        ├── buffer_seeker.go    // 파일을 메모리에 올려넣고 탐색 가능하도록 지원
        └── buffer_seeker_test.go
```

ggml
- llm 모델 저장 형식
- 텐서 라이브러리. 크기가 큰 모델과 하드웨어 환경에서 성능을 발휘함
- 하나의 파일로 모델을 쉽게 공유 가능하며, 다양한 cpu에서 ggml을 모델을 실행할 수 있음
- 다만 모델에 추가적인 정보를 포함시키기 어렵고, 새로운 기능 추가 시 기존 모델과 호환 문제가 발생한다는 단점이 있음

gguf
- llm 모델계의 도커
- ggml보다 발전된 형식. 기존 모델과의 호환성을 유지함. 다만 기존 모델을 gguf로 전환하는데는 시간이 필요함
- 딥러닝 모델을 효율적으로 저장, 배포하기 위한 파일 형식
- 기존의 모델 저장 방식들이 특정 프레임워크나 라이브러리에 종속되어 호환성이 떨어지는 문제를 해결하고자 만든 모델. CPU, GPU, TPU등 다양한 플랫폼에서 모델을 실행할 수 있도록 지원하고, 모델 가중치를 효과적으로 저장하고 로딩 가능하도록 설계됨
- [참고](https://drfirst.tistory.com/entry/llm-%EB%AA%A8%EB%8D%B8%EC%97%90%EC%84%9C-GGUF%EA%B0%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EC%A7%80-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90-feat-bllossom-%EB%AA%A8%EB%8D%B8%EC%9D%84-gguf%EB%A1%9C-%EB%B0%94%EA%BF%94%EB%B3%B4%EA%B8%B0)


buffer_sekker
- 각 파일에 형식에 대한 읽기 최적화 지원.
- ggml, gguf가 각 파일 형식에 대한 파싱을 담당하는거라면 얘는 최적화 담당
```go
type BufferedSeeker struct {
	rs io.ReadSeeker    // 원본 readSeeker
	br *bufio.Reader    // rs를 감싼 버퍼 리더
}

func NewBufferedSeeker(rs io.ReadSeeker, size int) *BufferedSeeker {
	return &BufferedSeeker{
		rs: rs,
		br: bufio.NewReaderSize(rs, size),
	}
}
```
- 직접 파일 핸들에서 한 바이트씩 읽는게 아니라 큰 버퍼로 파일 조각(size단위)을 읽어두고 거기서 빠르게 Read처리를 함
  - 왜 br에서 쪼개놓냐? -> IO호출을 최소화 하기 위해서! -> 버퍼에 size만큼 읽어두고 메모리에 올려둬서 빠르게 읽고 씀. IO(실제파일 접근. rs)접근을 최소화 하기 위한 구조임

```go
func (b *BufferedSeeker) Read(p []byte) (int, error) {
	return b.br.Read(p)
}
```
- 버퍼에서 읽기(파일을 읽부 읽어와서 메모리에 저장)
- rs에서 안 읽고 버퍼에서 읽는 이유
  - IO논 비용이 많이듬. rs에서 읽는다는건 매 바이트마다 디스크에 접근해 읽겠다는 의미
  - Buffer에 size(64kb)만큼 한 번에 많이 읽어와서 올려둔 뒤, 메모리에서 읽기 처리를 하여 대규모 파일 읽기 성능을 높힌것.

```go
func (b *BufferedSeeker) Seek(offset int64, whence int) (int64, error) {
	// whenece 가 io.SeekCurrent라는건 "현재 위치에서" 뭘 할지 결정하겠다는 뜻
    // 현재 위치에서 offset까지 이동하기 위해서
    // 미리 버퍼에서 데이터를 읽어두었기 때문에 rs가 실제 포인터보다 뒤쳐져 있을 수 있음
    // 따라서 버퍼에 남은 양 만큼 빼줘야 함
    if whence == io.SeekCurrent {
		offset -= int64(b.br.Buffered())
	}
    // 원본 파일에서 Seek 호출하여 정확한 위치로 이동
	n, err := b.rs.Seek(offset, whence)
	if err != nil {
		return 0, err
	}
    // 버퍼 초기화 -> 원본 파일 핸들이 움직였기 때문에 버퍼가 유효하지 않음.
    // Reset해서 새 위치로 이동해 버퍼를 다시 채움
    // 새로운 버퍼 객체를 매번 만들지 않아 GC를 줄여준다
	b.br.Reset(b.rs)
	return n, nil
}
```
- 버퍼 값이 조정되는 이유 : 실제로 파일 위치보다 버퍼에는 일부를 읽어와서 미리 데이터에 저장을 해 두는 방식임(앞으로 읽을 데이터를 미리 저장)
- 버퍼에서 읽으려고 하는 값을 `int64(b.br.Buffered())` 빼줘서 실제 위치를 찾은 뒤에 Seek를 호출함


fs 역할
- ollama에서 llm 모델을 다룰 때, 모델 파일을 읽는데 사용함
- 모델 파일을 실제로 메모리에 올려 추론하는 역할
- 모델 파일 포맷 파싱과 설정값 관리, 대용량 파일 최적화에 사용됨
- 호출 시점 : 모델 로딩 시점
```go
// llm/server.go

// LoadModel will load a model from disk. The model must be in the GGML format.
//
// It collects array values for arrays with a size less than or equal to
// maxArraySize. If maxArraySize is 0, the default value of 1024 is used. If
// the maxArraySize is negative, all arrays are collected.
func LoadModel(model string, maxArraySize int) (*ggml.GGML, error) {
	if _, err := os.Stat(model); err != nil {
		return nil, err
	}

	f, err := os.Open(model)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	ggml, _, err := ggml.Decode(f, maxArraySize)
	
```

이런 버퍼 읽기가 언제 쓰이냐?
- 대용량 파일을 다루는 시스템에서 표준 기법처럼 사용된다함... 동영상 스트리밍, db스냅샷 등에서...
- 디스크IO는 느리기 때문에 한바이트 한바이트 읽는건 비효율적. 한 번에 크게 읽고 메모리에서 처리하도록 한다.
- 쉽게 말하면 크게 읽고 메모리에서 처리하는 친구

### kvcache
