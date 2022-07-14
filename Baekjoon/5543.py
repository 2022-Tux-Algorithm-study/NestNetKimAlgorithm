ham, bev = [], []

for i in range(3):
  ham.append(int(input()))

for i in range(2):
  bev.append(int(input()))

ham.sort()
bev.sort()

print(ham[0] + bev[0] - 50)
