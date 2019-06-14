# -*- coding: utf-8 -*-
import os
import csv
import pandas as pd
from customNlp import mecab

#일반명사, 고유명사, 동사, 형용사, 일반 부사
TAG_LIST = ["NNG", "NNP", "VV", "VA", "MAG"]
FIXED_LIST = []

def CsvToDict(filename):
    mydict = dict()
    with open(filename, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            if len(rows) < 2:
                continue
            if not rows[0] in mydict.keys():
                mydict[rows[0]] = rows[1].strip()
    return mydict


def changeWord(input_text, originalIdx, recommendIdx):
    if (not originalIdx.empty) and (recommendIdx.empty) :
        return input_text
    elif (originalIdx.empty) and (recommendIdx.empty):
        return input_text
    elif (not originalIdx.empty) and (not recommendIdx.empty):
        if int(recommendIdx["횟수"]) < int(originalIdx["횟수"]):
            return input_text

    original_Word = originalIdx["단어"].tolist()[0]
    replace_Word = recommendIdx["단어"].tolist()[0]
    if not replace_Word in FIXED_LIST:
        FIXED_LIST.append(replace_Word)
    return input_text.replace(original_Word, replace_Word, 1)


def fixingResume(original_file, changed_file):
    global FIXED_LIST
    FIXED_LIST = []
    #Read dictionary csv and extract data
    data = pd.read_csv("./corpus/resumeresult2.csv", encoding="utf-8")
    recommend_dict = data.loc[data['형태소'].isin(TAG_LIST)]
    noun_dict = CsvToDict("./resources/Noun.csv")
    verb_dict = CsvToDict("./resources/output.csv")

    #Input File
    try:
        f = open(original_file, 'r', encoding='utf-8')
        input_text = f.read()
        f.close()
    except FileNotFoundError:
        print("FileNotFoundError!")
        return False

    tags = mecab.tokenize(input_text)
    
    for item in tags:
        if not item[1] in TAG_LIST:
            continue
        originalIdx = recommend_dict[recommend_dict["단어"] == item[0]]

        if item[1][0] == 'N' and item[0] in noun_dict.keys():
            recommendIdx = recommend_dict[recommend_dict["단어"] == noun_dict[item[0]]]
        elif item[1][0] == 'V' and item[0] in verb_dict.keys():
            recommendIdx = recommend_dict[recommend_dict["단어"] == verb_dict[item[0]]]
        else:
            continue
            
        try:
            input_text = changeWord(input_text, originalIdx, recommendIdx)
        except TypeError:
            continue


    if os.path.isfile(changed_file):
        os.remove(changed_file)    
    f = open(changed_file, 'w', encoding='utf-8')
    f.write(input_text)
    f.close()
    return True

def getFixedList():
    global FIXED_LIST
    if len(FIXED_LIST) == 0:
        FIXED_LIST.append("SUCCESS")
    print(FIXED_LIST)
    return FIXED_LIST