import random
import sys
SAMPLE_PROB = 0.01


filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    for line in file:
        if random.random() < SAMPLE_PROB:
            print(line, end="")
