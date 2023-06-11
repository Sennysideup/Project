### 보아즈 20기 분석 미니프로젝트1
- 뉴스 기사 분류 모델 구축 프로젝트
- 목표 : baseline 모델 성능 개선
- 프로세스
  1. 모델 크기 변경
  2. tokenizer에 vocab 추가
  3. 하이퍼 파라미터 튜닝
  4. augmentation & undersampling
  5. 학습 데이터와 다른 데이터에 적용

#### result
1. 모델 크기 : large < small < base
2. vocab 추가 : 추가 이후 < 추가 이전
3. 하이퍼 파라미터 튜닝 : 튜닝 이전 < 튜닝 이후
4. augmentation & undersampling : 적용 이전 < 적용 이후

#### contribution
- vocab 추가
  1. Okt 형태소 분석 결과를 vocab에 추가
  2. 빅카인즈 특성 추출 결과를 vocab에 추가
