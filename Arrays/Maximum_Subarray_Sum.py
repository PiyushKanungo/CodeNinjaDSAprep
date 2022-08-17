
from sys import stdin,setrecursionlimit


def maxSubArraySum(arr,size):
    max_till_now =arr[0]
    max_ending = 0

    for i in range(0, size):
        max_ending = max_ending + arr[i]
        if max_ending < 0:
            max_ending = 0

        elif(max_till_now <  max_ending):
            max_till_now = max_ending

    return max_till_now


size = int(input())
    
arr = list(map(int, stdin.readline().strip().split(" ")))

print(maxSubArraySum(arr,size))

