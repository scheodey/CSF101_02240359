with open('fruit_transactions.txt', 'r') as file:
    data = file.readlines()

firstline = data [0]
print (f'The first line is : {firstline}')

length = len(data)
print(f'The length of this data is: {length}')