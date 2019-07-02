import csv
from cdm_lib.schemas import SubArraySchema, cdm_to_json, cdm_to_obj
from marshmallow import Schema, fields, post_load, pprint

pprint('AT2-182 using CDM shared library')


#function to read contents of csv file named 'SubArrayNodeConfig.csv'
with open('SubArrayNodeConfig.csv','rt') as f:
  data = csv.reader(f)
  for row in data:
    csvread = open(row[0],"r") #read in file with name of row[0]
    if csvread.mode == 'r':
      contents = csvread.read()
      print(contents)
      #for item in contents:
      #  print item.get("subarrayID", "No subarrayID found...")
      #  print item.get("dish", "No dish found...")

      #Config_data = {
      #  'subarrayID': 1,
      #  'dish': row[0]
      #}
      csvread.close  
    schema = SubArraySchema()
    #result = cdm_to_obj(schema, row[0])
    #pprint(result)
    