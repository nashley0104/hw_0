import random
import sys

diff_prob = 1 / 100

filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    for line in file:
        if random.random() < diff_prob:
            print(line, end="")
