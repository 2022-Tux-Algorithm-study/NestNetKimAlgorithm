h, m = map(int, input().split())
time = int(input())

sum_h = (time+m)//60

fin_m = (time+m)%60
fin_h = (h + sum_h)%24

print(fin_h, fin_m)

