def sort_by_one_bits(arr):
    def set_bit_count(num):
        count = 0
        while num > 0:
            count += 1
            num&=num-1
        return count
    # return sorted(arr, key = lambda x: (bin(x).count('1'), x))
    # return sorted(arr, key = lambda x: (sum((x>>i) & 1 for i in range(32)), x))
    return sorted(arr, key = lambda x: (set_bit_count(x), x))





print(sort_by_one_bits([0,1,2,3,4,5,6,7,8]))