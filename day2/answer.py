

def isSafe(arr):
    asc=True
    desc=True
    for i in range(1,len(arr)):
        if arr[i]<=arr[i-1] or abs(arr[i]-arr[i-1]) > 3:
            asc= False
            break
    if asc :
        return True
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1] or abs(arr[i]-arr[i-1]) > 3:
            desc= False
            break
    return  desc


result_of_first_question=0
result_of_second_question=0
with open('input.txt', 'r') as file:
    for line in file:
        arr=list(map(int,line.strip().split()))
        if isSafe(arr):
            result_of_first_question+=1
        for i in range(len(arr)):
            if isSafe(arr[:i]+arr[i+1:]):
                result_of_second_question+=1
                break
            
print("result_of_first_question",result_of_first_question)
print("result_of_second_question",result_of_second_question)


    
   