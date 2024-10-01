n = int(input('введите число от 3 до 20: '))
while n < 3 or n > 20:
    print('Неверное число!')
    exit(n)


def password(num):
    p = ''
    for i in range(1, num):
        for k in range(2, num):
            if k <= i:
                continue
            if num % (k + i) == 0:
                p += str(i) + str(k)
    return p


result = password(n)
print(result)
