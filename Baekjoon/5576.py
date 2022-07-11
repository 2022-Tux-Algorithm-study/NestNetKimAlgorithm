stu = 10
w = [int(input()) for _ in range(stu)]
k = [int(input()) for _ in range(stu)]

w.sort(reverse=True)
k.sort(reverse=True)

w_score = w[0] + w[1] + w[2]
k_score = k[0] + k[1] + k[2]

print(w_score, k_score)
