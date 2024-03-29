from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from joblib import dump

data = fetch_20newsgroups()

categories = ['comp.graphics', 'rec.autos', 'rec.motorcycles']
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train.data, train.target)
labels = model.predict(test.data)
test.target[0:10]
n = len(test.data)
corrects = [ 1 for i in range(n) if test.target[i] == labels[i] ]
print(n)
print(sum(corrects))
print(sum(corrects)*100/n)
dump(model, 'chatgroup.model')