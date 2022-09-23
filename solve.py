from re import *
import sys


def Get_args():
    if len(sys.argv) == 1 or '--help' in sys.argv:
        return None

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg == '--dictionary':
            dictionary = sys.argv[i+1]
            i = i + 1
        elif arg == '--letters':
            letters = sys.argv[i+1]
            i = i + 1
        elif arg == '--center':
            center = sys.argv[i+1]
            i = i + 1
        else:
            print("unknown arg %s" % arg)
            exit(1)

        i = i + 1

    try:
        return letters, center, dictionary
    except NameError:
        try:
            return letters, center, "popular.txt"
        except NameError:
            print("missing argument; --letters and --center are required")
            exit(1)


def Main():
    args = Get_args()

    if args == None:
        print("NYT Spelling Bee solver")
        print("usage: solve --letters [all letters] --center [center letter] --dictionary [path to dictionary file]")
        exit(1)

    letters = args[0]
    center_letter = args[1]
    dictionary_file = args[2]

    fd = open(dictionary_file)
    allwords = fd.readlines()

    matched_words = list()

    for line in allwords:
        line = line.strip()
        if match('^[%s%s]+$' % (center_letter, letters), line):
            if search(center_letter, line):
                if len(line) > 3:
                    matched_words.append(line)

    for word in matched_words:
        print(word)

    print("\n\nfound %s total words" % len(matched_words))


Main()
