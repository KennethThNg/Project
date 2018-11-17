"""
File name: main.py
Python Version: 3.7
"""

import sys

if __name__ == '__main__':
    arguments = ["process_raw", "train_model"]
    if len(sys.argv) != 2 or sys.argv[1] not in arguments:
        print("Enter a valid argument: " + str(arguments))
        sys.exit()
    if sys.argv[1] == 'process_raw':
        print('Please, use the notebook for that.')
    elif sys.argv[1] == 'train_model':
        print('TODO')
