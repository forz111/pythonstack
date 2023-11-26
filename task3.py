def find_numbers(x):
    result = []
    k = 0
    while 3 ** k <= x:
        l = 0
        while 3 ** k * 5 ** l <= x:
            m = 0
            while 3 ** k * 5 ** l * 7 ** m <= x:
                result.append(3 ** k * 5 ** l * 7 ** m)
                m += 1
            l += 1
        k += 1
    return sorted(result)


x = 80
print(find_numbers(x))
