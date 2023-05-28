# https://softeer.ai/practice/info.do?idx=1&eid=804
import string

word = input()
key = input()

alpha_list = list(string.ascii_uppercase)
key_map = list()
key_li = list()

# make key map
for k in key:
    try:
        alpha_list.remove(k)
        key_li.append(k)
        if len(key_li) == 5:
            key_map.append(key_li)
            key_li = []
    except:
        pass
for a in alpha_list:
    if a == 'J':
        continue
    key_li.append(a)
    if len(key_li) == 5:
        key_map.append(key_li)
        key_li = []

def is_firstcase(a, b):
    for key_li in key_map:
        if (a,b) in key_li:
            a_idx = (key_li.index(a) + 1) % 5
            b_idx = (key_li.index(b) + 1) % 5

            return key_li[a_idx], key_li[b_idx]

    return -1, -1

def is_secondcase(a, b):
    for i in range(5):
        col_list = []
        for j in range(5):
            col_list.append(key_map[j][i])
        if (a,b) in col_list:
            a_idx = (col_list.index(a) + 1) % 5
            b_idx = (col_list.index(b) + 1) % 5
            
            return key_map[a_idx][i], key_map[b_idx][i]
    
    return -1, -1

def is_thirdcase(a, b):
    for i in range(5):
        for j in range(5):
            if key_map[i][j] == a:
                ax = i
                ay = j
            if key_map[i][j] == b:
                bx = i
                by = j
    
    