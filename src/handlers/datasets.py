import json
import csv

def start(dataset,function):
    file = open(f"resources/{dataset}.csv",'r',encoding="utf-8")
    archivo_json = open(f"resources/{dataset}.json",'w')

    contenido_archivo = csv.reader(file,delimiter=',')
    llaves = next(contenido_archivo)
    informacion = list(contenido_archivo)
    informacion = list(filter(function,informacion))

    nueva_informacion = []
    for elemento in informacion:
         dict = {}
         for i in range(len(llaves)):
            dict[llaves[i]] = elemento[i]  #agrego un diccionario al cual le añado el valor de su respectiva llave
         nueva_informacion.append(dict)
    
    json.dump(nueva_informacion,archivo_json,indent=4)

    file.close()
    archivo_json.close()