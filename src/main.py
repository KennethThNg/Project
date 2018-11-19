"""
File name: main.py
Python Version: 3.7
"""

import sys
from word2vec import Word2Vec

if __name__ == "__main__":
    arguments = [
        "transform_raw_database",
        "set_word2vec",
        "set_doc2vec"
    ]
    if len(sys.argv) != 2 or sys.argv[1] not in arguments:
        print("Enter a valid argument: " + str(arguments))
        sys.exit()
    if sys.argv[1] == arguments[0]:
        print("Please, use the notebook for that.")
    elif sys.argv[1] == arguments[1]:
        print("Running...")
        Word2Vec.train(True)
    elif sys.argv[1] == arguments[2]:
        raise NotImplementedError
    print("Done")
