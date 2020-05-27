def divisorGame(self, N: int) -> bool:
    # Even numbers always win.
    # Odd numbers will give back an even number to your opponent, so odd numbers always lose.
    # return not N%2


    # dp[i] should indicate the result of game of the player who starts first
    dp = [0]*(N+1)
    for num in range(2, N+1):
        for div in range(1, num//2 + 1):
            if num%div == 0 and (not dp[num - div]):
                dp[num] = 1
                break
            
    return dp[N]