import os
import yaml
from tqdm import tqdm

# 親のノードまでの1方向の構造を保存
# 自分の階層を分化，ループごとに別の物を出力
def make_list(i, list, export, last):
    for param in list[i]:
        export.append(param)
        if not i == len(list)-1:
            make_list(i+1, list, export, last)
        else:
            return last, export
    return last, export

a = [0, 1]
b = [True, False]
c = ["a", "b"]
list_test = [a, b]
last, export = make_list(0, list_test, [], [])
print(last)
print(export)