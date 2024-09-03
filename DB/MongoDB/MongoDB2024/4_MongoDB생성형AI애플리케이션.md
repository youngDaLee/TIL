# 서비스의 품질과 생산성 향상을 위한 MongoDB 생성형 AI 애플리케이션 아키텍처

## 생성형 AI 애플리케이션의 현재
시맨틱 텍스트 검색 `query = "imaginary characters form outer space at war"` 이렇게 자연어로 쿼리하는 것

## RAG 및 어려움
생성형 AI 쿼리
* 사용자가 llm에 쿼리하고 요청합는 형태.
* RAG에서는 사용자 쿼리에 대해 context를 추가로 제공하는 vector database에 전달. private한 추가적인 context를 Llm에 전달...
* 비정형 knowlge database가 무엇인가?
* 복잡한 데이터소스의 처리와 임베딩 모델 선택... 검색 파라미터 선택등을 고민

## MongoDB 생성형 AI 애플리케이션 스택 
* 파운데이션 모델
  * 여러 옵션들... 앤트로픽, OpenAI, GoogleAI... 
  * 어떤 LLM을 써야하는지. 적절한 비용대 성능비를 얻으려면 어떻게 해야하는지
* 임베딩 모델
  * 코히어, 오픈에이아ㅣ, 노믹 등등..
  * 어떤 임베딩 모델을 선택해야 하나요 등등...
* 모델 호스팅/서비스 플랫폼
* 데이터 전처리
* Vector Database
* LLM 오케스트레이션 프레임워크
* LLM 관측성 및 평가
