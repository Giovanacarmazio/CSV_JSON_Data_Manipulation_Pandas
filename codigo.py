#1
print(len(json_response["hits"]["hits"]))

#2
print(json_response["hits"]["hits"][0])
print(json_response["hits"]["hits"][-1])

#3
ufs = []
for paciente in json_response["hits"]["hits"]:
    ufs.append(paciente["_source"]["paciente_endereco_uf"])
    
#4
ceps = []
for paciente in json_response["hits"]["hits"]:
    ceps.append(paciente["_source"]["paciente_endereco_cep"])
    
