#Problem Link -> https://www.hackerrank.com/challenges/s10-interquartile-range/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def median(size, values):
    if size % 2 == 0:
        median = (values[int(size/2)-1] + values[int(size/2)]) / 2
    else:
        median = float(values[int(size/2)])
    return median

size = int(input())
elements = list(map(int, input().split()))
frequencies = list(map(int, input().split()))

new_data = []
for i in range(len(elements)):
    for j in range(frequencies[i]):
        new_data.append(elements[i])
new_data = sorted(new_data)

size = int(len(new_data))
if size % 2 == 0:
    data_low = new_data[0:int(size/2)]
    data_high = new_data[int(size/2):size]
else:
    data_low = new_data[0:int(size/2)]
    data_high = new_data[int(size/2)+1:size]

low = median(len(data_low), data_low)
high = median(len(data_high), data_high)
print(high - low)

#Input Format
#The first line contains an integer,N, denoting the number of elements in arrays X and F. -> 6
#The second line contains N space-separated integers describing the respective elements of array X. -> 6 12 8 10 20 16
#The third line contains N space-separated integers describing the respective elements of array F. -> 5 4 3 2 1 5

#sample output -> 9.0