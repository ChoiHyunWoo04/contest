import pandas as pd

replace_dict = {
    'Bladder Urothelial Carcinoma': 'BLCA',
    'Urothelial Carcinoma Other': 'BLCA',
    'Small Cell Bladder Cancer': 'BLCA',
    'Bladder Squamous Cell Carcinoma': 'BLCA',
    'Bladder Adenocarcinoma': 'BLCA',
    'Plasmacytoid/Signet Ring Cell Bladder Carcinoma': 'BLCA',
    'Sarcomatoid Carcinoma of the Urinary Bladder': 'BLCA',
    'Urethral Urothelial Carcinoma': 'BLCA',
    'Urachal Adenocarcinoma': 'BLCA',

    'Breast Invasive Carcinoma': 'BRCA',
    'Breast Carcinoma Other': 'BRCA',
    'Breast Microinvasive Carcinoma': 'BRCA',

    'Colorectal Adenocarcinoma': 'COAD',
    'Colorectal Carcinoma Other': 'COAD',

    'Cervical Squamous Cell Carcinoma': 'CESC',
    'Endocervical Adenocarcinoma': 'CESC',
    'Cervical Adenosquamous Carcinoma': 'CESC',
    'Small Cell Carcinoma of the Cervix': 'CESC',

    'Hepatocellular Carcinoma': 'LIHC',
    'Liver Hepatocellular Carcinoma': 'LIHC',
    'Hepatocellular Carcinoma plus Intrahepatic Cholangiocarcinoma': 'LIHC',

    'Lung Adenocarcinoma': 'LUAD',
    'Lung Adenosquamous Carcinoma': 'LUAD',

    'Lung Squamous Cell Carcinoma': 'LUSC',

    'High-Grade Serous Ovarian Cancer': 'OV',
    'Low-Grade Serous Ovarian Cancer': 'OV',
    'Ovarian Serous Carcinoma': 'OV',
    'Mucinous Ovarian Cancer': 'OV',
    'Clear Cell Ovarian Cancer': 'OV',
    'Ovarian Adenocarcinoma': 'OV',

    'Pancreatic Adenocarcinoma': 'PAAD',
    'Adenosquamous Carcinoma of the Pancreas': 'PAAD',
    'Solid Pseudopapillary Neoplasm of the Pancreas': 'PAAD',

    'Myxoid Fibrosarcoma': 'SARC',
    'Leiomyosarcoma': 'SARC',
    'Synovial Sarcoma': 'SARC',
    'Mucinous Liposarcoma': 'SARC',
    'Alveolar Soft Part Sarcoma': 'SARC',
    'Ewing Sarcoma': 'SARC',
    'Pleomorphic Rhabdomyosarcoma': 'SARC',
    'Unclassified Sarcoma': 'SARC',
    'Osteosarcoma': 'SARC',
    'Rhabdomyosarcoma': 'SARC',
    'Dedifferentiated Liposarcoma': 'SARC',
    'Malignant Peripheral Nerve Sheath Tumor': 'SARC',
    'Angiosarcoma': 'SARC',
    'Well Differentiated Liposarcoma': 'SARC',
    'Epithelioid Sarcoma': 'SARC',
    'Undifferentiated Sarcoma': 'SARC',
    'Pleomorphic Liposarcoma': 'SARC',
    'Malignant Small Cell Tumor': 'SARC',
    'Extraskeletal Myxoid Chondrosarcoma': 'SARC',

    'Gastric Adenocarcinoma': 'STES',
    'Esophageal Adenocarcinoma': 'STES',
    'Esophageal Squamous Cell Carcinoma': 'STES',
    'Esophageal Adenosquamous Carcinoma': 'STES',

    'Papillary Thyroid Carcinoma': 'THCA',
    'Medullary Thyroid Carcinoma': 'THCA',
    'Follicular Thyroid Carcinoma': 'THCA',

    'Uterine Endometrioid Carcinoma': 'UCEC',
    'Uterine Serous Carcinoma': 'UCEC',
    'Uterine Clear Cell Carcinoma': 'UCEC',

    'Adrenocortical Carcinoma': 'ACC',

    'Diffuse Large B-Cell Lymphoma': 'DLBC'
}

df = pd.read_csv('./mixed/origimed/label_mixed.csv')

leave_classes = replace_dict.values()

df['SUBCLASS'].replace(replace_dict, inplace=True)

df = df[df['SUBCLASS'].isin(leave_classes)]

# 데이터 불균형을 맞추기 위함
idx = df[df['SUBCLASS'] == 'SARC'].index
df.drop(idx, inplace=True)

idx = df[df['SUBCLASS'] == 'LUAD'].index
df.drop(idx, inplace=True)

idx = df[df['SUBCLASS'] == 'PAAD'].index
df.drop(idx, inplace=True)

idx = df[df['SUBCLASS'] == 'STES'].index
df.drop(idx, inplace=True)

# 결과를 확인하고 저장
print(df.shape)
df.to_csv('LARGE_ORIGIMED.csv', index=False)

'''unique_values = df['SUBCLASS'].value_counts()
print(unique_values)'''