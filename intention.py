import csv
import integration
from customNlp import mecab

#This code is for verb.csv pre processing

verb_dict = CsvToDict("./resources/Verb.csv")
verb_newDict = dict()
for key, item in verb_dict.items():
    verb_key = mecab.tokenize(key)
    verb_item = mecab.tokenize(item)
    verb_newDict[verb_key[0][0]] = verb_item[0][0]

wf = open("./resources/output.csv")
wr = csv.writer(wf)
for key, item in verb_newDict.items():
    wr.writerow([key, item])
wf.close