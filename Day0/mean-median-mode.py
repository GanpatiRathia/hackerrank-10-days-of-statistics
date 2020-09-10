#problem link ->https://www.hackerrank.com/challenges/s10-basic-statistics/problem
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))
#input -> first line no. of inputs, second line inputs separated by space
#10
#64630 11735 14216 99233 14470 4978 73429 38120 51135 67060