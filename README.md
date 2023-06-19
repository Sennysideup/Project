### 보아즈 20기 분석 미니프로젝트2
- 올리브영 리뷰 요약 데이터를 활용한 추천시스템 성능 개선
- 목표 : 추천시스템 성능을 개선할 수 있는 리뷰 데이터 feature 생성 및 적용
---------------------------------------------------------
#### contribution
- crawling
- text summarization
  1. KoBART
  2. lexrank
- text embedding
  1. TF-IDF
  2. word2vec
  3. KoBART
---------------------------------------------------------
### Crawling
#### Process
1. 상품 상세 페이지로 이동할 수 있는 goodsno 수집
2. 상품 상세 페이지 : 상품 정보 + <b>리뷰 작성자 id 수집</b>
3. 리뷰 작성자 페이지 : 최근에 작성한 20개 리뷰 및 상품명, 평점, 사용자 정보 수집
#### Issue
- 반복적으로 스크래핑 시 웹페이지 접속 불가
  1. fake-useragent : 효과X
  2. Tor : 효과X
  3. free-proxy : 가장 효과있던 방법
     1. https = yes
     2. elite, anonymous 여부 무관
