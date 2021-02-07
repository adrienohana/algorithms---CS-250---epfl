import math

#read n, m and k
s = input()

line1 = list(map(int, s.split()))
if len(line1)==1:
    [n] = line1
else:
    print('Wrong input, try again')
    
a_i = []
b_i = []
h_ji = []

#read line 2
s = input()
line2 = list(map(int, s.split()))
#read line 3
s = input()
line3 = list(map(int, s.split()))
for i in range(n):
    a_i.append(line2[i])
    b_i.append(line3[i])
a_i, b_i

sorted_ids = sorted(range(len(a_i)),key=a_i.__getitem__)

a_sorted = [a_i[i] for i in sorted_ids]
b_sorted = [b_i[i] for i in sorted_ids]

def merge_sort_inversions(A):
    n = len(A)
    if n > 1:
        q = math.floor(n/2)
        L = A[:q]
        R = A[q:]
        inversions_l,sorted_left = merge_sort_inversions(L)
        inversions_r,sorted_right = merge_sort_inversions(R)
        i = 0
        j = 0
        A = []
        inversions = inversions_l + inversions_r
        while(i<len(sorted_left) and j<len(sorted_right)):
            if sorted_left[i]<=sorted_right[j]:
                A.append(sorted_left[i])
                i= i+1
            else:
                A.append(sorted_right[j])
                j= j+1
                inversions = inversions + len(sorted_left)-i
        
        A = A + sorted_left[i:] + sorted_right[j:]
        
        return inversions,A
    else: 
        return 0,A
    
inversions,_ = merge_sort_inversions(b_sorted)
            
print(str(inversions) + "\n")
