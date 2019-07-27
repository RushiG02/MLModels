import numpy as np
import scipy.stats as stats

number_array =list()
n = int(input())
number_array = list(map(int,input().split()))
print(np.mean(number_array))
print(np.median(number_array))
mode = stats.mode(number_array, axis = None)
print(int(mode[0]))
print("%.1f" %np.std(number_array))

std    = round(np.std(number_array),1)
low    = round(np.mean(number_array)-1.960*(np.std(number_array)/(n**0.5)),1)
upp    = round(np.mean(number_array)+1.960*(np.std(number_array)/(n**0.5)),1)


print(low, upp)
