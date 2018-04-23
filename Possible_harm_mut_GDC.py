#Gets possibly harmful mutations from GDC cancer portal
#This is for CLPTM1L, same thing was done for CLPTM1
import json
mutation_aa = []
#Takes cancer data in json format
with open('CLPTM1L_Cancer.json') as json_data:
    d = json.load(json_data)

    for i in range(len(d['mutations'])):
        mutation = d['mutations'][i]['aa_change']
        mutation_aa.append(mutation)
