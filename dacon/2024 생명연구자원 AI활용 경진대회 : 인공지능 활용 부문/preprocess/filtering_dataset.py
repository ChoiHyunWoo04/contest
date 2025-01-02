import pandas as pd

train = pd.read_csv('DATASET_withSetting01.csv')

# 행의 모든 값이 0이면 필터링
train = train.loc[~(train.iloc[:, 2:] == 0).all(axis=1)]

# 행의 돌연변이 개수가 1000을 넘으면 드랍
id = train['ID']
subclass = train['SUBCLASS']
x_train = train.drop(columns=['ID', 'SUBCLASS'])

row_sums = x_train.sum(axis=1)
x_train = x_train[row_sums <= 1000]

x_train.insert(0, 'SUBCLASS', subclass)
x_train.insert(0, 'ID', id)

x_train.to_csv('train.csv', index=False)

# SUBCLASS 열의 각 도메인 비중 계산
total_rows = len(train)
domain_counts = train['SUBCLASS'].value_counts()
domain_ratios = (domain_counts / total_rows) * 100

print(f"{domain_ratios}%")
print(train.shape)