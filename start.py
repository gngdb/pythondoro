#!/usr/bin/python

import time
from tqdm import trange

def main():
    bar = trange(60*25)
    bar.write("Working time...")
    for t in bar:
        time.sleep(1)
    bar = trange(60*5)
    bar.write("Break time...")
    for t in bar:
        time.sleep(1)

if __name__ == "__main__":
    main()
