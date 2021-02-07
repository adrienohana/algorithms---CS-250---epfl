import math

#read n, m and k
s = input()

line1 = list(map(int, s.split()))
if len(line1)==3:
    [n,m,k] = line1
else:
    print('Wrong input, try again')

k_ = []
w_ji = []
h_ji = []

for j in range(k):
    s = input()
    line = list(map(int, s.split()))
    k_.append(line[0])
    rest = line[1:]
    wj, hj = rest[0::2], rest[1::2]
    w_ji.append(wj)
    h_ji.append(hj)
    
k_, w_ji, h_ji

c = [[0 for l in range(m+1)]for i in range(n+1)]

def knapsack():
    for j in range(0,k):
        for i in range(1,k_[j]+1):
            if j != 0:
                sum_ = 0
                for h in range(j):
                    sum_ = sum_ + k_[h]
                index = i + sum_
            else:
                index = i
            for l in range(0,m+1):
                if l == 0:
                    c[index][l]  = 0
                elif w_ji[j][i-1] <= l:
                    c[index][l] = max(c[index-1][l],c[index-i][l-w_ji[j][i-1]]+h_ji[j][i-1])
                else:
                    c[index][l] = c[index-1][l]
knapsack()
print(str(c[n][m]) + "\\n")
