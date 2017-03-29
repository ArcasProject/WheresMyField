import collections
import itertools
from .nlp_tools import *
import functools
from operator import add, and_
from library import Article
from sklearn.cluster import KMeans

from django.db.models import Q

from sklearn.feature_extraction.text import TfidfVectorizer


class MachineLearning():
    """A machine learning class to output some useful information to the 
    user"""
    def __init__(self):
        self.name = 'machine-learning'
        self.co_authors = []

    def getData(keywords):
        query = reduce(operator.and_, (Q(first_name__contains = keyword) for keyword in keywords))
        self.data = Article.object.filter(query)

    def journals(self):
        """
        A method that returns that most frequent journal authors in database 
        publish 
        """
        self.journals = [article.journal for article in self.data]
        self.journals_freq = collections.Counter(self.journals)

    def author_connections(self):
        """
        A method which returns a list of co-authors: 
        """
        self.authors = [[name.name.lower() for name in art.author.all()] for
                         art in self.data]

        for au in self.authors:
            for pair in itertools.combinations(au, 2):
                if (pair[0] == pair[1]) is False:
                    self.co_authors.append(pair)

    def link_keywords(self):
        """
        A method which will return the 5 
        """

        self.titles = [article.title for article in self.data]
        self.abstracts = [article.abstract for article in self.data]

        self.text = map(add, self.titles, self.abstracts)


        tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                           min_df=0.01,
                                           tokenizer=nlp_tools.tokenize_text,
                                           ngram_range=(2, 3))

        tfidf_matrix = tfidf_vectorizer.fit_transform(self.text)

        terms = tfidf_vectorizer.get_feature_names()

        km = KMeans(n_clusters=1, max_iter=500)
        km.fit(tfidf_matrix)

        order_centroids = km.cluster_centers_.argsort()[:, ::-1]
        clusters = [[terms[ind] for ind in order_centroids[i, :]] for i in range(1)]
