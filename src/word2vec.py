"""
File name: word2vec.py
Python Version: 3.7
"""
import gensim
import pandas as pd


class Word2Vec:
    """
    This class is used for convert words into vectors based on emails as corpus.
    """

    @staticmethod
    def train(based_on_word):
        """
        Generate the binary files.

        :param based_on_word: Should it run on word or document
        :type based_on_word: boolean
        :return: void
        """
        documents = pd.read_csv("../generated/emails.csv").content
        if based_on_word:
            sentences = []
            for doc in documents:
                for s in str(doc).split(". "):
                    sentences += [s.split()]
            model = gensim.models.Word2Vec(
                sentences,
                size=20,
                window=5,
                min_count=2,
                workers=4)
            model.train(sentences, total_examples=len(sentences), epochs=50)
            model.save('model_word2vec.bin')
        else:
            raise NotImplementedError
