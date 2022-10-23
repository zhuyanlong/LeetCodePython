# 两个堆，这种写法时间复杂度很高
# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.minstack=[]
#         self.bigstack=[]

#     def addNum(self, num: int) -> None:
#         if len(self.minstack)==0:
#             self.minstack.append(num)
#         else:
#             if num>self.minstack[-1]:
#                 while len(self.bigstack)!=0 and num>self.bigstack[-1]:
#                     self.minstack.append(self.bigstack.pop())
#                 self.bigstack.append(num)
#             else:
#                 while len(self.minstack)!=0 and num<self.minstack[-1]:
#                     self.bigstack.append(self.minstack.pop())
#                 self.minstack.append(num)
#             while True:
#                 if len(self.bigstack)==len(self.minstack):
#                     break
#                 if len(self.bigstack)+1==len(self.minstack):
#                     break
#                 if len(self.bigstack)>len(self.minstack):
#                     self.minstack.append(self.bigstack.pop())
#                 else:
#                     self.bigstack.append(self.minstack.pop())

#     def findMedian(self) -> float:
#         if len(self.bigstack)==len(self.minstack):
#             return (self.bigstack[-1]+self.minstack[-1])/2
#         else:
#             return self.minstack[-1]

    # def printStack(self):
    #     print(self.minstack)
    #     print(self.bigstack)

# 排序
# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.nums=[]

#     def addNum(self, num: int) -> None:
#         self.nums.append(num)
#         self.nums.sort()

#     def findMedian(self) -> float:
#         length=len(self.nums)
#         if length%2!=0:
#             return self.nums[length//2]
#         else:
#             return (self.nums[length//2]+self.nums[length//2-1])/2

# 两个优先权队列，因为实际上我们只需要知道最中间那两个数的相对顺序就可以，其他的数顺序是什么样的，并不重要
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small=PriQueue()
        self.large=PriQueue()

    def addNum(self, num: int) -> None:
        self.small.push(num)
        self.large.push(-self.small.pop())
        if self.small.len()<self.large.len():
            self.small.push(-self.large.pop())

    def findMedian(self) -> float:
        if self.small.len()==self.large.len():
            # print(self.small.top())
            return (self.small.top()-self.large.top())*0.5
        else:
            return self.small.top()

    def print(self):
        self.small.print()
        self.large.print()

# 自己定义一个优先队列，实现功能，想一下应该实现的是一个大根堆
class PriQueue:
    def __init__(self):
        self.queue=[]
    def push(self,num):
        # print(num)
        self.queue.append(num)
        self.swim()

# pop元素之后，必须恢复堆有序
    def pop(self):
        self.queue[0],self.queue[-1]=self.queue[-1],self.queue[0]
        tmp=self.queue.pop()
        self.sink()
        return tmp

# 堆的这两个算法真的是经常写，经常写错，要记住这种形式才可以
    def swim(self):
        i=len(self.queue)-1
        while self.queue[i]>self.queue[(i-1)//2]:
            self.queue[i],self.queue[(i-1)//2]=self.queue[(i-1)//2],self.queue[i]
            if (i-1)//2==0:
                break
            i=(i-1)//2

    def sink(self):
        i=0
        while 2*i+1<len(self.queue):
            j=2*i+1
            if j+1<len(self.queue):
                if self.queue[j]<self.queue[j+1]:
                    j=j+1
            if self.queue[i]>self.queue[j]:
                break
            self.queue[i],self.queue[j]=self.queue[j],self.queue[i]
            i=j


    def len(self):
        return len(self.queue)

    def top(self):
        return self.queue[0]

    def print(self):
        print(self.queue)

def main():
    m=MedianFinder()
    m.addNum(1)
    m.addNum(2)
    m.addNum(3)
    m.addNum(4)
    # m.addNum(5)
    # m.addNum(6)
    # m.addNum(7)
    # m.addNum(8)
    # m.addNum(9)
    # m.addNum(10)
    # m.print()
    print(m.findMedian())
    # q=PriQueue()
    # q.push(3)
    # q.push(2)
    # q.push(1)
    # q.push(4)
    # q.push(5)
    # q.push(0)
    # q.print()
    # q.pop()
    # q.pop()
    # q.print()

main()
