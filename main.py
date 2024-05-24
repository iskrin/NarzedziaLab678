import argparse
import json

def pharseArguments():
    parser = argparse.ArgumentParser(description="Converter between .xml, .yaml, .json") 
    parser.add_argument('sourceFile', type=str, help='Source file that we want to convert')
    #parser.add_argument('targetFile', type=str, help='Target file with a desired extension')
    args = parser.parse_args()  
    return args

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except ValueError:
        print("Error while reading source file")

args = pharseArguments()

sourceFile = args.sourceFile
currentFormat = sourceFile.split(".")[-1]

output = read_json(sourceFile)
print(output)