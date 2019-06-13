import os
import csv
import pandas as pd
from customNlp import mecab

#일반명사, 고유명사, 동사, 형용사, 일반 부사
TAG_LIST = ["NNG", "NNP", "VV", "VA", "MAG"]
FIXED_LIST = []

def CsvToDict(filename):
    mydict = dict()
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            if not rows[0] in mydict.keys():
                mydict[rows[0]] = rows[1].strip()
    return mydict

def fixingResume(original_file, changed_file):
    FIXED_LIST = []
    #Read dictionary csv and extract data
    data = pd.read_csv("./crawling/corpus/resumeresultutf.csv", encoding="utf-8")
    recommend_dict = data.loc[data['형태소'].isin(TAG_LIST)]
    noun_dict = CsvToDict("./resources/Noun.csv")
    verb_dict = CsvToDict("./resources/Verb.csv")

    #Input File
    try:
        f = open(original_file, 'r')
        input_text = f.read()
        f.close()
    except FileNotFoundError:
        return False

    tags = mecab.tokenize(input_text)
    for item in tags:
        if not item[1] in TAG_LIST:
            continue
        if item[1][0] == 'N':
            if item[0] in noun_dict.keys(): #Check if it has 유의어or준말
                originalIdx = recommend_dict[recommend_dict["단어"] == item[0]]
                recommendIdx = recommend_dict[recommend_dict["단어"] == noun_dict[item[0]]]
                if (originalIdx.empty) and (not recommendIdx.empty) :
                    input_text.replace(item[0], noun_dict[item[0]], 1)
                elif (not originalIdx.empty) and (not recommendIdx.empty):
                    if int(recommendIdx["횟수"]) > int(originalIdx["횟수"]):
                         input_text.replace(item[0], noun_dict[item[0]], 1)
        if item[1][0] == 'V':
            if item[0] in verb_dict.keys():
                print(verb_dict[item[0]])
    
    f = open(changed_file, 'w')
    f.write(input_text)
    f.close()
    
    return True

def getFixedList():
    return FIXED_LIST