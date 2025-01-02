import pandas as pd
import re

train = pd.read_csv('DATASET.csv')
id = train['ID']
subclass = train['SUBCLASS']
train = train.drop(columns=['ID', 'SUBCLASS'])

def identify_mutation(mutation):
    if isinstance(mutation, float) and pd.isna(mutation):
        return -1  # NaN 값 처리
    
    mutation = mutation.split(' ')[0]
    # Regular expressions for each mutation type
    missense_pattern = r'^[A-Z]\d+[A-Z]$'  # Example: N252I
    missense_pattern2 = r'^\*\d+\*$'  # Example: *252*
    missense_pattern3 = r'^[A-Z]\d+$' # M391
    missense_pattern4 = r'^[A-Z]\d+=$'
    nonsense_pattern = r'^[A-Z]\d+\*$'  # Example: R97*
    nonsense_pattern2 = r'^\*\d+[A-Z]$'  # Example: *97R
    frameshift_pattern = r'.*fs$'  # Example: I383Sfs
    frameshift_pattern2 = r'.*fs.*$' # F313Lfs*21
    insertion_pattern = r'.*ins.*$'
    deletion_pattern = r'^.*del$'  # Example: F508del
    deletion_pattern2 = r'^.*del.*$'
    duplication_pattern = r'^.*dup$'  # Example: T26dup
    complex_pattern = r'.*>.*$'
    complex_pattern2 = r'.*delins.*'
    splice_pattern = r'.*splice$'
    
    if mutation == 'WT':
        return 0
    if re.match(nonsense_pattern, mutation) or re.match(nonsense_pattern2, mutation):
        return 1
    elif re.match(missense_pattern, mutation) or re.match(missense_pattern2, mutation) or re.match(missense_pattern3, mutation) or re.match(missense_pattern4, mutation):
        return 2
    elif re.match(frameshift_pattern, mutation) or re.match(frameshift_pattern2, mutation):
        return 3
    elif re.match(complex_pattern, mutation) or re.match(complex_pattern2, mutation):
        return 4
    elif re.match(insertion_pattern, mutation):
        return 5
    elif re.match(deletion_pattern, mutation) or re.match(deletion_pattern2, mutation):
        return 6
    elif re.match(duplication_pattern, mutation):
        return 7
    elif re.match(splice_pattern, mutation):
        return 8
    else:
        print(mutation, end=' ')
        return 9

# Example test cases
train = train[(train != 0).all(axis=1)]
train = train.applymap(lambda x: identify_mutation(x))
count_9 = train.applymap(lambda x: x == 9).sum().sum()

train.insert(0, 'SUBCLASS', subclass)
train.insert(0, 'ID', id)

print(count_9)
train.to_csv('ML2024_DATASET_encoding.csv', index=False)