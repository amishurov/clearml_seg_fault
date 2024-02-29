import time
import clearml
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str)
    return parser.parse_args()

def main_func(args):
    print(args)
    time.sleep(5)

if __name__ == '__main__':
    main_func(parse_args())

