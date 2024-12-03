import re

result_of_first_question=0
result_of_second_question=0
with open('input.txt', 'r') as file:
    text = file.read()
    number_pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(number_pattern, text)
    for match in matches:
        result_of_first_question+=int(match[0])*int(match[1])
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    matches = re.finditer(pattern, text)
    calculate=True
    for x in matches :
        if x.group() == "do()":
            calculate=True
        elif x.group() == "don't()":
            calculate=False
        elif calculate:
            match = re.search(number_pattern, x.group())
            result_of_second_question+=int(match.group(1))*int(match.group(2))

    
print("result_of_first_question",result_of_first_question)
print("result_of_second_question",result_of_second_question)


    
   