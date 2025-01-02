import pandas as pd
import numpy as np

train = pd.read_csv('DATASET.csv', dtype=str)

id = train['ID']
subclass = train['SUBCLASS']
x_train = train.drop(columns=['SUBCLASS', 'ID'])
x_train = x_train.applymap(lambda x: 0 if x == 'WT' or x == '0' else 1)

x_train.insert(0, 'SUBCLASS', subclass)
x_train.insert(0, 'ID', id)

x_train.to_csv('DATASET_withSetting01.csv', index=False)