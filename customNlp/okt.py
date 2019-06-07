from konlpy.tag import Okt
from collections import Counter
import csv

            

def get_tags(text, ntags=500):
    okt = Okt()
    sentences = okt.pos(text)
    count = Counter(sentences)
    return_list = []
    for n, c in count.most_common(ntags):
        temp = {'tag':n, 'count':c}
        return_list.append(temp)
        
    return return_list

for i in range(1,2):
    n = str(i)
    f = open("/mnt/c/Users/MinsooKang/Documents/GitHub/CauNlpResume/crawling/corpus/resume" + n+".txt", 'r')
    wf = open("/mnt/c/Users/MinsooKang/Documents/GitHub/CauNlpResume/crawling/corpus/resumecsv"+ n+".csv", 'w', encoding='euc-kr', newline='')
    wr = csv.writer(wf)
    sen_count = 500
        
    text = f.read()
    tags = get_tags(text, sen_count)
    wr.writerow(["단어", "형태소", "횟수"])
    for tag in tags:
        sentence = tag['tag']
        count = tag['count']
        word, wpos = sentence
        print(sentence)
        wr.writerow([word, wpos, count])
    f.close
    wf.close
