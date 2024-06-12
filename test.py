# SuperFastPython.com
# example of benchmarking a statement with timeit.repeat()
from timeit import repeat
# benchmark the statement
results = repeat('[i*i for i in range(1000)]', repeat=3, number=10000)
# report the durations
print(results)
# report the min duration
print(min(results))



