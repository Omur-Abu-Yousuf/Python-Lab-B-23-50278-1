def count_elements(my_list):
    count = {}
    
    for item in my_list:
        if item in count:
            count[item] = count[item] + 1
        else:
            count[item] = 1
    
    return count

numbers = [10, 20, 30, 30, 30, 30, 20, 40]
result = count_elements(numbers)

for key in result:
    print(key, "=>", result[key], end=", ")