"""
File name: process.py
Python Version: 3.7
"""
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize


class Process:
    """
    This class is used for cleaning value.
    """

    @staticmethod
    def alias(name_raw):
        """
        Clean the raw name to make the join possible.

        :param name_raw: the value in the csv file
        :type name_raw: string
        :return: string
        """
        lower = name_raw.lower()
        if re.match(r"([a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+)", lower): # is email only
            return lower
        else:
            with_multiple_space = re.sub(r"[^a-z0-9\s]+", " ", lower)
            return re.sub(r"\s{2,}", " ", with_multiple_space).strip()

    @staticmethod
    def content(raw, lemmatize):
        """
        Clean the content from the sentences appearing for every email and stop words.

        :param raw: the content as it is in the csv file
        :type raw: string
        :param lemmatize: how good should we reduce the word. (quality vs time)
        :type lemmatize: boolean
        :return: string
        """
        def is_writing_convention(line):
            return line == "U.S. Department of State" or \
                    line == "UNCLASSIFIED" or \
                    line.startswith("Case No.") or \
                    line.startswith("Doc No.") or \
                    line.startswith("STATE DEPT") or \
                    line.startswith("RELEASE IN") or \
                    line.startswith("SUBJECT TO AGREEMENT") or \
                    line.startswith("Subject") or \
                    line.startswith("Sent:") or \
                    line.startswith("Date:") or \
                    line.startswith("Cc:") or \
                    line.startswith("From:") or \
                    line.startswith("To:")

        if lemmatize:
            lmtzr = WordNetLemmatizer()
        else:
            snow = SnowballStemmer('english')
        useful_sentences = []
        frequent_words = [w.lower() for w in stopwords.words('english')]
        content_as_list = []
        for line in raw.splitlines():
            line = line.strip()
            if not is_writing_convention(line):
                tmp = line.lower()
                tmp = re.sub(r"\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}", " ", tmp)  # remove emails
                content_as_list.append(tmp)

        content_as_str = " ".join(content_as_list)
        for sentence_dirty in sent_tokenize(content_as_str):
            sent = re.sub(r"[^a-z\s]+", " ", sentence_dirty)  # keep only alpha
            sentence_not_reduced = []
            for word in nltk.word_tokenize(sent):
                if word not in frequent_words:
                    sentence_not_reduced.append(word)
            if len(sentence_not_reduced) >= 4:
                sentence_reduced = []
                for word_raw in sentence_not_reduced:
                    if lemmatize:
                        sentence_reduced.append(lmtzr.lemmatize(word_raw))
                    else:
                        sentence_reduced.append(snow.stem(word_raw))
                ###
                useful_sentences.append(' '.join(sentence_reduced))
        return '|'.join(useful_sentences)

