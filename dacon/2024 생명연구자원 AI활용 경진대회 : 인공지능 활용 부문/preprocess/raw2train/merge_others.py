import pandas as pd

cancer_list = ['blca', 'coad', 'laml', 'kirc', 'dlbc', 'lgg', 'lusc', 'thca', 'skcm', 'gbmlgg', 'stes', 'hnsc',
               'luad', 'lihc', 'paad', 'prad', 'ucec', 'brca']

replace_dict = {
    'aml_ohsu_2022': 'LAML',
    'kirc_bgi': 'KIRC',
    'dlbcl_duke_2017': 'DLBC',
    'lusc_cptac_gdc': 'LUSC',
    'lgg_ucsf_2014': 'LGG',
    
    'thyroid_gatci_2024': 'THCA',
    'dlbcl_dfci_2018': 'DLBC',
    'aml_target_2018_pub': 'LAML',
    'skcm_yale': 'SKCM',
    'skcm_broad': 'SKCM',
    'ccrcc_irc_2014': 'KIRC', # KIRC
    'dlbc_broad_2012': 'DLBC',
    'nhl_bcgsc_2013': 'DLBC',

    'coad_cptac_gdc': 'COAD',
    'coad_caseccc_2015': 'COAD',
    'blca_bgi': 'BLCA',
    'blca_dfarber_mskcc_2014': 'BLCA',
    'gbm_cptac_2021': 'GBMLGG', # GBMLGG
    'gbm_columbia_2019': 'GBMLGG', # GBMLGG
    'esca_broad': 'STES', # STES
    'stad_oncosg_2018': 'STES', # STES
    'egc_tmucih_2015': 'STES', # STES
    'stad_pfizer_uhongkong': 'STES', # STES
    'stad_utokyo': 'STES', # STES
    'stad_uhongkong': 'STES',
    'hnsc_broad': 'HNSC',
    'hnsc_jhu': 'HNSC',
    'lihc_amc_prv': 'LIHC',
    'lihc_riken': 'LIHC',
    'luad_broad': 'LUAD',
    'luad_oncosg_2020': 'LUAD',
    #'luad_tsp': 'LUAD', # NS 때문에 안됨
    'paad_icgc': 'PAAD',
    'paad_qcmg_uq_2016': 'PAAD',
    'prad_broad_2013': 'PRAD',
    'prad_cpcg_2017': 'PRAD',
    'prad_fhcrc': 'PRAD',
    'prad_eururol_2017': 'PRAD',
    'ucec_cptac_2020': 'UCEC',

    'brca_bccrc': 'BRCA',
    'brca_broad': 'BRCA',
    'brca_sanger': 'BRCA'
    
}

df_list = []

for cancer in cancer_list:
    df = pd.read_csv(f'./{cancer}/{cancer}.csv')

    df = df.rename(columns={'STUDY_ID': 'SUBCLASS'})

    df.insert(0, 'ID', df.pop('ID'))

    df_list.append(df)

# 리스트에 있는 모든 데이터프레임을 행 단위로 결합
concatenated_df = pd.concat(df_list, ignore_index=True)
concatenated_df['SUBCLASS'].replace(replace_dict, inplace=True)

leave_classes = replace_dict.values()
concatenated_df = concatenated_df[concatenated_df['SUBCLASS'].isin(leave_classes)]

# 결과를 확인하고 저장
print(concatenated_df)
concatenated_df.to_csv('OTHERS.csv', index=False)

unique_values = concatenated_df['SUBCLASS'].value_counts()
print(unique_values)