class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sCharMap ={}
        potentialCows =""
        bulls = 0
        cows = 0

        for i in secret:
            if i not in sCharMap:
                sCharMap[i] =1
            else:
                sCharMap[i] += 1
        
        for i, v in enumerate(guess):
            if v  == secret[i]:
                bulls +=1
                sCharMap[v] -=1
                if sCharMap[v] == 0:
                    del sCharMap[v]
            elif v in sCharMap:
                if sCharMap[v] > 0:
                    potentialCows += v

        for v in potentialCows:
            if v in sCharMap:
                if sCharMap[v] > 0:
                    cows +=1
                    sCharMap[v] -=1
                    if sCharMap[v] == 0:
                        del sCharMap[v]
                        
secret = "1807"
guess = "7810"

obj= Solution()
print(obj.getHint(secret,guess))