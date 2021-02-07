{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue117;\red235\green236\blue237;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c53333;\cssrgb\c93725\c94118\c94510;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{none\}.}{\leveltext\leveltemplateid1\'01.;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl300\partightenfactor0
\ls1\ilvl0
\f0\b\fs26\fsmilli13200 \cf2 \cb3 import math\
\
#read n, m and k\
s = input()\
\
line1 = list(map(int, s.split()))\
if len(line1)==3:\
    [n,m,k] = line1\
else:\
    print('Wrong input, try again')\
\
k_ = []\
w_ji = []\
h_ji = []\
\
for j in range(k):\
    s = input()\
    line = list(map(int, s.split()))\
    k_.append(line[0])\
    rest = line[1:]\
    wj, hj = rest[0::2], rest[1::2]\
    w_ji.append(wj)\
    h_ji.append(hj)\
    \
k_, w_ji, h_ji\
\
c = [[0 for l in range(m+1)]for i in range(n+1)]\
\
def knapsack():\
    for j in range(0,k):\
        for i in range(1,k_[j]+1):\
            if j != 0:\
                sum_ = 0\
                for h in range(j):\
                    sum_ = sum_ + k_[h]\
                index = i + sum_\
            else:\
                index = i\
            for l in range(0,m+1):\
                if l == 0:\
                    c[index][l]  = 0\
                elif w_ji[j][i-1] <= l:\
                    c[index][l] = max(c[index-1][l],c[index-i][l-w_ji[j][i-1]]+h_ji[j][i-1])\
                else:\
                    c[index][l] = c[index-1][l]\
knapsack()\
print(str(c[n][m]) + "\\n")\
\
}