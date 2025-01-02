import pandas as pd

labeled_cbioportal_data = pd.read_csv('./mixed/tcga/labeled_mixed.csv')

# 여러 대체 작업을 한 번에 처리
replace_dict = {
    'KICH': 'KIPAN',
    'KIRP': 'KIPAN',
    'RECA': 'KIPAN',
    'MELA': 'SKCM',
    'GBM': 'GBMLGG',
    'BTCA': 'GBMLGG',
    'STAD': 'STES',
    'GACA': 'STES',
    'ESAD': 'STES',
    'LIRI': 'LIHC',
    'LICA': 'LIHC',
    'PBCA': 'PAAD',
    'PACA': 'PAAD',
    'EOPC': 'PRAD',
    'LINC': 'LUAD'
}
# 'READ': 'COAD'
# *'PAEN': 'PAAD'
labeled_cbioportal_data['SUBCLASS'] = labeled_cbioportal_data['SUBCLASS'].str[:-3]

labeled_cbioportal_data['SUBCLASS'].replace(replace_dict, inplace=True)

# 삭제해야 할 암종들
drop_classes = ['CLLE', 'CMDI', 'ORCA', 'BOCA', 'PAEN', 'READ']
labeled_cbioportal_data = labeled_cbioportal_data[~labeled_cbioportal_data['SUBCLASS'].isin(drop_classes)]

print(labeled_cbioportal_data)
labeled_cbioportal_data.to_csv('./mixed/tcga/filtered_mixed.csv', index=False)