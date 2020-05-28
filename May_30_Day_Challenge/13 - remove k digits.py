def removeKdigits(num, k) -> str:
    # Intuition: remove the first 'peak' digit
    stack = list()

    if len(num) == k:
        return '0'

    for i, char in enumerate(num):
        if not stack:
            stack.append(num[0])
        else:
            if char >= stack[-1]:
                stack.append(char)
            else:
                # char < stack[-1], keep popping until the peak is gone
                while stack and char < stack[-1]:
                    if k == 0:
                        break
                    k -= 1
                    stack.pop()

                stack.append(char)

    stack += list(num[i+1:])
    if k==0:
        return str(int(''.join(stack)))
    else:
        # remove top k elements of stack, while preserving order.
        # while k!=0:
        #     stack.remove(max(stack))
        #     k-=1

        ## The stack will only contain elements in increasing order, coz if local peak exists, it would have been popped earlier.
        return str(int(''.join(stack[:-k])))


print(removeKdigits("1432219", 3))
print(removeKdigits("14301620", 4))
print(removeKdigits("143012345", 4))
print(removeKdigits("1119", 4))
print(removeKdigits("1119", 1))
print(removeKdigits("10200", 1))
print(removeKdigits("10", 2))
print(removeKdigits("0", 0))
print(removeKdigits("21", 1))
print(removeKdigits("372181", 2))








def Myincorrect2hrsoln_removeKdigits(num: str, k: int) -> str:
    def no_zeros(num, k):
        indices = [1]*len(num)
        for i, digit in enumerate(num[:-1]):
            if num[i]>num[i+1]:
                indices[i] = 0
                k -=1
            
            if k==0:
                break
        
        if k == 0: 
            return ''.join([num[i] for i in range(len(num)) if indices[i]])
        else:
            # take out the k largest remaining numbers
            remaining = ''.join([num[i] for i in range(len(num)) if indices[i]])
            to_remove = sorted(remaining, reverse = True)[:k]

            indices = [1]*len(num)
            for i, digit in enumerate(remaining):
                if digit not in to_remove:
                    continue
                else:
                    indices[i] = 0
                    k-=1

                if k == 0: break

            return ''.join([remaining[i] for i in range(len(remaining)) if indices[i]])

    if len(num) == k:
        return "0"
    if '0' not in num:
        return no_zeros(num, k)
    else:
        orig = num
        while '0' in num:
            zeroloc = num.find('0') # find the left most zero
            # num = num[:zeroloc] + num[zeroloc+1:] # remove the zero

            # remove k numbers before the zero
            if k<zeroloc:
                pre_zero_string = no_zeros(num[:zeroloc], k)
                return pre_zero_string + num[zeroloc:]
            else:
                # remove all elements before that zero.
                k -= zeroloc
                num = num[zeroloc+1:]

            if k == 0:
                if num == '':
                    return '0.'
                return str(int(num))
        
        if k!=0:
            return no_zeros(num, k)

# print(removeKdigits('12345', 2))
# print(removeKdigits("1432219", 3))
# print(removeKdigits("1119", 1))
# print(removeKdigits("9119", 2))

# print(removeKdigits("10200", 1))
# print(removeKdigits("10", 1))
# print(removeKdigits("110099", 3))
# print(removeKdigits("120098", 2))
# print(removeKdigits("1107", 1))
