len_x, len_y = 3, 3
def print_table(table):
    print('-' * 9)
    for line in table:
        print('| ' + ' '.join(line.values()).replace('_', ' ') + ' |')
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
    count_x = [symbol for symbol in input_str].count('X')
    count_o = [symbol for symbol in input_str].count('O')
    if count_x <= count_o:
        return 'X'
    else:
        return 'O'

def print_result(tbl):
    result = None
    diag1_el_lst = []
    diag2_el_lst = []
    el_num = 1
    for ln in tbl:
        if all(el_val == 'X' for el_val in ln.values()):
            result = 'X wins'
            break
        elif all(el_val == 'O' for el_val in ln.values()):
            result = 'O wins'
            break
        diag1_el_lst.append(ln[(el_num, el_num)])
        diag2_el_lst.append(ln[(el_num, 4 - el_num)])
        el_num+=1
    if all(el_val == 'X' for el_val in diag1_el_lst) or all(el_val == 'X' for el_val in diag2_el_lst):
        result = 'X wins'
    elif all(el_val == 'O' for el_val in diag1_el_lst) or all(el_val == 'O' for el_val in diag2_el_lst):
        result = 'O wins'
    elif any(el_val == '_' for ln in tbl for el_val in ln.values()) and result is None:
        result = 'Game not finished'
    elif result is None:
        result = 'Draw'
    print(result)

input_str = input('Enter the cells:').replace(' ', '')
table = get_table_from_str(input_str)
turn = get_turn_symbol(input_str)
# print(table)
print_table(table)
occupied_cells = list(key for key, value in table[0].items() if value != '_') + list(key for key, value in table[1].items() if value != '_') + list(key for key, value in table[2].items() if value != '_')
while True:
    input_str = input('Enter the coordinates:')
    input_lst = list(input_str.split(' '))
    if not all(map(lambda x: x.isdigit(), input_lst)):
        print('You should enter numbers!')
        continue
    new_pos = (int(input_lst[0]), int(input_lst[1]))
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
print_result(table)
# print(table)
