# from heapq import heappush, heapify
N = int(input())
me = int(input())
count = 0
heap = []
if(N == 1) :
    print(0)
else :
    for _ in range(N-1) :
        a = int(input())
        # heappush(heap, a)
        heap.append(a)
        heap.sort(reverse=True)
    while(1) :
        if me <= heap[0] :
            me += 1
            count += 1
            heap[0] -= 1
            # heapify(heap)
            heap.sort(reverse=True)
        else :
            break

    print(count)