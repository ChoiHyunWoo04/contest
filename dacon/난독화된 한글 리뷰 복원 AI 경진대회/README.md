각 파일의 역할
=============
* dataset_analysis: 대회에서 제공한 train, test dataset을 분석
* fine-tuning_decoder/encoder/generating_reviews: 각 파일은 gemma-ko-7b 모델을 파인튜닝하여 난독화된 한글 리뷰 복원 모델, 한글 리뷰 난독화 모델, 한글 리뷰 생성 모델을 생성
* augmentation(shuffle): train dataset의 리뷰들의 문장 순서를 바꿔 데이터 증강을 실시(증강된 dataset으로 test dataset 추론 시 약 85%의 정확률을 달성)
* augmentation(generation-step1/2): step 1에서 한글 리뷰를 생성, step 2에서 생성된 한글 리뷰를 난독화하여 데이터 증강을 실시
* augmentation(generation): shuffle로 증강된 데이터셋에 generation된 데이터셋을 병합(증강된 dataset으로 test dataset 추론 시 약 90%의 정확률을 달성)
* test_finetuning_v2: test dataset 추론, gemma 모델에 적합한 prompt를 통해 정확률을 높임

### 팀원분들께서 (난독화 리뷰, 복원 리뷰) 쌍 데이터 생성을 통해 증강에 도움을 주심. 최종적으로 90.311%의 정확도를 보이며 14등으로 대회를 종료하였음.
