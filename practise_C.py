counter = 0
for num in range(2000,3001):
    if num % 13 == 0:
        counter = counter + 1
        if counter ==2:

            print(num)
            break
