class Solution:
    def fib(self, n: int) -> int:
        prevfib = 0
        currfib = 1
        position = 1

        if n == 0:return 0
        if n ==1 :return 1

        while position < n:
            currfib,prevfib = currfib+ prevfib, currfib
            position += 1

        return currfib
    
obj = Solution()
print(obj.fib(2))
    