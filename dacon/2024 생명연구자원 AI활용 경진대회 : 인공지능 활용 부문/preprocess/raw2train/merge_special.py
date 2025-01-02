import pandas as pd

cancer_list = ['thym', 'blca', 'cesc', 'lgg', 'lihc', 'coad']

replace_dict = {
    'glioma_mskcc_2019': 'LGG',
    'paired_bladder_2022': 'BLCA', 
    'cervix_msk_2023': 'CESC', 
    'hcc_msk_2024': 'LIHC',
    'tet_nci_2014': 'THYM',
    'crc_eo_2020': 'COAD'
}

replace_dict = {
    'Bladder Urothelial Carcinoma': 'BLCA',

    'Cervical Squamous Cell Carcinoma': 'CESC',
    'Endocervical Adenocarcinoma': 'CESC',

    'Diffuse Astrocytoma': 'LGG',
    'Glioblastoma Multiforme': 'GBMLGG',
    'Oligodendroglioma': 'LGG',
    'Anaplastic Astrocytoma': 'LGG',
    'Gliosarcoma': 'GBMLGG',
    'Anaplastic Oligodendroglioma': 'LGG',
    'Pilocytic Astrocytoma': 'LGG',
    'Rosette-forming Glioneuronal Tumor of the Fourth Ventricle': 'LGG',
    'Oligoastrocytoma': 'LGG',
    'Ganglioglioma': 'LGG',
    'Pleomorphic Xanthoastrocytoma': 'LGG',

    'Hepatocellular Carcinoma': 'LIHC',

    'Thymoma': 'THYM',
    
    'Colon Adenocarcinoma': 'COAD'
}
'''large = pd.read_csv('NoMSK_LARGE_DATASET.csv')
df = pd.read_csv(f'./mixed/special/thym/thym.csv')
clinical = pd.read_csv(f'./mixed/special/thym/clinical_data.tsv', sep='\t')
clinical = clinical[['Sample ID', 'Diagnosis']]
clinical = clinical.rename(columns={'Sample ID': 'ID', 'Diagnosis': 'SUBCLASS'})
df = df[['ID', 'STUDY_ID'] + [col for col in df.columns if col not in ['STUDY_ID', 'ID']]]
merged_df = pd.merge(clinical, df, on='ID')
merged_df.drop(columns='STUDY_ID', inplace=True)
merged_df['SUBCLASS'].replace(replace_dict, inplace=True)

leave_classes = replace_dict.values()
merged_df = merged_df[merged_df['SUBCLASS'].isin(leave_classes)]
concatenated_df = pd.concat([merged_df, large], ignore_index=True)

concatenated_df.to_csv('NoMSK_LARGE_DATASET.csv', index=False)'''

df_list = []
for cancer in cancer_list:
    df = pd.read_csv(f'./mixed/special/{cancer}/{cancer}.csv')
    clinical = pd.read_csv(f'./mixed/special/{cancer}/clinical_data.tsv', sep='\t')

    if cancer != 'thym':
        df[['STUDY_ID', 'ID']] = df['ID'].str.split(':', expand=True)
        df = df.drop(columns='Altered')

        clinical = clinical[['Sample ID', 'Cancer Type Detailed']]
        clinical = clinical.rename(columns={'Sample ID': 'ID', 'Cancer Type Detailed': 'SUBCLASS'})

    else:
        clinical = clinical[['Sample ID', 'Diagnosis']]
        clinical = clinical.rename(columns={'Sample ID': 'ID', 'Diagnosis': 'SUBCLASS'})

    df = df[['ID', 'STUDY_ID'] + [col for col in df.columns if col not in ['STUDY_ID', 'ID']]]

    merged_df = pd.merge(clinical, df, on='ID')
    merged_df.drop(columns='STUDY_ID', inplace=True)
    df_list.append(merged_df)

concatenated_df = pd.concat(df_list, ignore_index=True)
concatenated_df['SUBCLASS'].replace(replace_dict, inplace=True)

leave_classes = replace_dict.values()
concatenated_df = concatenated_df[concatenated_df['SUBCLASS'].isin(leave_classes)]

print(concatenated_df)

unique_values = concatenated_df['SUBCLASS'].value_counts()
print(unique_values)

concatenated_df.to_csv('LARGE_SPECIAL.csv', index=False)