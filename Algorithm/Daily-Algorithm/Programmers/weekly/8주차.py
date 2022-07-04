def solution(sizes):
    answer = 0
    widths = []
    heights = []

    for size in sizes:
        if size[0]> size[1]:
            w, h = size[0], size[1]
        else:
            w, h = size[1], size[0]
        widths.append(w)
        heights.append(h)

    width = max(widths)
    height = max(heights)

    answer = width*height
    
    return answer


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))