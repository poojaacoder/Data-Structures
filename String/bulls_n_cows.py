class Solution:
    def getHint(self, secret: str, guess: str) -> str:


        secret_dict = [0] * 10
        guess_dict = [0] * 10
        bulls_count = 0
        cows_count = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls_count +=1
            else:
                secret_dict[int(secret[i])]+=1
                guess_dict[int(guess[i])]+=1
        
        print(secret_dict, guess_dict)
        for i in range(10):
           cows_count += min(guess_dict[i], secret_dict[i])

        return str(bulls_count)+ 'A'+str(cows_count)+'B'
        

        # https://leetcode.com/problems/bulls-and-cows/