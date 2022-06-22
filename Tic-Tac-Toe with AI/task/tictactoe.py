import random

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
def get_turn_symbol_from_table(table):
    count_x = [value for line in table for key, value in line.items()].count('X')
    count_o = [value for line in table for key, value in line.items()].count('O')
    if count_x <= count_o:
        return 'X'
    else:
        return 'O'

def get_result(tbl):
    result_str = None
    result = False
    diag1_el_lst = []
    diag2_el_lst = []
    el_num = 1
    for ln in convert_table(table):
        if all(el_val == 'X' for el_val in ln.values()):
            result_str = 'X wins'
            break
        elif all(el_val == 'O' for el_val in ln.values()):
            result_str = 'O wins'
            break
    if result_str is None:
        for ln in tbl:
            if all(el_val == 'X' for el_val in ln.values()):
                result_str = 'X wins'
                break
            elif all(el_val == 'O' for el_val in ln.values()):
                result_str = 'O wins'
                break
            diag1_el_lst.append(ln[(el_num, el_num)])
            diag2_el_lst.append(ln[(el_num, 4 - el_num)])
            el_num+=1
        if result_str is None:
            if all(el_val == 'X' for el_val in diag1_el_lst) or all(el_val == 'X' for el_val in diag2_el_lst):
                result_str = 'X wins'
            elif all(el_val == 'O' for el_val in diag1_el_lst) or all(el_val == 'O' for el_val in diag2_el_lst):
                result_str = 'O wins'
            elif any(el_val == '_' for ln in tbl for el_val in ln.values()) and result_str is None:
                result_str = 'Game not finished'
                result = True
            elif result_str is None:
                result_str = 'Draw'

    if any(el_val != '_' for ln in tbl for el_val in ln.values()):
        print(result_str)
    return result
# input_str = input('Enter the cells:').replace(' ', '')

def make_turn(table, new_pos, turn):
    for i, line in enumerate(table):
        if new_pos in line.keys():
            line[new_pos] = turn
            table[i] = line
            break
    return table

def get_computer_turn(table, occupied_cells, lvl):
    # print(occupied_cells)
    while True:
        new_pos_comp = (random.randint(1, len_x), random.randint(1, len_x))
        if new_pos_comp not in occupied_cells:
            break
    print('Making move level "' + lvl + '"')
    return new_pos_comp
def convert_table(table):
    tmp_lst = [{}, {}, {}]
    for i, line in enumerate(table):
        for j in range(1, len_x+1):
            tmp_lst[i][(i+1,j)] =  table[j-1][(j, i+1)]
    return tmp_lst

input_str = "_________"
table = get_table_from_str(input_str)
print_table(table)
occupied_cells = []
while get_result(table):
    turn = get_turn_symbol_from_table(table)
    if turn == 'X':
        occupied_cells = list(key for key, value in table[0].items() if value != '_') + list(key for key, value in table[1].items() if value != '_') + list(key for key, value in table[2].items() if value != '_')
        while True:
            input_str = input('Enter the coordinates:')
            input_lst = list(input_str.split(' '))
            if not all(map(lambda x: x.isdigit(), input_lst)):
                print('You should enter numbers!')
                continue
            new_pos = (int(input_lst[0]), int(input_lst[1]))
            if any(map(lambda x: int(x) > len_x, input_lst)):
                print('Coordinates should be from 1 to {0}!'.format(len_x))
                continue
            if new_pos in occupied_cells:
                print('This cell is occupied! Choose another one!')
                continue
            break
        table = make_turn(table, new_pos, turn)
        print_table(table)
    else:
        occupied_cells = list(key for key, value in table[0].items() if value != '_') + list(key for key, value in table[1].items() if value != '_') + list(key for key, value in table[2].items() if value != '_')
        if len(occupied_cells) == len_x * len_y:
            break
        new_pos_comp = get_computer_turn(table, occupied_cells, 'easy')
        table = make_turn(table, new_pos_comp, turn)
        print_table(table)
    # print(table)
    # print(convert_table(table))
