def my_soln(num):
    return int(''.join('0' if i == '1' else '1' for i in bin(num)[2:]), 2) 

def disc_page(num):
    # left shift 1 by the length of the binary number; 1 --> 100..0;
    # Subtract 1 from this; e.g., 1000 - 1 = 111
    # Perform AND operation using ^

    mask = 1 << (len(bin(num)) - 2)
    return (mask - 1) ^ num

    # 1 line
    # return num ^ (2 ** num.bit_length()) - 1

print(my_soln(10))
print(disc_page(10))