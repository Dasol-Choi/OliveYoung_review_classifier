# OliveYoung_review_classifier
올리브영 온라인몰에 있는 장문의 리뷰를 넣으면 핵심 문장만 추출한 후, 긍/부정을 분류해서 내보내는 모델 설계
## Dataset
* 올리브영에서 크롤링한 약 16,000 문장의 리뷰 (평점 1점 ~ 5점까지 골고루 추출)
* Labeling
  * 핵심 문장 분류 : 0 - 핵심이 아닌 문장, 1 - 핵심문장 (16,000 문장)
  * 긍/부정 분류 : 0 - 부정 문장, 1 - 긍정 문장 (6,000 문장)
## 사용한 모델
* KlUE-BERT : BERT 기반 한국어 추가 학습 모델 
* ![](https://github.com/codespaces)
## Model Process
<img src="https://github.com/Dasol-Choi/OliveYoung_review_classifier/blob/main/figures/model_process.png" width=100% height=100%/><br>
## Key Sentence Classifier
<img src="https://github.com/Dasol-Choi/OliveYoung_review_classifier/blob/main/figures/key_sentence_models.png" width=75% height=75%/><br>
<br>
## Sentiment Classifier
<img src="https://github.com/Dasol-Choi/OliveYoung_review_classifier/blob/main/figures/sentiment_models.png" width=70% height=70%/><br>
