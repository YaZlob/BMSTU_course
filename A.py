"""
Дан пазл, в котором указаны начальное и конечное состояния
Написать алгоритм, реализующий оптимальный посик, используя
алгоритм А*
В качестве эвристики предлагается выбрать количество
числе стоящих не на своих местах
"""

# puzzle = input("for empty square enter *\n")
ans = "1 2 3 8 * 4 7 6 5"
puzzle = "2 8 3 1 6 4 7 * 5"


def convert2matrix(puzzle:str) ->list:
    return [puzzle.split()[i*3:(i+1)*3] for i in range(3)]

def check_correct(current_puzzle: str, ans: str):
    return len([1 for i, j in zip(current_puzzle, ans) if i == j and i != " "])

