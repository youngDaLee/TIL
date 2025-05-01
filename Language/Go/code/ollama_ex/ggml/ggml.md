# GGML
## GGML이란?
- C와 C++로 제작된 ML 라이브러리(트랜스포머(Transformer) 추론에 중접을 둔 ML)
  - Trasnformer : 쉽게 말하면 요약 -> 단어, 문장에서 중요한 정보를 추출하는 딥러닝 모델
- ggml의 장점
  - minimalism : 코어 라이브러리가 5개 미만의 파일로 구성되어 있음
  - easy compilation : 좋은 빌드 툴이 필요하지 않음. GPU 없이도 GCC나 Clang만으로 동작 가능
  - Lightweight : 컴파일된 바이너라 사이즈가 1MB미만임
  - Good compatibility(좋은 호환성) : x86_62, ARM, CUDA, Apple Silicon 등등의 다양한 하드웨어가 지원됨
  - Support for quantized tensors : 텐서가 메모리 절약을 위해 양자화 될 수 있음
    - Tensor : 배열
    - Quantized(양자화) : 쉽게 말하면 아날로그화
  - Exteremely memory efficient : 텐서를 저장하고 계산을 수행하는데 드는 오버헤드가 적음
- ggml 단점
  - 모든 텐서 연산이 백엔드에서 지원되는건 아님(일부는 CPU에서는 작동해도 CUDA에서는 작동X)
  - ggml이용한 개발은 쉽지 않을 수 있음(저수준 프로그래밍 지식 필요할수도..)

### ggml 시작하기
```shell
# Start by installing build dependencies
# "gdb" is optional, but is recommended
sudo apt install build-essential cmake git gdb

# Then, clone the repository
git clone https://github.com/ggerganov/ggml.git
cd ggml

# Try compiling one of the examples
cmake -B build
cmake --build build --config Release --target simple-ctx

# Run the example
./build/bin/simple-ctx

# example output
mul mat (4 x 3) (transposed result):
[ 60.00 55.00 50.00 110.00
 90.00 54.00 54.00 126.00
 42.00 29.00 28.00 64.00 ]
```

### 용어, 개념
- ggml_context: 텐서, 그래프, (optional)데이터 객체를 저장하는 컨테이너
- ggml_cgraph: computational graph(계산 그래프). 백엔드로 전달될 계산 순서
- ggml_backend: computation graphs를 실행하기 위한 인터페이스. 백엔드 타입 : CPU (default), CUDA, Metal (Apple Silicon), Vulkan, RPC, etc.
- ggml_backend_buffer_type: buffer type. 각각의 ggml_backend 에 연결된"memory allocator".
  - ex) GPU에서 계산을 수행하기 위해서는, GPU에 buffer_type(buft)을 통해 메모리를 할당해야 함
- ggml_backend_buffer: buffer_type별로 할당된 버퍼. 버퍼는 여러 텐서를 저장할 수 있다.
- ggml_gallocr: computation graph에서 사용되는 텐서를 효율적으로 할당하는데 사용되는 그래프 메모리 할당기
- ggml_backend_sched: 여러 백엔드를 동시에 사용할 수 있는 스케줄러. 대형 모델이나 여러 GPU를 다룰 때 다양한 하드웨어(CPU, GPU등)에 연산을 분산시킬 수 있음. 스케줄러는 GPU가 지원하지 않는 작업은 CPU에 할당하는 등 최적의 리소스 활용과 호환성을 보장함

### 예시
두 개의 매트릭으로 합성곱을 만드는 예시

파이토치에서는 아래와 같이 합성곱을 만든다면
```py
import torch

# Create two matrices
matrix1 = torch.tensor([
  [2, 8],
  [5, 1],
  [4, 2],
  [8, 6],
])
matrix2 = torch.tensor([
  [10, 5],
  [9, 9],
  [5, 4],
])

# Perform matrix multiplication
result = torch.matmul(matrix1, matrix2.T)
print(result.T)
```
ggml에서는 아래와 같이 만들어줌
1. 텐서를 저장하기 위해 ggml_context할당
2. 텐서 생성 및 데이터 설정
3. mul_mat 연산을 위한 ggml_c 그래프 생성
4. 계산 실행
5. 결과 도출
6. 메모리 해제 및 종료

