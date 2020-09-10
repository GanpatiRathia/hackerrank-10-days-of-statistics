#Problem link -> https://www.hackerrank.com/challenges/s10-quartiles/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def median(size, values):
    if size % 2 == 0:
        median = (values[int(size/2)-1] + values[int(size/2)]) / 2
    else:
        median = values[int(size/2)]
    return int(median)

# Set the data
size = int(input())
numbers = sorted(list(map(int, input().split())))

# Verify that the total data is even or odd
if size % 2 == 0:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2):size]
else:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2)+1:size]

# Get the final result and print on the screen
print (median(len(data_low), data_low))
print (median(size, numbers))
print (median(len(data_high), data_high))

#smaple input 
#The first line contains an integer,N, denoting the number of elements in the array. -> 9
#The second line contains N space-separated integers describing the array's elements. -> 3 7 8 5 12 14 21 13 18

#sample output
#6
#12
#16