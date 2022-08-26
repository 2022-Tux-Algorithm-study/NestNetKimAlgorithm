# 박사 과정

n = int(input())

for i in range(n):
  problem = input()

  if problem == 'P=NP':
    print('skipped')
    
  else:
    index = problem.index('+')
    total = int(problem[:index])+int(problem[index+1:])
    print(total)