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

param = ["C", "G", "W"]

limit = [
    ["C", "G"],
    ["G", "W"]]


def all_variance(array: list):
    param = set(array)
    return [[list(param - set(i)), i] for i in array]

assert len(all_variance(param)) == 3
print(all_variance(param))

def check_correct(array: list, limits: list):
    if len(array) <= 1:
        return True
    else:
        array.sort()
        if array == limits[0] or array == limits[1]:
            return False
    return True


assert False == check_correct(["G", "C"], limit)
assert True == check_correct(["C", "W"], limit)
assert True == check_correct(["C"], limit)

def like_DFS(params, limits):
    ans=[]
    # while left beach not empty
    while params:
        # check left beach
        variance = all_variance(params)
        for var in variance:
            if check_correct(var[0], limits) and len(variance)>1:
                print("Перевожу на правый берег:{}".format(var[1]))
                ans.append(var[1])
                params.pop(params.index(var[1]))
                break
            elif len(variance) == 1:
                print("Перевожу на правый берег:{}".format(params[0]))
                ans = ans + params

        # check right beach
        if not check_correct(ans, limits) and len(ans) < 3:
            print("Перевожу на левый берег:{}".format(ans[0]))
            params.append(ans[0])
            ans.pop(0)

        elif len(ans) ==3:
            return ans

print(like_DFS(param, limit))