```c
#include "ggml.h"
#include "ggml-cpu.h"
#include <string.h>
#include <stdio.h>

int main(void) {
    // initialize data of matrices to perform matrix multiplication
    const int rows_A = 4, cols_A = 2;
    float matrix_A[rows_A * cols_A] = {
        2, 8,
        5, 1,
        4, 2,
        8, 6
    };
    const int rows_B = 3, cols_B = 2;
    float matrix_B[rows_B * cols_B] = {
        10, 5,
        9, 9,
        5, 4
    };

    // 1. Allocate `ggml_context` to store tensor data
    // Calculate the size needed to allocate
    size_t ctx_size = 0;
    ctx_size += rows_A * cols_A * ggml_type_size(GGML_TYPE_F32); // tensor a
    ctx_size += rows_B * cols_B * ggml_type_size(GGML_TYPE_F32); // tensor b
    ctx_size += rows_A * rows_B * ggml_type_size(GGML_TYPE_F32); // result
    ctx_size += 3 * ggml_tensor_overhead(); // metadata for 3 tensors
    ctx_size += ggml_graph_overhead(); // compute graph
    ctx_size += 1024; // some overhead (exact calculation omitted for simplicity)

    // Allocate `ggml_context` to store tensor data
    struct ggml_init_params params = {
        /*.mem_size   =*/ ctx_size,
        /*.mem_buffer =*/ NULL,
        /*.no_alloc   =*/ false,
    };
    struct ggml_context * ctx = ggml_init(params);

    // 2. Create tensors and set data
    struct ggml_tensor * tensor_a = ggml_new_tensor_2d(ctx, GGML_TYPE_F32, cols_A, rows_A);
    struct ggml_tensor * tensor_b = ggml_new_tensor_2d(ctx, GGML_TYPE_F32, cols_B, rows_B);
    memcpy(tensor_a->data, matrix_A, ggml_nbytes(tensor_a));
    memcpy(tensor_b->data, matrix_B, ggml_nbytes(tensor_b));


    // 3. Create a `ggml_cgraph` for mul_mat operation
    struct ggml_cgraph * gf = ggml_new_graph(ctx);

    // result = a*b^T
    // Pay attention: ggml_mul_mat(A, B) ==> B will be transposed internally
    // the result is transposed
    struct ggml_tensor * result = ggml_mul_mat(ctx, tensor_a, tensor_b);

    // Mark the "result" tensor to be computed
    ggml_build_forward_expand(gf, result);

    // 4. Run the computation
    int n_threads = 1; // Optional: number of threads to perform some operations with multi-threading
    ggml_graph_compute_with_ctx(ctx, gf, n_threads);

    // 5. Retrieve results (output tensors)
    float * result_data = (float *) result->data;
    printf("mul mat (%d x %d) (transposed result):\n[", (int) result->ne[0], (int) result->ne[1]);
    for (int j = 0; j < result->ne[1] /* rows */; j++) {
        if (j > 0) {
            printf("\n");
        }

        for (int i = 0; i < result->ne[0] /* cols */; i++) {
            printf(" %.2f", result_data[j * result->ne[0] + i]);
        }
    }
    printf(" ]\n");

    // 6. Free memory and exit
    ggml_free(ctx);
    return 0;
}
```

### 그러면 ggml은 pytorch나 tensorflow같은 라이브러리인가?
아님. ggml은 실제로 딥러닝 모델을 추론하기 위한 라이브러리가 아니라, 이미 학습된 모델을 로컬에서 추론하기 위한 라이브러리임. 학습이 완료된 모델에 대해서 해당 모델에 입력을 했을 때 결과를 얻는 라이브러리.
모델을 학습시켜서 추론하는 pytorch, tensorflow랑은 다름.


## GGUF는?
- GPT 생성 통합 형식 이라는 뜻
- LLM의 사용, 배포를 간소화 하도록 설계된 파일 형식
- 추론 모델을 저장하고 소비자용 컴퓨터 하드웨어에서 잘 작동하도록 설계됨
- 효율적인 실행을 위해 **모델 매개변수(weight, bias)**를 추가 메타데이터랑 결합하여 달성
- 이미 학습된 모델의 빠른 로딩과 저장을 위해 설계된 바이너리 형식
- **파일 형식이지 추론을 하지는 않음** -> 추론은 그대로 ggml에서 담당. ggml에서 읽는 모델 파일 형식을 발전시킨 버전이 gguf. 기존 ggml과 결합해서 사용함

### GGML과는 무슨 차이가 있는지?
- GGML은 인공지능 모델을 로드할 수 있도록 인공지능 모델을 파일화 한 초창기의 시도
- 초창기 라이브러리인 만큼 유연성, 확장성 측면에서 제한적임(모델을 추가 학습시키는게 불가능)
- GGUF는 GGML의 제한 사항을 해결하고 이전 모델과의 호환성을 유지하며 새로운 기능을 추가할 수 있도록 개선함.
- GGML에서 정의한 포맷을 개선한 포맷으로 이해하면 될듯...


## 참고
- [IBM - GGUF와 GGML 비교](https://www.ibm.com/kr-ko/think/topics/gguf-versus-ggml)
- [huggingface - introduction to ggml](https://huggingface.co/blog/introduction-to-ggml)
