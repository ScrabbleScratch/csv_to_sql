#################################################
# PROGRAM TO CONVERT A TABLE INTO AN SQL SCRIPT #
#################################################

import errno
from os import strerror
from re import search

# Simple parsing function 
# TODO: correctly unescape characters 

def parse(line):
    tableCols = []
    cur = 0
    length = len(line)
    while cur < length:
        comma = line.find(",", cur)
        quote = line.find('"', cur)
        if comma == -1 and quote == -1:
            tableCols.append(line[cur:].strip())
            cur = length + 1
        elif comma < quote or quote == -1:
            tableCols.append(line[cur:comma])
            cur = comma + 1
        else:
            quote = line.find('"', cur + 1)
            double = line.find('""', cur + 1)
            temp = cur
            while double != -1 and quote == double:
                double += 2
                quote = line.find('"', double)
                double = line.find('""', double)
                if double != -1:
                    temp = double
            tableCols.append(line[cur + 1:line.find('"', temp + 2)].replace('""', '"'))
            cur = line.find(",", line.find('"', temp + 2)) + 1
    return tableCols

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
tableCols = []
header = table[0].split(",")
for row in table:
    t_row = row.split(",")
    print(len(t_row))
    tableCols.append(t_row)

#for i in tableCols:
    #print("NL: ", i)
print(len(tableCols))