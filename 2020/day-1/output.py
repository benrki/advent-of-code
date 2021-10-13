f = open("input.txt", "r")

SUM = 2020
num = int(f.readline())
need = set()

while num not in need and f.readable():
    need.add(abs(num-SUM))
    num = int(f.readline())

num2 = abs(num-2020)
print("found numbers adding to", num+num2, num, num2, num*num2)
