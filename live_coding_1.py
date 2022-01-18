import spacy
nlp = spacy.load("en_core_web_sm")

mario = spacy.load("it_core_news_md")
doc_2=mario("lucia")
prova = list(doc_2.sents)[0]
print(prova)

with open("data/wiki_us.txt") as f:
    text = f.read()


doc = nlp(text)
print(len(text))
print(len(doc))

sentence1 = list(doc.sents)[0]
print(sentence1)

token2 = sentence1[2]
print(token2.text)
print(token2.left_edge)
print(token2.right_edge)
print(token2.ent_type_)
print(token2.lemma_)

print(sentence1[12].lemma_)

print(sentence1[12].pos_)




