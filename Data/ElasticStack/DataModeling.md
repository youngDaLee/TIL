# Data Modeling
**Mapping** : ES에서 인덱싱 시, 문서의 데이터 유형에 따른 적절한 타입을 지정하는 것. 사전에 매핑을 하지 않으면 ES가 타입 자동지정. 문제 발생시키지 않기 위해 매핑 과정 매우 중요함

## Mapping API
동적 매핑
- 사용자가 매핑 타입을 지정하지 않고, ES가 자동지정.
- 첫번째로 인서트되는 데이터에 따라 타입을 정의함
- 한 번 생성된 매핑 타입은 변경할 수 없다. 타입 변경을 원하면 인덱스 삭제 후 다시 생성하거나 매핑 다시 정의해야 한다.

### 매핑 생성 시 고려사항
- 문자열을 분석할 것인가?
- _source에 어떤 필드를 정의할 것인가?
- 날짜 필트를 가지는 필드는 무엇인가?
- 매핑에 정의되지 않고 유입되는 필드는 어떻게 처리할 것인가?

### 인덱스 생성
```
PUT movie_search
{
    "settings": {
        "number_of_shards": 5,
        "number_of_replicas": 1,
    },
    "mappings": {
        "_doc": {
            "properties": {
                "movieCd": {
                    "type": "keyword"
                },
                "movieNm": {
                    "type": "text",
                    "analyzer: "standard",
                },
                "prdtYear": {
                    "type": "integer"
                },
                "companies": {
                    "progerties": {
                        "companyCd": {
                            "type": "keyword"
                        },
                        "companyNm": {
                            "type": "keyword"
                        }
                    }
                }
            }
        }
    }
}
```

### 매핑 확인
```
GET movie_search/_mapping
```

### 매핑 파라미터
#### analyzer
- 해당 필드 데이터를 형태소 분석하겠다.
- text 데이터타입 필드는 analyzer 매핑 파라미터를 기본적으로 사용해야함.

#### nomalizer
- term query에 분석기를 사용하기 위해 사용
- cafe, Cafe, Cafe` 가 모두 같은 문서로 인식되기 위해 사용

#### boost
- 필드에 가중치(Weigth) 부영
- 가중치에 따라 유사도 점수(_score)가 달라짐
- 인덱싱 시점에 boost 설정하면 다시 indexing 하지 않는 이상 가중치 변경 안됨 -> 검색 시점에만 사용!!
- 7.0버전부터 boost 설정 기능 제거됨

#### coerce
- 인덱싱 시 자동 변환 허용 여부 설정
- "10"과 같은 형태 문자열이 integer 필드에 들어올 때 자동으로 형변환.
  - coerce 미설정 시 인덱싱 실패

#### copy_to
- 매핑 파라미터를 추가한 필드를 지정한 필드로 복사.

#### fileddata
- ES가 힙 공간에 생성하는 매모리 캐시
- 거의 사용하지 않지만, text타입 필드가 정렬되어야 할 때..
- 메모리 소모가 크기 때문에 기본적으로 비활성화 되어있음

#### doc_values
- ES에서 사용하는 기본 캐시
- 루씬 기바 캐시 방식
- 필드를 정렬, 집계할 필요 없고 스크립트에서 필드값에 액세스 할 필요 없으면 디스크 공간 절약 위해 doc_values 비활서오하

#### dynamic
- 매핑 필드를 동적으로 생성할지, 생성하지 않을지 결정
  - true : 새로 추가되는 필드를 매핑에 추가
  - false : 새로 추가되는 필드 무시. -> 새로 추가되는 필드 검색 불가(인덱싱 안됨), _source에는 표시됨
  - strict : 새로운 필드 추가되면 예외 발생, 문서 자체가 색인되지 않음. 새로 유입되는 필드는 사용자가 매핑에 명시적으로 추가해야 함

#### enabled
- 검색 결과에는 포함하지만 색인은 하지 않음

#### format
- 날짜/시간을 문자열로 표시 포맷

#### ignore_above
- 필드에 저장되는 문자열이 일정 크기 넘어가면 빈값으로 색인

#### ignore_malformed
- 잘못된 데이터 타입 인덱싱 시, 해당 필드만 무시하고 도큐먼트는 인덱싱 가능

#### index
- 필드값을 인덱싱할지 결정
- 기본값 true

#### fields
- 다중 필드 설정 옵션
- 필드 안에 다른 필드 추가 가능

```
PUT my_idx
{
    "mappings": {
        "_doc": {
            "properties": {
                "name": {
                    "type": "text",
                    "fields": {
                        "alias": {
                            "type": "keyword"
                        }
                    }
                }
            }
        }
    }
}
```

#### norms
- _score값 계산에 필요한 정규화 인수 사용 여부.
- 기본값 true. 비활성화해서 디스크 공간 절약 가능

#### null_value
- 문서값 null이어도 필드 생성하고 저장함

#### position_increment_gap
- 배열 형태의 데이터 색인 시 검색 정확도 높이기 위해 사용
- `["John Abraham", "Lincon Smith"]` 검색 시 `"Abraham Lincon"` 으로 검색해도 검색 가능

#### properties
- Object타입 or 중첩(Nested)타입 스키마 정의 시 사용

#### search_analyzer
- 검색 시 사용할 분석기를 별도로 지정

#### simiarity
- 유사도 측정 알고리즘 지정
  - BM25 : ES 디폴트 유사도 측정 알고리즘
  - classic : TF/IDF 알고리즘. 용어 개수로 유사도 계산
  - boolean  : 복잡한 수학적 모델 없이 단순 boolean 연산으로 유사도 측정

#### store
- 필드를 자체적으로 저장 가능

#### term_vector
- 루씬에서 분석된 용어 정보를 포함할지 여부를 견정
  - no : term vector 저장 x
  - yes : 필드, 용어만 저장
  - with_positions : 용어, 용어 시작 끝 위치 저장
  - with_offsets : 용어, 문자 오프셋 저장
  - with_position_offsets : 용어, 용어 시작과 끝, 문자 오프셋 모두 저장


## 메타 필드
실제 문서의 정보를 담고있는 _source 필드, 그 밖의 _index, _type, _id, _score의 메타필드

### _index
문서 인덱스 명.
- 인덱스 명과 인덱스에 몇 개 도큐먼트 있는지 확인 가능

### _type
해당 도큐먼트가 속한 매핑 타입 정보

### _id
- 도큐먼트 식별 키

### _uid
- `#` 태그를 사용해 _type과 _id값 조합해 사용 -> 내부적으로만사용. 검색 시 조회되는 값은 아님

