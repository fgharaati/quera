n = int(input())


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True



def generate_n_digit_fibs(n):
    fiblis = []
    a = 0
    b = 1
    c = a + b
    while c < 10 ** n:
        a = b
        b = c
        c = a + b
        if len(str(b)) == n:
            fiblis.append(b)
    return fiblis


fib_numbers = generate_n_digit_fibs(n)

flag = False
for i in range(-1, (-len(fib_numbers)) - 1, -1):
    number = fib_numbers[i]

    if is_prime(number):
        flag = True
        print(number)
        break

if not flag:
    print("There isn't such a number.")