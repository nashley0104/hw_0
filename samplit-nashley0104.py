import random
import sys

filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    for line in file:
        if random.random() < 0.01:
            print(line, end="")
