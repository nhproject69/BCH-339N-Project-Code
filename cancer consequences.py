#Gets amino acid mutations from GDC cancer portal
import json
from pprint import pprint
from xlrd import open_workbook
mutation_aa = []
#Takes cancer data in json format
with open('mutations.2018-04-18.json') as json_data:
    d = json.load(json_data)
    for i in range(len(d)):
        dict_aa = d[i]
        #Selects only for nonsynonomous mutations
        mutation = dict_aa['consequence'][0]['transcript']['aa_change']
        if mutation != None:
            mutation_aa.append(mutation)


