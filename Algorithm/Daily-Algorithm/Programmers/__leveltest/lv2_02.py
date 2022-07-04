def solution(board, moves):
    answer = 0
    stack = []
    top = 0

    for i in moves :
        for j in range(0,len(board)):
            if(board[j][i-1] != 0):
                if(top == board[j][i-1]):
                    stack.pop()
                    top = stack[-1]
                    answer += 2
                    board[j][i-1] = 0
                    break
                else :
                    stack.append(board[j][i-1])
                    top = stack[-1]
                    board[j][i-1] = 0
                    break
        print(board)
        print(stack)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))