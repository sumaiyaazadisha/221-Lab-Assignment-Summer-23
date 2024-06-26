# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JmAOcyQU6-YeKoL08Es7J3eFuk62yjX4
"""

#Task-02
input = open('/content/input2.txt', 'r')
output_file = open('/content/output2.txt','w')
N = int(input.readline().strip())
arr = input.readline().strip().split(" ")
array = []
for ele in arr:
  array.append(int(ele))

def find_max(array,N):
    array_sqr = []
    maximum = 0
    array_sqr = [(array[i]**2, i) for i in range(N)]
    array_sqr.sort()

    if array_sqr[N - 1][1] == 0:
        for j in range(array_sqr[N - 2][1], 0, -1):
            if array_sqr[N - 2][0] + array[j - 1] > maximum:
                maximum = array_sqr[len(array) - 2][0] + array[j - 1]
    else:
        for j in range(array_sqr[N - 1][1], 0, -1):
            if array_sqr[N - 1][0] + array[j - 1] > maximum:
                maximum = array_sqr[N - 1][0] + array[j - 1]

    return maximum


print(find_max(array, N), file = output_file)
output_file.close()