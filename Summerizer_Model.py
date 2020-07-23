import nltk
import re
import heapq
def summerizer(text):
    sentences=nltk.sent_tokenize(text)
    clean_text=re.sub(r"\-|\.|\d|\"|\s+[a-zA-Z]\s+|\s+(km)\s+|\,|('s)"," ",text)
    clean_text=re.sub(r"\s+"," ",clean_text)
    stopwords=nltk.corpus.stopwords.words("english")
    word2count={}
    for word in nltk.word_tokenize(clean_text):
        if word not in stopwords:
            if word not in word2count.keys():
                word2count[word]=1
            else:
                word2count[word]+=1
    for key in word2count.keys():
        word2count[key]=word2count[key]/max(word2count.values())
    sent2score={}
    for sent in sentences:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word2count.keys():
                if len(sent.split(' '))<27: 
                    if sent not in sent2score:
                        sent2score[sent]=word2count[word]
                    else:
                        sent2score[sent]+=word2count[word]
    bestsent=heapq.nlargest(5,sent2score,key=sent2score.get)
    summerize=""
    for sent in bestsent:
        summerize+=sent
    return summerize

                      


 
 
 