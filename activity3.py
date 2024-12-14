def a(n):
    b = ""
    if n == 0:
        return "0"
    while n > 0:
        r = n % 2
        b = str(r) + b
        n = n // 2
    return b
n = int(input("Enter a decimal number: "))
b = a(n)
print("The binary of",n,"is",a(n))
