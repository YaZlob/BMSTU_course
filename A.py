"""
Дан пазл, в котором указаны начальное и конечное состояния
Написать алгоритм, реализующий оптимальный посик, используя
алгоритм А*
В качестве эвристики предлагается выбрать количество
числе стоящих не на своих местах
"""
from copy import deepcopy

# puzzle = input("for empty square enter *\n")
ans = "1 2 3 8 * 4 7 6 5"
puzzle = "2 8 3 1 6 4 7 * 5"


def convert2matrix(puzzle: str) -> list:
    return [puzzle.split()[i * 3:(i + 1) * 3] for i in range(3)]


def convert2string(puzzle: list) -> str:
    return " ".join(sum(puzzle, []))


def str_correct(current_puzzle: str, ans=ans):
    return len([1 for i, j in zip(current_puzzle, ans) if i == j and i != " "])


def check_correct(current_puzzle: list, ans=ans):
    count = 0
    ans_matrix = convert2matrix(ans)
    for i in range(len(ans_matrix)):
        for j in range(len(ans_matrix)):
            if ans_matrix[i][j] == current_puzzle[i][j]:
                count += 1
    return count


assert str_correct(puzzle, ans) == 4
assert check_correct(convert2matrix(puzzle), ans) == 4


def find_empty_square(current_puzzle: str):
    star_index = current_puzzle.split().index("*")
    column_index, row_index = star_index % 3, int(star_index / 3)
    return column_index, row_index


def check_move(current_puzzle: str, limit: int):
    _ = []
    column_index, row_index = find_empty_square(current_puzzle)
    # check column
    if column_index == limit:
        _.append([row_index, column_index - 1])
    elif column_index == 0:
        _.append([row_index, column_index + 1])
    else:
        _.append([row_index, column_index - 1])
        _.append([row_index, column_index + 1])

    # check row
    if row_index == limit:
        _.append([row_index - 1, column_index])
    elif row_index == 0:
        _.append([row_index + 1, column_index])
    else:
        _.append([row_index - 1, column_index])
        _.append([row_index + 1, column_index])

    return _


def all_variance(current_puzzle: str):
    _ = []
    matrix = convert2matrix(current_puzzle)
    limit = len(matrix) - 1
    star_column, star_row = find_empty_square(current_puzzle)
    for row, column in check_move(current_puzzle, limit):
        temp_matrix = deepcopy(matrix)
        temp_matrix[star_row][star_column], temp_matrix[row][column] = temp_matrix[row][column], temp_matrix[star_row][
            star_column]
        _.append(temp_matrix)
    return _


def step(variance: list, history: list):
    step_correct = [check_correct(i) for i in variance]
    best = step_correct.index(max(step_correct))
    if len(history) >= 2 and variance[best] == history[-2]:
        step_correct.pop(best)
        best = step_correct.index(max(step_correct))
    return variance[best]


def loop(current_puzzle: str):
    correct = str_correct(current_puzzle)
    steps = []
    steps.append(convert2matrix(current_puzzle))
    iteration = 0
    while correct != 8:
        iteration+=1
        print(iteration)
        variance = all_variance(current_puzzle)
        var = step(variance, steps)
        steps.append(var)
        current_puzzle = convert2string(var)
        correct = str_correct(current_puzzle)
    return steps


print(loop(puzzle))
