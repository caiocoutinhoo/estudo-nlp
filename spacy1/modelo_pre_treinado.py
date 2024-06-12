from spacy import load
nlp = load('pt_core_news_lg')
doc = nlp('Eduardo foi a feira. Comprou dois pasteis')

for sent in doc.sents:
    print(sent)
