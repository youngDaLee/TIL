# Scrapy를 사용하여 다음 뉴스 크롤링
## Spider Middleware
[공식문서](https://docs.scrapy.org/en/latest/topics/spider-middleware.html?highlight=middleware)
- Scrapy spider가 처리하는 매카니즘에 우리가 추가한 function을 응답할 때 추가 가능
- responce, request, items 처리과정에서 내가 만든 기능 추가 가능
- pipeline은 item이 export되는 중 혹은 그 전에 작업 처리 가능, spider middleware는 요청 직전 혹은 응답 후에 혹은 어떤 함수 실행 전에 중간에서 계속 내가 만든 기능을 추가 할 수 있음.
- 이미지 다운 해 줄 수 있는 미들웨어, 등등 여러 기능 미들웨어 존재함.

### fake-user-agent
[github](https://github.com/alecxe/scrapy-fake-useragent)
매번 User-Agent 넣지 말고 fake agent로 접속   
`pip install scrapy-fake-useragent`

## 내가 겪은 어려움
### `.extract_first()`
강의는 스크래피 1.6버전을 사용하고 나는 2.x버전을 사용한다. 2.x버전 부터는 `.extract_first()`대신 `.get()`을 사용한다.    
[공식문서](https://docs.scrapy.org/en/latest/topics/selectors.html)

