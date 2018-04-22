import json
from pprint import pprint
from xlrd import open_workbook
mutation_aa = []
with open('mutations.2018-04-18.json') as json_data:
    d = json.load(json_data)
    for i in range(len(d)):
        dict_aa = d[i]
        mutation = dict_aa['consequence'][0]['transcript']['aa_change']
        if mutation != None:
            mutation_aa.append(mutation)


#only amino acid changes
mutation_no_text = []
for i in mutation_aa:
    temp = ''
    for j in range(len(i)):
        if i[j].isdigit():
            temp += i[j]
    mutation_no_text.append(temp)



exac_mu = []
cancer_mu = []

book = open_workbook("exac2.xlsx")
sheet = book.sheet_by_index(2)
for row in range(1,189):
    exac_mu.append(sheet.cell(row,0))

for row in range(1,68):
    cancer_mu.append(sheet.cell(row,1))


same = []
for i in cancer_mu:
    if i in exac_mu:
        same.append(i)

pprint(same)
