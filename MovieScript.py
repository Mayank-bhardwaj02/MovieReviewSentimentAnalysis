import numpy as np
import pandas as pd

df = pd.read_csv('IMDBDataset.csv')



#Dividing into independent and dependent variables
x = df.iloc[:,0].values
y = df.iloc[:,1].values

#Splitting in training and test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train , y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#Building a pipleine
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

text_clf = Pipeline([('tfidf',TfidfVectorizer()),
                     ('clf',LinearSVC())])

text_clf.fit(x_train, y_train)

def predict_sentiment(text):
    sentiment = text_clf.predict([text])
    answer = " ".join(sentiment)
    return answer



