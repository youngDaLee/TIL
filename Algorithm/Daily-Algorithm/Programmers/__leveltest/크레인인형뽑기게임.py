def solution(board, moves):
    # 테스트케이스 1,2 런타임 에러남
    answer = 0
    stack = []
    top = 0

    for i in moves:  # len(moves)만큼 반복
        for j in range(0, len(board)):  # n x n의 n만큼 반복
            if(board[j][i-1] != 0):  # 검사하려는 열의(i) 맨 윗칸(n)부터 검사, 만약 비어있지 않다면
                if(top == board[j][i-1]):  # 만약 걸리는거랑 stack top에 있는 애가 같으면
                    stack.pop()  # pop하고
                    if not stack:
                        top = 0
                    else:
                        top = stack[-1]  # top바뀜
                    answer += 2  # pop한 인형 개수 추가됨
                    board[j][i-1] = 0  # 인형뽑기 인형 뽑힘
                    break
                else:  # 비어있지 않은데 stack top이랑 다르면
                    stack.append(board[j][i-1])  # stack에 넣어줌
                    top = stack[-1]
                    board[j][i-1] = 0
                    break
        # print(board)
        # print(stack)
    return answer


# board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
#     0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
# moves = [1, 5, 3, 5, 1, 2, 1, 4]

# print(solution(board, moves))
