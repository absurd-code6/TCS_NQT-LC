# For Generating all prefix-substrings/subarrays
s="aab"
start=0
for i in range(start+1,len(s)+1):
    sub=s[start:i]
    print(sub)

ary=[1,2,3,4]
for i in range(start+1,len(ary)+1):
    print(ary[start:i])

#For Generating all possible substrings/subarrays
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j])

for i in range(len(ary)):
    for j in range(i+1,len(ary)+1):
        print(ary[i:j])