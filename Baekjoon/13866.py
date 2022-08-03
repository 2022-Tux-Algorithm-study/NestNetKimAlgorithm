# 팀 나누기

skill = list(map(int, input().split()))
skill.sort()
a = skill[0] + skill[3]
b = skill[1] + skill[2]

print(abs(a-b))