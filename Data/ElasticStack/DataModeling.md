# Data Modeling
**Mapping** : ES���� �ε��� ��, ������ ������ ������ ���� ������ Ÿ���� �����ϴ� ��. ������ ������ ���� ������ ES�� Ÿ�� �ڵ�����. ���� �߻���Ű�� �ʱ� ���� ���� ���� �ſ� �߿���

## Mapping API
���� ����
- ����ڰ� ���� Ÿ���� �������� �ʰ�, ES�� �ڵ�����.
- ù��°�� �μ�Ʈ�Ǵ� �����Ϳ� ���� Ÿ���� ������
- �� �� ������ ���� Ÿ���� ������ �� ����. Ÿ�� ������ ���ϸ� �ε��� ���� �� �ٽ� �����ϰų� ���� �ٽ� �����ؾ� �Ѵ�.

### ���� ���� �� �������
- ���ڿ��� �м��� ���ΰ�?
- _source�� � �ʵ带 ������ ���ΰ�?
- ��¥ ��Ʈ�� ������ �ʵ�� �����ΰ�?
- ���ο� ���ǵ��� �ʰ� ���ԵǴ� �ʵ�� ��� ó���� ���ΰ�?

### �ε��� ����
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

### ���� Ȯ��
```
GET movie_search/_mapping
```

### ���� �Ķ����
#### analyzer
- �ش� �ʵ� �����͸� ���¼� �м��ϰڴ�.
- text ������Ÿ�� �ʵ�� analyzer ���� �Ķ���͸� �⺻������ ����ؾ���.

#### nomalizer
- term query�� �м��⸦ ����ϱ� ���� ���
- cafe, Cafe, Cafe` �� ��� ���� ������ �νĵǱ� ���� ���

#### boost
- �ʵ忡 ����ġ(Weigth) �ο�
- ����ġ�� ���� ���絵 ����(_score)�� �޶���
- �ε��� ������ boost �����ϸ� �ٽ� indexing ���� �ʴ� �̻� ����ġ ���� �ȵ� -> �˻� �������� ���!!
- 7.0�������� boost ���� ��� ���ŵ�

#### coerce
- �ε��� �� �ڵ� ��ȯ ��� ���� ����
- "10"�� ���� ���� ���ڿ��� integer �ʵ忡 ���� �� �ڵ����� ����ȯ.
  - coerce �̼��� �� �ε��� ����

#### copy_to
- ���� �Ķ���͸� �߰��� �ʵ带 ������ �ʵ�� ����.

#### fileddata
- ES�� �� ������ �����ϴ� �Ÿ� ĳ��
- ���� ������� ������, textŸ�� �ʵ尡 ���ĵǾ�� �� ��..
- �޸� �Ҹ� ũ�� ������ �⺻������ ��Ȱ��ȭ �Ǿ�����

#### doc_values
- ES���� ����ϴ� �⺻ ĳ��
- ��� ��� ĳ�� ���
- �ʵ带 ����, ������ �ʿ� ���� ��ũ��Ʈ���� �ʵ尪�� �׼��� �� �ʿ� ������ ��ũ ���� ���� ���� doc_values ��Ȱ������

#### dynamic
- ���� �ʵ带 �������� ��������, �������� ������ ����
  - true : ���� �߰��Ǵ� �ʵ带 ���ο� �߰�
  - false : ���� �߰��Ǵ� �ʵ� ����. -> ���� �߰��Ǵ� �ʵ� �˻� �Ұ�(�ε��� �ȵ�), _source���� ǥ�õ�
  - strict : ���ο� �ʵ� �߰��Ǹ� ���� �߻�, ���� ��ü�� ���ε��� ����. ���� ���ԵǴ� �ʵ�� ����ڰ� ���ο� ��������� �߰��ؾ� ��

#### enabled
- �˻� ������� ���������� ������ ���� ����

#### format
- ��¥/�ð��� ���ڿ��� ǥ�� ����

#### ignore_above
- �ʵ忡 ����Ǵ� ���ڿ��� ���� ũ�� �Ѿ�� ������ ����

#### ignore_malformed
- �߸��� ������ Ÿ�� �ε��� ��, �ش� �ʵ常 �����ϰ� ��ť��Ʈ�� �ε��� ����

#### index
- �ʵ尪�� �ε������� ����
- �⺻�� true

#### fields
- ���� �ʵ� ���� �ɼ�
- �ʵ� �ȿ� �ٸ� �ʵ� �߰� ����

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
- _score�� ��꿡 �ʿ��� ����ȭ �μ� ��� ����.
- �⺻�� true. ��Ȱ��ȭ�ؼ� ��ũ ���� ���� ����

#### null_value
- ������ null�̾ �ʵ� �����ϰ� ������

#### position_increment_gap
- �迭 ������ ������ ���� �� �˻� ��Ȯ�� ���̱� ���� ���
- `["John Abraham", "Lincon Smith"]` �˻� �� `"Abraham Lincon"` ���� �˻��ص� �˻� ����

#### properties
- ObjectŸ�� or ��ø(Nested)Ÿ�� ��Ű�� ���� �� ���

#### search_analyzer
- �˻� �� ����� �м��⸦ ������ ����

#### simiarity
- ���絵 ���� �˰��� ����
  - BM25 : ES ����Ʈ ���絵 ���� �˰���
  - classic : TF/IDF �˰���. ��� ������ ���絵 ���
  - boolean  : ������ ������ �� ���� �ܼ� boolean �������� ���絵 ����

#### store
- �ʵ带 ��ü������ ���� ����

#### term_vector
- ������� �м��� ��� ������ �������� ���θ� ����
  - no : term vector ���� x
  - yes : �ʵ�, �� ����
  - with_positions : ���, ��� ���� �� ��ġ ����
  - with_offsets : ���, ���� ������ ����
  - with_position_offsets : ���, ��� ���۰� ��, ���� ������ ��� ����


## ��Ÿ �ʵ�
���� ������ ������ ����ִ� _source �ʵ�, �� ���� _index, _type, _id, _score�� ��Ÿ�ʵ�

### _index
���� �ε��� ��.
- �ε��� ��� �ε����� �� �� ��ť��Ʈ �ִ��� Ȯ�� ����

### _type
�ش� ��ť��Ʈ�� ���� ���� Ÿ�� ����

### _id
- ��ť��Ʈ �ĺ� Ű

### _uid
- `#` �±׸� ����� _type�� _id�� ������ ��� -> ���������θ����. �˻� �� ��ȸ�Ǵ� ���� �ƴ�

