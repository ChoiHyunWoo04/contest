import pandas as pd

cancer_list = ['blca', 'brca', 'cesc', 'coad', 'dlbc', 'lgg', 'hnsc', 'kipan', 'lihc','luad',
               'ov', 'paad', 'prad', 'sarc', 'skcm', 'stes', 'tgct', 'thca', 'ucec']

replace_dict = {
    #'paired_bladder_2022': 'BLCA', # 골라내기 필요
    'breast_msk_2018': 'BRCA', #
    #'cervix_msk_2023': 'CESC', # 골라내기 필요
    #'crc_eo_2020': 'COAD', # 골라내기 필요
    'mbn_msk_2024': 'DLBC',
    #'glioma_mskcc_2019': 'LGG', # 골라내기 필요
    'hnc_mskcc_2016': 'HNSC',
    'urcc_mskcc_2016': 'KIPAN',
    #'hcc_msk_2024': 'LIHC', # 골라내기 필요
    'luad_mskcc_2020': 'LUAD',
    'pdac_msk_2024': 'PAAD',
    'prad_cdk12_mskcc_2020': 'PRAD',
    'sarcoma_mskcc_2022': 'SARC',
    'mel_mskimpact_2020': 'SKCM',
    'egc_mskcc_2020': 'STES',
    'gct_msk_2016': 'TGCT',
    'thyroid_mskcc_2016': 'THCA',
    'ucec_ancestry_cds_msk_2023': 'UCEC',
    'lgsoc_mapk_msk_2022': 'OV',
    'hgsoc_msk_2021': 'OV'
}

df_list = []
for cancer in cancer_list:
    df = pd.read_csv(f'./{cancer}/msk/{cancer}.csv')
    df[['SUBCLASS', 'ID']] = df['ID'].str.split(':', expand=True)
    df = df.drop(columns='Altered')
    df = df[['ID', 'SUBCLASS'] + [col for col in df.columns if col not in ['SUBCLASS', 'ID']]]
    id = df['ID']
    subclass = df['SUBCLASS']

    df_list.append(df)

# 리스트에 있는 모든 데이터프레임을 행 단위로 결합
concatenated_df = pd.concat(df_list, ignore_index=True)
concatenated_df['SUBCLASS'].replace(replace_dict, inplace=True)
idx1 = concatenated_df[concatenated_df['SUBCLASS'] == 'msk_spectrum_tme_2022'].index
concatenated_df = concatenated_df.drop(idx1)

leave_classes = replace_dict.values()
concatenated_df = concatenated_df[concatenated_df['SUBCLASS'].isin(leave_classes)]

'''row1 = concatenated_df[concatenated_df['SUBCLASS'] == 'PAAD']
rows_to_drop1 = row1.sample(n=1100).index
concatenated_df = concatenated_df.drop(rows_to_drop1)'''

# 결과를 확인하고 저장
print(concatenated_df)
concatenated_df.to_csv('LARGE_MSK.csv', index=False)

unique_values = concatenated_df['SUBCLASS'].value_counts()
print(unique_values)
print(unique_values.shape)