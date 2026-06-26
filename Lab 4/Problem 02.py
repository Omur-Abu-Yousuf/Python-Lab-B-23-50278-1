original = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 70, 'XII': 20}

count = {}

for key in original:
    value = original[key]
    
    if value in count:
        count[value] = count[value] + 1
    else:
        count[value] = 1

print(count)