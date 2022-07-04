
def solution(n, times):
    answer = 0
    total_time = 0
    time = {}
    pin = 0 #마지막으로 들어간 사람

    for i in times:
        time[i] = i
    
    n = n-len(times)

    while n:
        for key, value in time.items():
            if value == 0:
                n -= 1
                time[key] = key
                pin = key
        for key, value in time.items():
            time[key] = value-1
        total_time += 1
        
        print(time)
    
    total_time += pin
    return total_time

n = 6
times = [7,10]
print(solution(n,times))