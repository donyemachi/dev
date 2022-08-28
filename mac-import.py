import yaml
from rich import print
from jinja2 import Environment, FileSystemLoader
import yaml
from jinja2 import Template


from jinja2 import Environment, FileSystemLoader
import pandas as pd
from macaddress import EUI48, EUI64, MAC, OUI
import macaddress
import copy
from datetime import datetime
import numpy as np
from jinja2 import Template
from jinja2 import Template, StrictUndefined
import yaml


df1 = pd.read_excel('mac-list.xlsx')
df2 = copy.deepcopy(df1)

def mmac(mm):
    return macaddress.MAC(str(mm))



df2['user_mac'] = df2.apply(lambda row: mmac(row['EthernetMacAddress']), axis = 1)

df3 = df2[["AddressName","user_mac"]] 


df4 = df3.replace(r'^\s*$', 'unknown-user', regex=True)
dict2 = df4.to_dict(orient="list")

ss = list(dict2.values())[0]
sss = list(dict2.values())[1]

c = {str(new_key1):str(new_value1) for (new_key1,new_value1) in zip(ss,sss)}


cas = {'users':c}

data2 = yaml.dump(cas)

#read your jinja template file
with open("template.j2") as file:
    template = Template(file.read())
    
   
with open("vari.yaml", mode="w", encoding="utf-8") as results:
    results.write(data2)
    
with open("vari.yaml") as file1:
    vari = yaml.safe_load(file1)

#use jinja to render your configuration
aa = template.render(vari)

with open("wired-mac.xml", mode="w", encoding="utf-8") as results:
    results.write(aa)

#print(aa)
#print(variables)
