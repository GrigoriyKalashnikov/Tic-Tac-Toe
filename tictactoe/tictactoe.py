field = [' ' for i in range(9)]
field_list = [field[i:i+3] for i in range(0, len(field), 3)]


def draw_field(field_list):
    print('---------')
    print('| ' + field_list[0][0] + ' ' + field_list[0][1] + ' ' + field_list[0][2] + ' |')
    print('| ' + field_list[1][0] + ' ' + field_list[1][1] + ' ' + field_list[1][2] + ' |')
    print('| ' + field_list[2][0] + ' ' + field_list[2][1] + ' ' + field_list[2][2] + ' |')
    print('---------')


def check_win():
    interim_columns_list = [i[j] for j in range(len(field_list)) for i in field_list]
    columns_list = [interim_columns_list[i:i+3] for i in range(0, len(interim_columns_list), 3)]
    main_diag = [[columns_list[0][0], columns_list[1][1], columns_list[2][2]]]
    side_diag = [[columns_list[2][0], columns_list[1][1], columns_list[0][2]]]
    total_list = field_list + columns_list + main_diag + side_diag
    x_win = ['X', 'X', 'X']
    o_win = ['O', 'O', 'O']
    if x_win in total_list and o_win not in total_list:
        print('X wins')
        return True
    elif o_win in total_list and x_win not in total_list:
        print('O wins')
        return True


def main():
    cnt = 0
    draw_field(field_list)
    while True:
        if cnt % 2 == 1:
            player = 'O'
        else:
            player = 'X'
        coordinates = input('Enter the coordinates: > ').split()
        new_row = 3 - int(coordinates[1])
        new_col = int(coordinates[0]) - 1
        if len(coordinates) > 2 or coordinates[0].isnumeric() is False or coordinates[1].isnumeric() is False:
            print('You should enter numbers!')
        elif int(coordinates[0]) > 3 or int(coordinates[0]) < 1 or int(coordinates[1]) > 3 or int(coordinates[1]) < 1:
            print('Coordinates should be from 1 to 3!')
        elif field_list[new_row][new_col] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            field_list[new_row][new_col] = player
            draw_field(field_list)
            cnt += 1
            if cnt > 4:
                if check_win():
                    break
            if cnt == 9:
                print('Draw')
                break


main()






