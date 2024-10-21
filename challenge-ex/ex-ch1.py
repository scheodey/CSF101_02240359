with open('fruit_transactions.txt', 'r') as file:
    data = file.readlines()

firstline = data [0]
print (f'The first line is : {firstline}')

length = len(data)
print(f'The length of this data is: {length}')

all_data = []
for line in data:
    line_dictionary = {}
    cleaned_line = line.replace('\n', '')
    splitted_line = cleaned_line.split(',')

    line_dictionary['name'] = splitted_line[0]
    line_dictionary['action'] = splitted_line[1]
    line_dictionary['quantity'] = int(splitted_line[2])
    line_dictionary['item'] = splitted_line[3]
    line_dictionary['price'] = float(splitted_line[4])

    all_data.append(line_dictionary)

total_sales = sum(item['quantity'] * item['price'] for item in all_data if item['action'] == 'sold')
print(f'The total sale from sold transaction is: ${total_sales}')

fruit_count = {}
for item in all_data:
    fruit = item['item']  
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1
    
popular_fruit = max(fruit_count, key=fruit_count.get)
popular_fruit_trans = fruit_count[popular_fruit]
print(f'The most popular fruit is: {popular_fruit} with {popular_fruit_trans} transactions.')


total_value = sum(item['quantity'] * item['price'] for item in all_data)
average = total_value / length
print(f'The average transaction value is: {average:.2f}')

spender = {}
for item in all_data:
    if item['action'] == 'bought':
        if item['name'] in spender:
            spender[item['name']] += item['quantity'] * item['price']
        else:
            spender[item['name']] = item['quantity'] * item['price']

biggest_spender = max(spender, key=spender.get)
amount = spender[biggest_spender]
print(f'The biggest spender is: {biggest_spender} with total spent of: ${amount:.2f}')

summary = (
    f'Total sales from sold transaction is: {total_sales} \n'
    f'The most popular fruit is: {popular_fruit}\n'
    f'The average transaction value is: {average}\n'
    f'The biggest spender is: {biggest_spender}'
)

with open('transaction_summary.txt', 'w') as file:
    file.write(summary)

print(f'The summary has been written in transaction_summary.txt')