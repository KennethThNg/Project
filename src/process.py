"""
File name: process.py
Python Version: 3.7
"""
import re
from nltk.corpus import stopwords


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
    def content(raw):
        """
        Clean the content from the sentences appearing for every email and stop words.

        :param raw: the content as it is in the csv file
        :type raw: string
        :return: string
        """
        without_common_sentence = []
        for line in raw.splitlines():
            line = line.strip()
            if line != "U.S. Department of State" and \
                    line != "UNCLASSIFIED" and \
                    not line.startswith("Case No.") and \
                    not line.startswith("Doc No.") and \
                    not line.startswith("STATE DEPT") and \
                    not line.startswith("RELEASE IN") and \
                    not line.startswith("SUBJECT TO AGREEMENT") and \
                    not line.startswith("Subject") and \
                    not line.startswith("Sent:") and \
                    not line.startswith("Date:") and \
                    not line.startswith("Cc:") and \
                    not line.startswith("From:") and \
                    not line.startswith("To"):
                tmp = re.sub(r"[^a-z0-9\s]+", " ", line.lower())
                tmp =  re.sub(r"\s{2,}", " ", tmp).strip()
                without_common_sentence.append(tmp)
        word_list = ' '.join(without_common_sentence).split()
        filtered_words = [word for word in word_list if word not in stopwords.words('english')]
        return ' '.join(filtered_words)
