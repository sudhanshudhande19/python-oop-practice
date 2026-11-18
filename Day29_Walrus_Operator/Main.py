print('=================================')
print('       SMART DATA ANALYZER')
print('=================================')



Original_Numbers = [10, 20, 30, 40, 50]
print()
all = [w for  w in Original_Numbers if w > (avg := sum(Original_Numbers) / len(Original_Numbers))]
print(f'Total : {sum(Original_Numbers)}')
print(f'Average : {avg}')

print()
print('Numbers Greater Than Average:')
print(all)

print()
result =  [square for number in  Original_Numbers if (square := number * number) > 10]
print('Squares :')
print(result)

print()
total =  [square for number in  Original_Numbers if (square := number * number) > 1000]
print('Squares Greater Than 1000:')
print(total)