"""
Крестьянину нужно перевезти через реку
волка, козу и капусту. Но лодка такова,
что в ней может поместиться только
крестьянин, а с ним или одмн волки, или одна
коза, или одна капуста. Но если оставить
волка с козой то волк съест козу, а если
оставить козу с капустой, то коза съест
капусту. Как перевезти свой груз крестьянину?
"""

param = ["C","G","W"]
limit = [["C","G"],["G","W"]]

def correct():
    pass
    #
def ans_like_DFS(persons:list, limit:list):
    # Обходим все варианты вглубь
    answer = []
    while len(answer) != len(persons):
        #выкинуть одного из персонажей

        #проверить корректность для остатка
        #в списке героев

        

def ans_like_Graf():
    #
    pass