def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        key1 = phone_book[i]
        key2 = phone_book[i+1]
        if(key1 == key2[:len(key1)]):
            answer = False
            break
    return answer


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
