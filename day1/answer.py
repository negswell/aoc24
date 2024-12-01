
from collections import Counter

arr1=[]
arr2=[]
with open('input.txt', 'r') as file:
    for line in file:
        val1,val2=line.strip().split()
        arr1.append(int(val1))
        arr2.append(int(val2))
arr1.sort()
arr2.sort()

result_of_first_question=0
for i in range(len(arr1)):
    result_of_first_question+=abs(arr1[i]-arr2[i])

counter_arr2 = Counter(arr2)
result_of_second_question=0
for val in arr1 :
    result_of_second_question+=(val * counter_arr2.get(val,0))

print(f"result_of_first_question is {result_of_first_question}")
print(f"result_of_second_question is {result_of_second_question}")