### _source
- ���� ���� ������

### _all
- ���ο� ���� ��� �ʵ� ���� ���� ��Ÿ �ʵ�
- ��� �ʵ� ������ �ϳ��� �ؽ�Ʈ�� ������ ������

### _routing
- Ư�� ������ ���忡 �����ϱ� ���� ����


## �ʵ� ������ Ÿ��
- keyword, text�� ���� ���ڿ� Ÿ��
- date, long, double, integer, boolean, ip ���� ������ Ÿ��
- ��ü, ��ø�� �� JSON ���� Ư���� ������ Ÿ��
- geo_point, geo_shape ���� Ư���� ������ Ÿ��

### Keyword 
������ �м��⸦ ��ġ�� �ʰ� ���� �״�� ����.

���Ǵ� �׸�
- �˻� �� ���͸� �Ǵ� �׸�
- ������ �ʿ��� �׸�
- ����(aggregation)�ؾ� �ϴ� �׸�

ex) 'elastic search' �˻� ��
- 'elastic search'�θ� �˻� ����
- 'elastic' : �˻� �Ұ�

Kyword Ÿ�Կ��� ���������� �ֿ� �Ķ����
- boost : �˻� ��� ���Ŀ� ����
- doc_values : �ʵ带 �޸𸮿� �ε��� ĳ�÷� ���. �⺻�� true
- index : �ش� �ʵ带 �˻��� �������. �⺻�� true
- null_value : ������ ���� ���� �ܿ� null�� �ʵ� �� ��ü���� ����(�⺻������ �� ������ �ʵ� ��ü�� �������� ����)
- store : �ʵ尪�� �ʵ�� ������ _source�� �����ϰ� �˻� �����ϰ� ���� ����. �⺻�� false

### Text
�����͸� ���ڿ� �����ͷ� �ν�. �м���� �⺻������ Standard Analyzer�� ���.

textŸ���� �˻� & ����(sorting) & ����(aggregation)�� ����ؾ� �� �� -> ��Ƽ�ʵ�� ����   
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

text Ÿ�Կ��� ���� ������ �ֿ� �Ķ����
- analyzer : �ε����� �˻��� ����� ���¼� �м��� ����
- boost
- fielddata
- index
- norms
- store
- search_analyzer
- simialrity
- term_vector

### Array
�迭 ù��° ���� ������ Ÿ�� ����. �迭�� ��� ���� ���� Ÿ������ �����Ǿ�� ��

### Numeric
- long : 64��Ʈ ����
- integer : 32��Ʈ ����
- short : 16��Ʈ ����
- byte : 8��Ʈ ����
- double : 64��Ʈ �ε� �Ҽ���
- float : 32��Ʈ �ε��Ҽ���
- half_float : 16��Ʈ �ε� �Ҽ���

### Date
���� ���� �������� ���� �� `"yyyy-MM-ddTHH:mm:ssZ"` ���·� ������.

�Ʒ� �� ���� ���� ����, UTC �и��� ����
- ���ڿ� ���Ե� ��¥ ����
- ISO_INSTANT ���Ե� ��¥ ����
- �и���

### Range
������ �ִ� ������
- integer_range
- float_range
- long_range
- double_range
- date_range
- ip_range

### Boolean

### Geo-Point
- ���浵 ��ġ

### IP
IPv4, IPv6 ��� ���� ����

### Object
���� ��ü ������ ǥ�� ����. Ư�� Ű����� ������ �������� �ʰ� �ʵ尪���� ���� ���� �Է�
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
Object ��ü �迭�� ���������� ����/�����ϴ� ������ Ÿ��.

�ʵ� �� �˻��� �⺻������ OR�������� �˻���.    
- OR ���� �˻��� ���ݸ� ���������� �˻� ��ȣ����.
- Array Ÿ�� ���� �˻��� ��� �����͸� �������� OR�����ϱ� ������ Array ���� ��ť��Ʈ �ʵ尪 �����Ҽ��� ȥ�� ����  
```
{
    "title": "�ظ�����,
    "copanies": [
        {  
            "companyCd": 1,
            "companyName": "����"
        },
        {
            "companyCd": 2,
            "companyName": "heyday"
        }
    ]
}
```
=> �̷� ���� �ذ� ���� Nested ����!!
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
    "title": "�ظ�����",
    "companies: [
        {  
            "companyCd": 1,
            "companyName": "����"
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
                            "match": {"companies.companyName": "����"}
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

## ES �м���
