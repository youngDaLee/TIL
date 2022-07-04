n = int(input())
n_li = list(map(int, input().split()))
n_dict = dict.fromkeys(n_li, 1)
m = int(input())
m_li = list(map(int, input().split()))

for m in m_li:
    try:
        print(n_dict[m])
    except:
        print(0)
