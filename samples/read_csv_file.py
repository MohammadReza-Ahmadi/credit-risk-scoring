# first way #
# result = pandas.read_csv('../resource/data.csv')
# print(result)

# second way ##
# import csv
# with open('../resource/data.csv', 'rt')as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row)

# drop columns with more than 80% null values
# data.dropna(thresh=data.shape[0] * 0.2, how='all', axis=1, inplace=True)
# data.dropna()


import pandas as pd

loan_data = pd.read_csv('../resource/data.csv')
print(loan_data)
# drop columns with more than 80% null values
loan_data.dropna(thresh=loan_data.shape[0] * 0.2, how='all', axis=1, inplace=True)
print(loan_data)
