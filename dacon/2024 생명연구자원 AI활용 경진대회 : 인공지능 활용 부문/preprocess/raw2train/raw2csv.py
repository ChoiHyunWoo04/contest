import pandas as pd
import glob

data = 'stes'
laboratory = 'tcga'

txt_files = glob.glob(f'./{data}/{laboratory}/stad/*.txt')

dataframes = []

i = 0
for file in txt_files:
    df = pd.read_csv(file, sep='\t')
    #if df.columns[1] == 'Altered':
        #df[['STUDY_ID', 'SAMPLE_ID']] = df['studyID:sampleId'].str.split(':', expand=True)
        #df = df.drop(columns={'Altered', 'studyID:sampleId'})
        #df = df[['STUDY_ID', 'SAMPLE_ID'] + [col for col in df.columns if col not in ['STUDY_ID', 'SAMPLE_ID']]]
    if i != 0:
        df = df.drop(columns={'STUDY_ID'})
    dataframes.append(df)
    i = 1

merged_data = dataframes[0]
if len(dataframes) > 1:
    for file in dataframes[1:]:
        merged_data = pd.merge(merged_data, file, on='SAMPLE_ID')

merged_data = merged_data.rename(columns={'SAMPLE_ID': 'ID'})
#print(merged_data)
merged_data.to_csv(f'./{data}/tcga/stad/stad.csv', index=False)