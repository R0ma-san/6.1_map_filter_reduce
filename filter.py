numbers = [4, 17, 3, 90, 28, 55]

def odd(a):
    if a%2!=0:
     return a

a = list(filter(odd, numbers))

print(a)