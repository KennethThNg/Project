"""
File name: word2vec.py
Python Version: 3.7
"""
import gensim
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class Analyse:
    """
    This class is used for complex operations.
    """

    @staticmethod
    def tfidf_matrix(documents):
        corpus = []
        for doc in documents:
            corpus.append(str(doc).replace("|", " "))

        vectorizer = TfidfVectorizer(max_df=0.5, max_features=200000,
                                     min_df=0.01, stop_words='english',
                                     use_idf=True, ngram_range=(1,3))
        matrix = vectorizer.fit_transform(corpus)

        return matrix

    @staticmethod
    def word2vec():
        """
        Generate the binary files.

        :return: void
        """
        documents = pd.read_csv("../generated/emails.csv").content
        sentences = []
        for doc in documents:
            for s in str(doc).split("|"):
                sentences += [s.split()]
        model = gensim.models.Word2Vec(
            sentences,
            size=20,
            window=5,
            min_count=2,
            workers=4)
        model.train(sentences, total_examples=len(sentences), epochs=300)
        model.save('model_word2vec.bin')
