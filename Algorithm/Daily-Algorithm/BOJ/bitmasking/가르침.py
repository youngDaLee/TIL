from itertools import combinations

def solution(n,k):
    words = list()
    antatica = set(map(str, 'antatica'))
    for _ in range(n):
        w = set(map(str, input()))
        word = list(w - antatica)
        words.append(word)
    
    if k<5:
        return 0
    k -= 5
    alpabet = set(map(lambda x:chr(x), range(ord('a'), ord('z')+1))) - antatica
    combs = combinations(alpabet, k)
    result = 0
    for comb in combs:
        cnt = 0
        print(sum(comb))
        for w in words:
            if set(comb) & set(w) == set(w):
                cnt += 1
        result = max(result, cnt)

    return result


n, k = map(int, input().split())
print(solution(n,k))