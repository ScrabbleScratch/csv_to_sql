#################################################
# PROGRAM TO CONVERT A TABLE INTO AN SQL SCRIPT #
#################################################

import errno
from os import strerror
from re import search, split

# open the table to be converted
while True:
    try:
        file = input("File to be converted (.csv): ")
        # check if the extension is valid and try to open the file
        if search(r"(\.csv)$", file):
            # open file and read content inside local var called 'table' then close the file
            stream = open(file, "rt", encoding="utf-8")
            table = stream.readlines()
            stream.close()
            break
        else:
            raise Exception("[CustomError] Invalid extension!")
    except Exception as E:
        print(E, "Try again!\n", sep="\n")

# separate each column in a new variable
csvPattern = r"\".+?\"|[^\"]+?(?=,)|(?<=,)[^\"]+"
tableCols = []
header = table[0].split(",")
for row in table:
    t_row = split(csvPattern, row)
    print(len(t_row))
    tableCols.append(t_row)

print(len(tableCols))
