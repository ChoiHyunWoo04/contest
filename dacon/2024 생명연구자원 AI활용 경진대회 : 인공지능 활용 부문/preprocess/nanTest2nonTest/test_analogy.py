import pandas as pd

test = pd.read_csv("./test.csv")

#test = test.fillna(0.5)

id = test['ID']
x_test = test.drop(columns=['ID'])

def setting(x):
    if pd.isna(x):
        return x
    elif x == 'WT':
        return 0
    else:
        return 1

def fill_nan_with_row_mean(df):
    # 각 행의 평균을 계산 (NaN을 제외하고 계산)
    row_means = df.mean(axis=1)
    
    # NaN 값을 해당 행의 평균으로 채우기
    df_filled = df.apply(lambda row: row.fillna(row.mean()), axis=1)
    
    return df_filled

# NaN 값을 행의 평균으로 채워 넣기
x_test = x_test.applymap(setting)
x_test = fill_nan_with_row_mean(x_test)

non_binary_count = ((x_test != 0.0) & (x_test != 1.0)).sum().sum()

print(f"0 또는 1이 아닌 셀의 개수: {non_binary_count}")

x_test.insert(0, 'ID', id)

#print(x_test)
#x_test.to_csv('test_with_nan_mean_setting.csv', index=False)

non_binary_count = ((x_test != 0.0) & (x_test != 1.0)).sum().sum()

print(f"0 또는 1이 아닌 셀의 개수: {non_binary_count}")

'''count_nan = test.isna().sum().sum()
#count_0_5 = (test == 0.5).sum().sum()

print(f"값이 nan인 셀의 개수: {count_nan}")'''