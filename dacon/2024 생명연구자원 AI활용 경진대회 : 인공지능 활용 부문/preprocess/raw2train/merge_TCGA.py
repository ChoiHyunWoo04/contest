import pandas as pd

cancer_list = ['acc', 'blca', 'brca', 'cesc', 'coad', 'dlbc', 'gbmlgg', 'hnsc', 'kipan', 'kirc', 'laml', 'lgg', 'lihc','luad',
               'lusc', 'ov', 'paad', 'pcpg', 'prad', 'sarc', 'skcm', 'stes', 'tgct', 'thca', 'thym', 'ucec']

replace_dict = {
    'acc_tcga_gdc': 'ACC',
    'blca_tcga_gdc': 'BLCA',
    'brca_tcga_gdc': 'BRCA',
    'cesc_tcga_gdc': 'CESC',
    'coad_tcga_gdc': 'COAD',
    'dlbc_tcga_pan_can_atlas_2018': 'DLBC',
    'lgggbm_tcga_pub': 'GBMLGG',
    'hnsc_tcga_gdc': 'HNSC',
    'kich_tcga': 'KIPAN', # KIPAN
    'kirp_tcga': 'KIPAN', # KIPAN
    'kirc_tcga': 'KIRC',
    'laml_tcga': 'LAML',
    'lgg_tcga': 'LGG',
    'lihc_tcga': 'LIHC',
    'luad_tcga_gdc': 'LUAD',
    'lusc_tcga_gdc': 'LUSC',
    'ov_tcga_pan_can_atlas_2018': 'OV',
    'paad_tcga_gdc': 'PAAD',
    'pcpg_tcga_pub': 'PCPG',
    'prad_tcga_gdc': 'PRAD',
    'sarc_tcga': 'SARC',
    'skcm_tcga_pan_can_atlas_2018': 'SKCM',
    'stes_tcga_pub': 'STES', # STAD 필요
    'tgct_tcga_pan_can_atlas_2018': 'TGCT',
    'thca_tcga': 'THCA',
    'thym_tcga_gdc': 'THYM',
    'ucec_tcga': 'UCEC',
    'gbm_tcga_pub2013': 'GBMLGG', # GBMLGG
    
    'thpa_tcga_gdc': 'THCA',
    'nsgct_tcga_gdc': 'TGCT', # TGCT
    'dlbclnos_tcga_gdc': 'DLBC', # DLBC
    'hgsoc_tcga_gdc': 'OV', # OV
    'ccrcc_tcga_gdc': 'KIRC', # KIRC
    'chrcc_tcga_gdc': 'KIPAN', # KIPAN
    'prcc_tcga_gdc': 'KIPAN', # KIPAN

    'stad_tcga': 'STES'
}

mixed = pd.read_csv('./mixed/tcga/filtered_mixed.csv')
df_list = []

for cancer in cancer_list:
    file_path = cancer
    df = pd.read_csv(f'./{file_path}/tcga/{cancer}.csv')
    df = df.rename(columns={'STUDY_ID':'SUBCLASS', 'SAMPLE_ID':'ID'})
    df.insert(0, 'ID', df.pop('ID'))
    df_list.append(df)

df_list.append(mixed)

# 리스트에 있는 모든 데이터프레임을 행 단위로 결합
concatenated_df = pd.concat(df_list, ignore_index=True)
concatenated_df['SUBCLASS'].replace(replace_dict, inplace=True)
idx = concatenated_df[concatenated_df['SUBCLASS'] == 'MALY'].index
concatenated_df = concatenated_df.drop(idx)

leave_classes = replace_dict.values()
concatenated_df = concatenated_df[concatenated_df['SUBCLASS'].isin(leave_classes)]

# 결과를 확인하고 저장
print(concatenated_df)
concatenated_df.to_csv('LARGE_TCGA.csv', index=False)
