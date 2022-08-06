# 17배

n = input()
bin = 0

for i in range(len(n)):
    bin += int(n[i]) * (2 ** (len(n) - i - 1))

bin *= 17
bin = format(bin, 'b')
print(bin)