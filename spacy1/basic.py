from spacy import blank

nlp = blank('pt')

doc = nlp('Carlos foi a feira.')

token = doc[0] # Carlos

span = doc[:2] # Carlos foi

