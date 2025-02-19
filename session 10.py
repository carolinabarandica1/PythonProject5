import random
random_numbers = []
for i in range (18):
    num = random.randint(1,100)
    random_numbers.append(num)

filtered_numbers = [num * 2 for num in random_numbers if num %2 ==0]

print(random_numbers)
print("filtered_numbers and multiplied by 2", filtered_numbers)