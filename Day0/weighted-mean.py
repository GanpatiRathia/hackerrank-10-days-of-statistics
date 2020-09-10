#problem link -> https://www.hackerrank.com/challenges/s10-weighted-mean/problem?h_r=next-challenge&h_v=zen
size = int(input())
numbers = list(map(int, input().split()))
weighted = list(map(int, input().split()))

sum_items = 0
for i in range(size):
    sum_items = sum_items + (numbers[i] * weighted[i])

print(round(sum_items/sum(weighted), 1))
#The first line contains an integer,N, denoting the number of elements in arrays X and W. -> 5
#The second line contains N space-separated integers describing the respective elements of array X. -> 10 40 30 50 20
#The third line contains N space-separated integers describing the respective elements of array W. -> 1 2 3 4 5

#sample output -> 32.0