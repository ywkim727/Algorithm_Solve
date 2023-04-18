#Single-Linked_list로 Queue 구현 예제
import sys
class Node() :
    def __init__ (self, data) :
        self.data = data
        self.Next = None

class Queue() :
    def __init__ (self) :
        self.f = None
        self.r = None
        self.num = 0

    def push(self, x:int) :
        temp = Node(x)
        if not self.f :
            self.f = self.r = temp
        else :
            self.r.Next = temp
            self.r = temp
        self.num += 1

    def pop(self) :
        if self.num == 0 :
            print(-1)
            return
        print(self.f.data)
        temp = self.f
        self.f = temp.Next
        self.num -= 1

    def size(self) :
        print(self.num)

    def empty(self) :
        if self.num == 0 :
            print(1)
        else :
            print(0)

    def front(self) :
        if self.num == 0 :
            print(-1)
            return
        print(self.f.data)

    def back(self) :
        if self.num == 0 :
            print(-1)
            return
        print(self.r.data)
        
queue = Queue()


case = {
    "pop" : lambda queue : queue.pop(),
    "size" : lambda queue : queue.size(),
    "empty" : lambda queue : queue.empty(),
    "front" : lambda queue : queue.front(),
    "back" : lambda queue : queue.back()
    }
    
n = int(sys.stdin.readline())
for _ in range(n):
    # 명령 수가 많아서 sys로 받음
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        queue.push(int(command[1]))
    else:
        case[command[0]](queue)
 
