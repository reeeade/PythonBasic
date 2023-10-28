num = int(input("Input number: "))
len_ = len(str(num - 1))
one = '1'
zero = '0'
for i in range(num):
    print(f'{i:<{len_}}{one + zero * i:>{num + 1}}')
