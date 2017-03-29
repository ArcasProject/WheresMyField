import collections
import itertools
from .nlp_tools import *
from library.models import Article
import functools
from operator import add, and_, or_
from sklearn.cluster import KMeans

from django.db.models import Q

from sklearn.feature_extraction.text import TfidfVectorizer


class MachineLearning():
    """A machine learning class to output some useful information to the 
    user"""
    def __init__(self):
        self.name = 'machine-learning'
        self.co_authors = []

    def getData(self, keywords):
        query = functools.reduce(or_, (Q(title__contains = keyword) for keyword in keywords), Q(title__contains=''))
        self.data = Article.objects.filter(query)
        print(len(self.data))

    def journals(self):
        """
        A method that returns that most frequent journal authors in database 
        publish 
        """
        journals_list = [article.journal for article in self.data]
        return collections.Counter(journals_list)

    def author_connections(self):
        """
        A method which returns a list of co-authors: 
        """

        authors = [[name.name.lower() for name in art.author.all()] for
                         art in self.data]
        co_authors = []
        for au in authors:
            for pair in itertools.combinations(au, 2):
                if (pair[0] == pair[1]) is False:
                    co_authors.append(pair)
        return co_authors

    def link_keywords(self):
        """
        A method which will return the pairs of famous words
        """

        titles = [article.title for article in self.data]
        abstracts = [article.abstract for article in self.data]

        text = map(add, titles, abstracts)


        tfidf_vectorizer = TfidfVectorizer(max_features=200000,
                                           tokenizer=tokenize_text,
                                           ngram_range=(2, 3))

        tfidf_matrix = tfidf_vectorizer.fit_transform(text)

        terms = tfidf_vectorizer.get_feature_names()

        km = KMeans(n_clusters=1, max_iter=500)
        km.fit(tfidf_matrix)

        order_centroids = km.cluster_centers_.argsort()[:, ::-1]
        clusters = [[terms[ind] for ind in order_centroids[i, :]] for i in range(1)]

        return clusters 
