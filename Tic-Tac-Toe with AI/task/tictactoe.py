len_x, len_y = 3, 3
def print_table(table):
    print('-' * 9)
    for line in table:
        print('| ' + ' '.join(line.values()) + ' |')
    print('-' * 9)
def get_table_from_str(str):
    table = []
    i = 1
    j = 1
    table_line = {}
    for symbol in str:
        table_line[(i, j)] = symbol
        j += 1
        if j > len_x:
            i += 1
            j = 1
            table.append(table_line)
            table_line = {}
    return table
def get_turn_symbol(input_str):
    count_x = list(input_str.split()).count('X')
    count_o = list(input_str.split()).count('O')
    if count_x <= count_o:
        return 'X'
    else:
        return 'O'

def print_result():
    pass
input_str = input('Enter the cells:')
table = get_table_from_str(input_str)
turn = get_turn_symbol(input_str)
print(table)
print_table(table)
occupied_cells = list(key for key, value in table[0].items() if value != '_') + list(key for key, value in table[1].items() if value != '_') + list(key for key, value in table[2].items() if value != '_')
while True:
    input_str = input('Enter the coordinates:')
    input_lst = list(input_str.split(' '))
    new_pos = (int(input_lst[0]), int(input_lst[1]))
    if not all(map(lambda x: x.isdigit(), input_lst)):
        print('You should enter numbers!')
        continue
    if any(map(lambda x: int(x) > len_x, input_lst)):
        print('Coordinates should be from 1 to 3!')
        continue
    if new_pos in occupied_cells:
        print('This cell is occupied! Choose another one!')
        continue
    break
for i, line in enumerate(table):
    if new_pos in line.keys():
        line[new_pos] = turn
        table[i] = line
        break
print_table(table)
print_result()
