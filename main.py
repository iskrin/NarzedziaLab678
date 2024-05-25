import argparse
import json
import yaml
import xmltodict as xml

def pharseArguments():
    parser = argparse.ArgumentParser(description="Converter between .xml, .yaml, .json") 
    parser.add_argument('sourceFile', type=str, help='Source file that we want to convert') #Plik wejsciowy
    parser.add_argument('targetFile', type=str, help='Target file with a desired extension') #Plik docelowy
    args = parser.parse_args()  
    return args

def readJson(filePath): #Czyta jsona i zwaraca obiekt z zawartoscia
    try:
        with open(filePath, 'r') as jsonFile:
            data = json.load(jsonFile)
        return data
    except:
        print("Error while reading source file (json)")

def writeJson(filePath, dataObject):    #Zapisuje obiekt jako plik json
    with open(filePath, "w") as jsonFile:
            json.dump(dataObject, jsonFile)

def readYaml(filePath): #Czyta yamla i zwaraca obiekt z zawartoscia
    try:
        with open(filePath, 'r') as yamlFile:
            data = yaml.safe_load(yamlFile)
        return data
    except:
        print("Error while reading source file (yaml)")

def writeYaml(filePath, dataObject):    #Zapisuje obiekt jako plik yaml
    with open(filePath, "w") as yamlFile:
            yaml.dump(dataObject, yamlFile)

def readXml(filePath): #Czyta xmla i zwaraca obiekt z zawartoscia
    try:
        with open(filePath, 'r') as xmlFile:
            xmlContent = xmlFile.read()
            data = xml.parse(xmlContent)
            return data
    except:
        print("Error while reading source file (yaml)")



args = pharseArguments()    #argumenty

sourceFile = args.sourceFile    #nazwa pliku wejsciowego wraz z rozszerzeniem
sourceFormat = sourceFile.split(".")[-1]   #rozszerze pliku wejsciowego

targetFile = args.targetFile    #nazwa pliku docelowego wraz z rozszerzeniem
targetFormat = targetFile.split(".")[-1]    #rozszerze pliku docelowego

if(sourceFormat == "json"):
    dataObject = readJson(sourceFile) 

    if(targetFormat == "json"):
      writeJson(targetFile, dataObject)
    elif(targetFormat == "yaml"):
      writeYaml(targetFile, dataObject)

elif(sourceFormat == "yaml"):
    dataObject = readYaml(sourceFile) 
    
    if(targetFormat == "json"):
      writeJson(targetFile, dataObject)
    elif(targetFormat == "yaml"):
      writeYaml(targetFile, dataObject)

elif(sourceFormat == "xml"):
    dataObject = readXml(sourceFile) 
    
    if(targetFormat == "json"):
      writeJson(targetFile, dataObject)
    elif(targetFormat == "yaml"):
      writeYaml(targetFile, dataObject)
