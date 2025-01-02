import pandas as pd

tcga = pd.read_csv('LARGE_TCGA.csv')
#msk = pd.read_csv('LARGE_MSK.csv', dtype=str)
others = pd.read_csv('LARGE_OTHERS.csv')
#special = pd.read_csv('LARGE_SPECIAL.csv', dtype=str)
origimed = pd.read_csv('LARGE_ORIGIMED.csv')


df_list = [tcga, others, origimed]

concatenated_df = pd.concat(df_list, ignore_index=True)

print(concatenated_df.shape)
concatenated_df.to_csv('ML2024_DATASET_noMSK.csv', index=False)
'''
unique_values = concatenated_df['SUBCLASS'].value_counts()
print(unique_values)
print(unique_values.shape)

print(concatenated_df.isna().any(axis=1).sum())'''

'''
import pandas as pd

# 파일 읽기
mixed = pd.read_csv('./mixed/origimed/mixed.csv')
clinical = pd.read_csv('./mixed/origimed/pan_origimed_2020_clinical_data.tsv', sep='\t')

clinical = clinical[['Sample ID', 'Cancer Type']]
# 'SAMPLE_ID'와 'Sample id'를 기준으로 inner join (기본 동작)
merged = merged = pd.merge(clinical, mixed, left_on='Sample ID', right_on='ID', how='inner')
merged = merged.drop(columns=['Sample ID', 'STUDY_ID'])
merged = merged.rename(columns={'Project Code': 'SUBCLASS'})
merged.insert(0, 'ID', merged.pop('ID'))
# 결과 출력 및 저장
print(merged)
merged.to_csv('./mixed/origimed/labeled_mixed.csv', index=False)
'''
'''
df = pd.read_csv('./skcm/msk/skcm.csv')
# ID 열을 ':'을 기준으로 나누어 SUBCLASS와 새로운 ID 열 생성
df[['SUBCLASS', 'ID']] = df['ID'].str.split(':', expand=True)
df = df[['ID', 'SUBCLASS'] + [col for col in df.columns if col not in ['SUBCLASS', 'ID']]]
df = df.loc[df.Altered == 1]

print(df)
'''
'''thca = pd.read_csv('./stes/tcga/stes1.csv')
thpa = pd.read_csv('./stes/tcga/stad/stad.csv')
# 두 데이터프레임을 병합 (행을 기준으로 이어붙임)
df_combined = pd.concat([thca, thpa])

# CSV 파일로 저장
df_combined.to_csv('./stes/tcga/stes.csv', index=False)

print(thca.shape)'''