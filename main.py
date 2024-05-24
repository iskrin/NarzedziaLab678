import argparse

def pharseArguments():
    parser = argparse.ArgumentParser(description="Program do kowersji między .xml, .yaml, .json") 
    parser.add_argument('currentFormat', type=str, help='Plik który chcemy przekonwertować z obecnym rozszerzeniem')
    #parser.add_argument('targetFormat', type=str, help='Plik który chcemy przekonwertować z docelowym rozszerzeniem')
    args = parser.parse_args()  
    return args

