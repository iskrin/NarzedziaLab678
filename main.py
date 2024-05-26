import json
import yaml
import xmltodict as xml
from pathlib import Path


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
        print("Error while reading source file (xml)")

def writeXml(filePath, dataObject):    #Zapisuje obiekt jako plik yaml
    with open(filePath, "w") as xmlFile:
            xmlData = xml.unparse(dataObject, pretty = True, full_document=False)
            xmlFile.write(xmlData)



def convert(sourceFile, targetFormat, targetPath):
    sourceFormat = sourceFile.split('.')[-1]
    currentPath = Path(sourceFile)
    filename = currentPath.with_suffix("." + str(targetFormat)).name
    targetPath = Path(targetPath) / filename
    print("target path")
    print(targetPath)
    
    

    if(sourceFormat == "json"):
        dataObject = readJson(currentPath) 
        if(targetFormat == "json"):
            writeJson(targetPath, dataObject)
        elif(targetFormat == "yaml"):
            writeYaml(targetPath, dataObject)
        elif(targetFormat == "xml"):
            writeXml(targetPath, dataObject)
        else:
            print("Invalid file format")

    elif(sourceFormat == "yaml"):
        dataObject = readYaml(sourceFile) 
        
        if(targetFormat == "json"):
            writeJson(targetPath, dataObject)
        elif(targetFormat == "yaml"):
            writeYaml(targetPath, dataObject)
        elif(targetFormat == "xml"):
            writeXml(targetPath, dataObject)
        else:
            print("Invalid file format")

    elif(sourceFormat == "xml"):
        dataObject = readXml(sourceFile) 
        
        if(targetFormat == "json"):
            writeJson(targetPath, dataObject)
        elif(targetFormat == "yaml"):
            writeYaml(targetPath, dataObject)
        elif(targetFormat == "xml"):
            writeXml(targetPath, dataObject)
        else:
            print("Invalid file format")
    else:
        print("Invalid file format")

