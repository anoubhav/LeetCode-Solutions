def numberOfSteps (num: int) -> int:
        
        ## soln 1
        steps = 0
        while num!=0:
            steps += 1
            if num%2 == 0:
                num //= 2
            else:
                num -= 1
        return steps

        # ## soln 2
        # b = bin(num)[2:]
        # return b.count('1') + len(b) - 1

        # ## soln 3
        # steps = 0
        # while num!=0:
        #     steps += (num & 1) + 1
        #     num >>= 1
        # return steps-1