import os
import csv
import pandas as pd
from customNlp import mecab

def CsvToDict(filename):
    mydict = dict()
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            if not rows[0] in mydict.keys():
                mydict[rows[0]] = rows[1].strip()
    return mydict
#일반명사, 고유명사, 동사, 형용사, 일반 부사
TAG_LIST = ["NNG", "NNP", "VV", "VA", "MAG"]

#Read dictionary csv and extract data
data = pd.read_csv("./crawling/corpus/resumeresultutf.csv", encoding="utf-8")
recommend_dict = data.loc[data['형태소'].isin(TAG_LIST)]
noun_dict = CsvToDict("./resources/Noun.csv")
verb_dict = CsvToDict("./resources/Verb.csv")

#Input File
INPUT_FILE = input("PLEASE GIVE RESUME : ")
try:
    f = open(INPUT_FILE, 'r')
    input_text = f.read()
    f.close()
except FileNotFoundError:
    print("File not exist!")
    exit();

tags = mecab.tokenize(input_text)
for item in tags:
    if not item[1] in TAG_LIST:
        continue
    if item[1][0] == 'N':
        print(item[0])
        '''
        if item[0] in noun_dict.keys(): #Check if it has 유의어or준말
            originalIdx = recommend_dict[recommend_dict["단어"] == item[0]]
            if not originalIdx.empty:
                print(originalIdx)
            recommendIdx = recommend_dict[recommend_dict["단어"] == noun_dict[item[0]]]
            if not recommendIdx.empty:
                print("Original Word : " + item[0])
                print("Recommend Word : " + noun_dict[item[0]])
        '''
    if item[1][0] == 'V':
        if item[0] in verb_dict.keys():
            print(verb_dict[item[0]])

