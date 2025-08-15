def reverse_number(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)
number = 12345678910
print(f"Reversed number: {reverse_number(number)}")
