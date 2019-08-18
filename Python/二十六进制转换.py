from string import ascii_uppercase


def letter_to_number(s):
    # 26 to 10
    s = reversed(s.upper())
    dct = {v: k for k, v in enumerate(ascii_uppercase, start=1)}
    return sum(dct[char] * (26 ** idx) for idx, char in enumerate(s))


def number_to_letter(n):
    # 10 to 26
    lst = []
    dct = dict(enumerate(ascii_uppercase, start=1))

    while n:
        mod = n % 26
        n //= 26
        if mod == 0:
            mod = 26
            n -= 1
        lst.append(mod)

    return ''.join([dct[i] for i in reversed(lst)])


print(letter_to_number('AZ'))
print(number_to_letter(52))