# Testing 
def f(x):
    # If x is even, divide by two:
    if abs(x) % 2 == 0:
        return x // 2
    else: 
        return (3 * x) + 1    

def collatz(x):
    while x != 1:
        print(x, end=', ')
        x = f(x)
    print(x)

# For range 1-10000:

for number in range(1,10001):
    print(f'Collatz sequence for {number}: ', end= '')
    collatz(number)
    print()

