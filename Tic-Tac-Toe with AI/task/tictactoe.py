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
def get_diag_el_lst(tbl):
    diag1_el_lst = []
    diag2_el_lst = []
    el_num = 1
    for ln in tbl:
        diag1_el_lst.append(ln[(el_num, el_num)])
        diag2_el_lst.append(ln[(el_num, 4 - el_num)])
        el_num += 1
    return diag1_el_lst, diag2_el_lst

def get_position_to_win(tbl, turn, occupied_cells):
    result_pos = None
    diag1_el_lst, diag2_el_lst = get_diag_el_lst(tbl)
    # print('Ход ', turn)
    # print('diag1_el_lst ', diag1_el_lst)
    # print('diag2_el_lst ', diag2_el_lst)
    for ln in convert_table(tbl):
        if sum(el_val == turn for el_val in ln.values()) == 2:
            result_pos = [(el_key[1], el_key[0]) for el_key, el_val in ln.items() if el_val != turn][0]
            if result_pos in occupied_cells:
                result_pos = None
            else:
                break
    if result_pos is None:
        for ln in tbl:
            if sum(el_val == turn for el_val in ln.values()) == 2:
                result_pos = [el_key for el_key, el_val in ln.items() if el_val != turn][0]
                if result_pos in occupied_cells:
                    result_pos = None
                else:
                    break
    if result_pos is None:
        if sum(el_val == turn for el_val in diag1_el_lst) == 2:
            result_pos = [(i+1, i+1) for i, el_val in enumerate(diag1_el_lst) if el_val != turn][0]
        if sum(el_val == turn for el_val in diag2_el_lst) == 2:
            result_pos = [(i+1, 3 - i) for i, el_val in enumerate(diag2_el_lst) if el_val != turn][0]
        result_pos = result_pos if result_pos not in occupied_cells else None
    # print('result_pos ', result_pos)
    # print('occupied_cells', occupied_cells)
    return result_pos


def get_result(tbl):
    result_str = None
    result = False
    diag1_el_lst, diag2_el_lst = get_diag_el_lst(tbl)
    for ln in convert_table(tbl):
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

def make_turn(table, new_pos, turn):
    for i, line in enumerate(table):
        if new_pos in line.keys():
            line[new_pos] = turn
            table[i] = line
            break
    return table

def get_computer_turn(table, occupied_cells, lvl, turn):

    if lvl == 'easy':
        while True:
            new_pos_comp = (random.randint(1, len_x), random.randint(1, len_x))
            if new_pos_comp not in occupied_cells:
                break
    elif lvl == 'medium':
        new_pos_comp = get_position_to_win(table, turn, occupied_cells)
        # print('Выигрышная позиция ' + str(new_pos_comp))
        if new_pos_comp is None:
            new_pos_comp = get_position_to_win(table, 'X' if turn == 'O' else 'O', occupied_cells)
        # print('Позиция, чтобы нее проиграть ' + str(new_pos_comp))
        if new_pos_comp is None:
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
def get_new_pos_user(occupied_cells, len_x):
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
    return new_pos
input_str = "_________"
role_list = ['easy', 'medium']
occupied_cells = []
players = {}
while True:
    input_command_str = input()
    coorect_command = False
    if input_command_str == 'exit':
        break
    else:
        input_command = input_command_str.split(' ')
        if len(input_command) == 3 and input_command[0] == 'start' and input_command[1] in ['user'] + role_list and input_command[2] in ['user'] + role_list:
            coorect_command = True
            players['X'] = input_command[1]
            players['O'] = input_command[2]
    if coorect_command:
        table = get_table_from_str(input_str)
        print_table(table)
        while get_result(table):
            turn = get_turn_symbol_from_table(table)
            # if turn == 'X':
            occupied_cells = list(key for key, value in table[0].items() if value != '_') + list(key for key, value in table[1].items() if value != '_') + list(key for key, value in table[2].items() if value != '_')
            if len(occupied_cells) == len_x * len_y:
                break
            if players[turn] == 'user':
                new_pos = get_new_pos_user(occupied_cells, len_x)
            if players[turn] in role_list:
                new_pos = get_computer_turn(table, occupied_cells, players[turn], turn)
            table = make_turn(table, new_pos, turn)
            print_table(table)
    else:
        print("Bad parameters!")
