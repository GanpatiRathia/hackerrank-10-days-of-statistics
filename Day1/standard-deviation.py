# problem link -> https://www.hackerrank.com/challenges/s10-standard-deviation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import math

def mean(data):
    return sum(data) / len(data)

def stddev(data, size):
    sum = 0
    for i in range(size):
        sum = sum + (data[i] - mean(data)) ** 2
    return math.sqrt(sum / size)

size = int(input())
numbers = list(map(int, input().split()))

print(round(stddev(numbers, size), 1))

# sample input 
#The first line contains an integer,N, denoting the number of elements in the array. -> 5
#The second line contains N space-separated integers describing the respective elements of the array. -> 10 40 30 50 20

# sample output -> 14.1