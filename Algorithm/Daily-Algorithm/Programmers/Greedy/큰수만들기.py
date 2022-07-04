def solution(number, k):
    stack = [number[0]]

    for num in number[1:]:
        # 스택에 값이 있고, stack top이 num보다 작으며 제거해야 할 수가 남았을 때(k>0)
        while len(stack)>0 and stack[-1]<num and k>0:
            # pop해줌
            k-=1
            stack.pop()
        stack.append(num)

    # 만약 k가 남아있으면 그냥 뒷부분 삭제
    if k!= 0:
        stack = stack[:-k]
    return ''.join(stack)

number = "4177252841"
k = 4

print(solution(number,k))