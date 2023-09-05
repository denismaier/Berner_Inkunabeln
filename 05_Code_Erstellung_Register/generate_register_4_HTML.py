#!/usr/bin/env python
# coding: utf-8

# In[1]:


from platform import python_version
import os
import ast
from collections import defaultdict

import pandas as pd
import jinja2
from jinja2 import Template
import regex as re


# In[2]:


print("Python version: " + python_version())
print("Pandas version: " + pd.__version__)
print("Jinja2 version: " + jinja2.__version__)
print("Regex version: " + re.__version__)


# In[ ]:


# Pfad zum Ordner, in dem sich die nachbearbeiteten Inkunabeldatensätze befinden
data_path = r"..."


# In[ ]:


# Pfad zum Ordner, in dem das mit diesem Script erstellte html-Dokument abgelegt werden soll
output_path = r"..."


# In[ ]:


people_all_data = []
reference_all_data = []

for item in os.listdir(data_path):
    with open(data_path + item, "r", encoding='utf8') as file:
        lines = file.read()

        reg_4_recognition_start = "<-REGISTER-4-START->\n"
        reg_4_recognition_stop = "<-REGISTER-4-STOP->\n"
        reg_4_content_start = lines.find(reg_4_recognition_start)
        reg_4_content_stop = lines.find(reg_4_recognition_stop)
        reg_4_content_range = lines[reg_4_content_start + len(reg_4_recognition_start) : reg_4_content_stop]
        reg_4_content = re.findall("<-P-START->(.*?)<-P-STOP->", reg_4_content_range)

        reference_recognition_start = "<-REGISTER-REF-START->\n"
        reference_recognition_stop = "<-REGISTER-REF-STOP->\n"
        reference_content_start = lines.find(reference_recognition_start)
        reference_content_stop = lines.find(reference_recognition_stop)
        reference_content_range = lines[reference_content_start + len(reference_recognition_start) : reference_content_stop]
        reference_doi = re.findall("<-DOI-START->(.*?)<-DOI-STOP->", reference_content_range)[0]
        reference_number = re.findall("<-Nr-START->(.*?)<-Nr-STOP->", reference_content_range)[0]
        reference_signature = re.findall("<-SIGN-START->(.*?)<-SIGN-STOP->", reference_content_range)[0]
    
    people_all_data.append(reg_4_content)
    
    references = [reference_doi, reference_number, reference_signature]
    #html_ref_raw = item[:-4] + ".html"
    #html_ref = html_ref_raw.replace("(","").replace(")","").replace("<<","").replace(">>","").replace(" ","_").replace("&","").replace("'", "")
    #references = [html_ref, reference_number, reference_signature]
    
    reference_all_data.append(references)


# In[ ]:


filedict = defaultdict(list)


# In[ ]:


for index, author in enumerate(people_all_data):
    for item in author:
        if reference_all_data[index] not in filedict[item]:
            filedict[item].append(reference_all_data[index])


# In[ ]:


sorted_dict = sorted(filedict.items())


# In[ ]:


filedict_sorted = dict(sorted_dict)


# ---

# In[ ]:


path_excelfile = "Vorgaben_Registersortierung/"


# In[ ]:


excelfile = "Register_4_Wunschsortierung.xlsx" 


# In[ ]:


df_sortierliste = pd.read_excel(path_excelfile + excelfile, header=None, names=["owners"])


# In[ ]:


index_sorted = df_sortierliste["owners"].to_list()
len(index_sorted)


# In[ ]:


index_unsorted = list(filedict_sorted.keys())
len(index_unsorted)


# In[ ]:


l_drin = []
l_nichtdrin = []

for item in index_unsorted:
    if item in index_sorted:
        l_drin.append(item)
    else:
        l_nichtdrin.append(item)


# In[ ]:


len(l_drin)


# In[ ]:


len(l_nichtdrin)


# In[ ]:


owner_dict_custom_sorted = {k: filedict_sorted[k] for k in index_sorted if k in filedict_sorted}


# In[ ]:


template = '''
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Register 4</title>
        <link rel="stylesheet" type="text/css" href="_galley.css" media="screen">
    </head>
    <body>
        <div class="index">
            <h1 class="title">Vorbesitzer</h1> 
            {% for key, value in owner_reference_dict.items() %}
            <div class="index-entry">
                <div class="index-entry-term">{{key}}</div>
                <div class="nav-pointer-group">
                    <span class="nav-pointer">
                        <span class="ext-ref">
                            {% for element in value %}
                            <a href ="{{element[0]}}" target="_blank">{{element[1]}}</a>{{ "," if not loop.last }}
                            {% endfor%}
                        </span>
                    </span>
                </div>
             </div> 
             {% endfor%}
        </div>
    </body>
</html>'''


# In[ ]:


data = {
    "owner_reference_dict" : owner_dict_custom_sorted
}


# In[ ]:


t = Template(template, trim_blocks=True, lstrip_blocks=True)
bits = t.render(data)


# In[ ]:


with open(output_path + "Register_4_sortiert.html", 'w', encoding='utf8') as file:
    file.write(bits)


# ---
