# !/usr/bin/python
# -*- coding:utf-8 -*-
from gensim import corpora, models, similarities
from pprint import pprint

if __name__ == "__main__":
    f = open('22.LDA_test.txt')
    stop_list = set('for a of the and to in'.split())
    lines = [line.strip().lower().split() for line in f]
    texts = [[word for word in line if word not in stop_list]for line in lines]
    print 'Texts='
    pprint(texts)

    dictionary = corpora.Dictionary(texts)
    V = len(dictionary)
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpus_tfidf = models.TfidfModel(corpus)[corpus]

    print 'TF-IDF:'
    for c in corpus_tfidf:
        print c

    print '\nLSI Model:'
    lsi = models.LsiModel(corpus_tfidf, num_topics=2, id2word=dictionary)
    topic_result = [a for a in lsi[corpus_tfidf]]
    pprint(topic_result)

    print 'LSI Topics:'
    pprint(lsi.print_topics(num_topics=2, num_words=5))
    similarity = similarities.MatrixSimilarity(lsi[corpus_tfidf])
    print 'similarity'
    pprint(list(similarity))





