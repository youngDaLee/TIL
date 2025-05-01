# GGML
GGML이란?
- C와 C++로 제작된 ML 라이브러리(트랜스포머(Transformer) 추론에 중접을 둔 ML)
  - Trasnformer : 쉽게 말하면 추상화 -> 단어, 문장에서 중요한 정보를 추출하는 딥러닝 모델
- ggml의 장점
  - minimalism : 코어 라이브러리가 5개 미만의 파일로 구성되어 있음
  - easy compilation : 좋은 빌드 툴이 필요하지 않음. GPU 없이도 GCC나 Clang만으로 동작 가능
  - Lightweight : 컴파일된 바이너라 사이즈가 1MB미만임
  - Good

GGUF는?
- GPT 생성 통합 형식 이라는 뜻
- LLM의 사용, 배포를 간소화 하도록 설계된 파일 형식
- 추론 모델을 저장하고 소비자용 컴퓨터 하드웨어에서 잘 작동하도록 설계됨
- 

추론 모델을 어떻게 저장하는지?

어떤 방식으로 소비자용 컴퓨터 하드웨어에서 잘 작동하도록 하는지?

GGML과는 무슨 차이가 있는지?

ollama에서는 어떻게 사용되는지?

## 참고
- [IBM - GGUF와 GGML 비교](https://www.ibm.com/kr-ko/think/topics/gguf-versus-ggml)
- [huggingface - introduction to ggml](https://huggingface.co/blog/introduction-to-ggml)
