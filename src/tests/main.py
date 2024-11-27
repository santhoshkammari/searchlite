import time
from statistics import mean

from src.searchlite import google

def first():
    def internal():
        t = time.perf_counter()
        google("when is kohli born?")
        e = time.perf_counter()
        return e - t
    return mean([internal() for _ in range(10)])

if __name__ == '__main__':
    print(first())
