from konlpy.tag import Mecab
from collections import Counter
import csv

            
mecab = Mecab()

def tokenize(text, ntags=10000):
    sentences = mecab.pos(text)
    return sentences

def get_tags(text, ntags=10000):
    sentences = mecab.pos(text)
    count = Counter(sentences)
    return_list = []
    for n, c in count.most_common(ntags):
        temp = {'tag':n, 'count':c}
        return_list.append(temp)
        
    return return_list

textlist = str()
sen_count = 10000
    
for i in range(1,853):
    n = str(i)
    f = open("/mnt/c/Users/MinsooKang/Documents/GitHub/CauNlpResume/crawling/corpus2/resume" + n+".txt", 'r')        
    text = f.read()
    textlist = textlist + text
    f.close
    
    
wf = open("/mnt/c/Users/MinsooKang/Documents/GitHub/CauNlpResume/crawling/corpus2/resumeresult.csv", 'w', encoding='euc-kr', newline='')
wr = csv.writer(wf)
wr.writerow(["단어", "형태소", "횟수"])

tags = get_tags(textlist, sen_count)
    
for tag in tags:
    sentence = tag['tag']
    count = tag['count']
    word, wpos = sentence
    if word == '\u30fb' or word == '\u2013':
        continue
    wr.writerow([word, wpos, count])
wf.close
