import json
import requests
from pprint import pprint
from bs4 import BeautifulSoup
#Gets filtering allele frequency for CLPTM1L gene. Same thing was done for CLPTM1
url = 'http://exac.hms.harvard.edu/rest/gene/variants_in_gene/ENSG00000049656'
response = requests.get(url)
response.raise_for_status()
data = json.loads(response.text)
freq = {}
filtering_af = {}

for i in range(len(data)):
    temp = data[i]["pop_acs"]
    hgvsp = data[i]['HGVSp']
    for ethnicity in (temp):
        if ethnicity in freq:
            freq[ethnicity] += temp[ethnicity]
        else:
            freq[ethnicity] = temp[ethnicity]
    variant = data[i]["variant_id"]
    url_variant = 'http://exac.broadinstitute.org/variant/' + variant
    response_variant = requests.get(url_variant)
    response_variant.raise_for_status()
    c = response_variant.content
    soup2 = BeautifulSoup(c, 'html.parser')
    link = soup2.select('a[href="http://cardiodb.org/allelefrequencyapp/"]')
    filtering_af[variant] = (link[0].text.lstrip().strip('\n'))

pprint(filtering_af)