## cbioportal
+ 이 포털에서 각 기관에서 공개한 암환자의 유전자변이 데이터를 가져올 수 있었음.
+ 각 기관마다 cancer code가 달랐기에 TCGA의 cancer code로 통합할 필요가 있었음. (dacon에서 제공한 훈련 데이터셋의 라벨링이 TCGA code로 되어있었기 때문)
+ 다운받은 파일이 txt 파일이었기에 csv 파일로 변환하는 과정이 필요했고, 각 기관마다 제공하는 속성(열)이 달라서 열을 divide, drop, merge하는 등의 과정이 필요했음.
+ 