### _source
- 문서 원본 데이터

### _all
- 색인에 사용된 모든 필드 정보 가진 메타 필드
- 모든 필드 내용이 하나의 텍스트로 합쳐져 제공됨

### _routing
- 특정 문서를 샤드에 저장하기 위해 지정


## 필드 데이터 타입
- keyword, text와 같은 문자열 타입
- date, long, double, integer, boolean, ip 같은 데이터 타입
- 각체, 중첩문 등 JSON 계층 특성의 데이터 타입
- geo_point, geo_shape 같은 특수한 데이터 타입

### Keyword 
별도의 분석기를 거치지 않고 원문 그대로 색인.

사용되는 항목
- 검색 시 필터링 되는 항목
- 정렬이 필요한 항목
- 집계(aggregation)해야 하는 항목

ex) 'elastic search' 검색 시
- 'elastic search'로만 검색 가능
- 'elastic' : 검색 불가

Kyword 타입에서 설정가능한 주요 파라미터
- boost : 검색 결과 정렬에 영향
- doc_values : 필드를 메모리에 로드해 캐시로 사용. 기본값 true
- index : 해당 필드를 검색에 사용할지. 기본값 true
- null_value : 데이터 값이 없는 겨우 null로 필드 값 대체할지 설정(기본적으로 값 없으면 필드 자체를 생성하지 않음)
- store : 필드값을 필드와 별도로 _source에 저장하고 검색 가능하게 할지 설정. 기본값 false

### Text
데이터를 문자열 데이터로 인식. 분석기는 기본적으로 Standard Analyzer를 사용.

text타입을 검색 & 정렬(sorting) & 집계(aggregation)에 사용해야 할 때 -> 멀티필드로 설정   
```
PUT movie_search/_mapping/_doc
{
    "properties": {
        "movieComment": {
            "type": "text",
            "fields": {
                "movieComment_keyword": {
                    "type": "keyword"
                }
            }
        }
    }
}
```

text 타입에서 설정 가능한 주요 파라미터
- analyzer : 인덱스와 검색에 사용할 형태소 분석기 설정
- boost
- fielddata
- index
- norms
- store
- search_analyzer
- simialrity
- term_vector

### Array
배열 첫번째 값이 데이터 타입 결정. 배열의 모든 값이 같은 타입으로 구성되어야 함

### Numeric
- long : 64비트 정수
- integer : 32비트 정수
- short : 16비트 정수
- byte : 8비트 정수
- double : 64비트 부동 소수점
- float : 32비트 부동소수점
- half_float : 16비트 부동 소수점

### Date
별도 형식 지정하지 않을 시 `"yyyy-MM-ddTHH:mm:ssZ"` 형태로 지정됨.

아래 세 가지 형태 제공, UTC 밀리초 단위
- 문자열 포함된 날짜 형식
- ISO_INSTANT 포함된 날짜 형식
- 밀리초

### Range
범위가 있는 데이터
- integer_range
- float_range
- long_range
- double_range
- date_range
- ip_range

### Boolean

### Geo-Point
- 위경도 위치

### IP
IPv4, IPv6 모두 지정 가능

### Object
내부 객체 계층적 표현 가능. 특정 키워드로 데이터 정의하지 않고 필드값으로 문서 구조 입력
```
{
    "properties": {
        "compaies": {
            "properties": {
                "companyName": {
                    "type": "text"
                }
            }
        }
    }
}
```

### Neseted
Object 객체 배열을 독립적으로 질의/색인하는 데이터 타입.

필드 내 검색은 기본적으로 OR조건으로 검색됨.    
- OR 조건 검색은 조금만 복잡해져도 검색 모호해짐.
- Array 타입 내부 검색은 모든 데이터를 기준으로 OR연산하기 때문에 Array 내부 도큐먼트 필드값 증가할수록 혼란 가중  
```
{
    "title": "해리포터,
    "copanies": [
        {  
            "companyCd": 1,
            "companyName": "워너"
        },
        {
            "companyCd": 2,
            "companyName": "heyday"
        }
    ]
}
```
=> 이런 문제 해결 위해 Nested 정의!!
```
PUT movie/_mapping/_doc
{
    "properties: {
        "compaies": {
            "type": "nested"
        }
    }
}

PUT movie/_doc/8
{
    "title": "해리포터",
    "companies: [
        {  
            "companyCd": 1,
            "companyName": "워너"
        },
        {
            "companyCd": 2,
            "companyName": "heyday"
        }
    ]
}

POST movie/_search
{
    "query": {
        "nested": {
            "path": "companies",
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {"companies.companyName": "워너"}
                        },
                        {
                            "match": {"companies.companyCd": "2"}
                        }
                    ]
                }
            }
        }
    }
}
```

## ES 분석기
