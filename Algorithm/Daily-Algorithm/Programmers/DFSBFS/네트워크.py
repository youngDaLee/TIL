def dfs(graph, start_node):
    visit = []
    stack = []

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node]) # append 와 차이점 -> 
            # ['a','b'] 넣을 때 append는 ['c','d',['a','b']] 이렇게
            # extend는 ['c','d','a','b'] 이렇게 넣음
    
    return visit

def solution(n, computers):
    # 각 컴퓨터 인덱스 번호를 key로 딕셔너리 생성. value는 빈 리스트
    graph = {node: [] for node in range(n)} 

    for i, computer in enumerate(computers):
        for j, conn in enumerate(computer):
            if i != j and conn == 1:
                graph[i].append(j)
    
    path = map(sorted, [dfs(graph, node) for node in graph]) # [2,1,4] [4,1,2]를 모두 [1,2,4]로 만들어 같은 네트워크인 지 판별

    return len(set(["".join(map(str, path)) for path in paths])) # 정렬된 모든 경로 순회하며 string으로 연결해주고 set으로 중복 제거

# https://itholic.github.io/kata-network/