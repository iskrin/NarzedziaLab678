import argparse
import json

def pharseArguments():
    parser = argparse.ArgumentParser(description="Converter between .xml, .yaml, .json") 
    parser.add_argument('sourceFile', type=str, help='Source file that we want to convert') #Plik wejsciowy
    parser.add_argument('targetFile', type=str, help='Target file with a desired extension') #Plik docelowy
    args = parser.parse_args()  
    return args

def readJson(filePath): #Czyta jsona i zwaraca obiekt z zawartoscia
    try:
        with open(filePath, 'r') as f:
            data = json.load(f)
        return data
    except ValueError:
        print("Error while reading source file (json)")

def writeJson(filePath, dataObject):    #Zapisuje obiekt jako json
    with open(filePath, "w") as jsonFile:
            json.dump(dataObject, jsonFile)

args = pharseArguments()    #argumenty

sourceFile = args.sourceFile    #nazwa pliku wejsciowego wraz z rozszerzeniem
currentFormat = sourceFile.split(".")[-1]   #rozszerze pliku wejsciowego

targetFile = args.targetFile    #nazwa pliku docelowego wraz z rozszerzeniem
targetFormat = targetFile.split(".")[-1]    #rozszerze pliku docelowego

if(currentFormat == "json"):
    dataObject = readJson(sourceFile) 

    if(targetFormat == "json"):
      writeJson(targetFile, dataObject)  
    