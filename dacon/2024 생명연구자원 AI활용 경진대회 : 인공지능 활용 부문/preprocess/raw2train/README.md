## cbioportal
+ 이 포털에서 각 기관에서 공개한 암환자의 유전자변이 데이터를 가져올 수 있었음. 원하는 암종에 대한 암환자들의 유전자 데이터를 가져오거나, 암종이 섞인 대용량 데이터셋을 가져올 수 있었음.
+ 각 기관마다 cancer code가 달랐기에 TCGA의 cancer code로 통합할 필요가 있었음. (dacon에서 제공한 훈련 데이터셋의 라벨링이 TCGA code로 되어있었기 때문)
+ 다운받은 파일이 txt 파일이었기에 csv 파일로 변환하는 과정이 필요했고, 각 기관마다 제공하는 속성(열)이 달라서 열을 divide, drop, merge하는 등의 과정이 필요했음.
+ 특정 기관들은 각 암종 코드에 세부적인 암종들이 들어있었고, 특정 암종들은 TCGA에서 다루지 않는 암종들이었기에 따로 분류해내는 과정이 필요했음.
+ TCGA, MSK, ORIGIMED, CPTAC, OHSU ... 등등 다양한 기관에서 데이터를 가져옴. MSK 데이터셋의 일부 데이터들은 전처리가 특별히 더 필요했고 따로 SPECIAL이라는 데이터셋에 모아둠. CPTAC, OHSU 등 데이터가 많지 않은 기관들의 데이터들은 OTHERS라는 데이터셋에 concat하여 모아둠.

## 파일 설명
+ raw2csv: 포탈에서 받아온 데이터들은 모두 txt 파일이므로 csv파일로 변형할 필요가 있었음. 각 파일마다 전처리 할 부분이 보이면 약간의 변형(행 분할)을 해주었음.
+ merge_: 각 기관들의 csv 데이터들을 하나의 데이터셋으로 모아둠. cancer code가 다른 기관들은 TCGA의 코드에 맞게 변형을 가하였음. 훈련 데이터셋의 암종 분포가 너무 치우쳐지는 것을 막기 위해 일부 데이터(행)들은 drop함.
+ mixed_: 모든 암종이 섞여있는 데이터셋에서 분류하고자하는 26종을 따로 분류해냄.
+ concat: 각 기관들의 데이터셋을 하나로 통합. 코드 아래엔 특정 기관에서 제공한 데이터의 세부적인 암종 정보를 얻기 위한(기관에서 따로 제공하는 clinical_data.txt 파일이 있음) 과정이 있음.
+ 모든 데이터셋을 통합하는 것이 꼭 좋은 결과를 가져오진 않았음. (아마도, 전체 훈련 데이터셋에 특정 암종의 데이터가 너무 많아져서 불균형이 일어났기 때문으로 해석됨.)
