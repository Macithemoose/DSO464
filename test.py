def solution(U, weight):
    queue = weight[:]
    removed = 0
    
    i = 0
    while i < len(queue) - 1:
        if queue[i] + queue[i + 1] > U:
            queue.pop(i + 1)
            removed += 1
        else:
            i += 1
    
    return removed

#ans = solution(2, [3,7,5,5,6,3,9,10,8,4])