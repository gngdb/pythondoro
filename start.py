#!/usr/bin/python

import time
import sys
from tqdm import tqdm

def main():
    print("Working time...")
    sys.stdout.flush()
    for t in tqdm(range(60*25)):
        time.sleep(1)
    print("Break time...")
    sys.stdout.flush()
    for t in tqdm(range(60*5)):
        time.sleep(1)

if __name__ == "__main__":
    main()
