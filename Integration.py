import os
import pandas as pd
from konlpy.tag import Mecab
from collections import Counter
from customNlp import mecab

#일반명사, 고유명사, 동사, 형용사, 일반 부사
TAG_LIST = ["NNG", "NNP", "VV", "VA", "MAG"]
RECOMMEND_LIST = ["높임말", "유의어", "준말"]

#Read dictionary csv and extract data
data = pd.read_csv("./crawling/corpus/secresumecsv.csv")
recommend_dict = data.loc[data['형태소'].isin(TAG_LIST)]

#Input File
INPUT_FILE = input("PLEASE GIVE RESUME : ")
f = open(INPUT_FILE, 'r')
input_text = f.read()
f.close()

tags = mecab.get_tags(input_text)
print(tags)
# ToDo : Taglist에 있는 것들로만 뽑아내기

