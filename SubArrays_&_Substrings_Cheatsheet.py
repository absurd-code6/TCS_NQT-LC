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



def backtrack(start, path):
    for i in range(start, len(ary)):
        # 1. Choose: add the current element to the path
        path.append(ary[i])
        
        # 2. Explore: print or process the current subset
        print(path)
        
        # 3. Recurse to build longer subsets
        backtrack(i + 1, path)
        
        # 4. Un-choose (Backtrack): remove the element to explore other paths
        path.pop()

# Example call
backtrack(0, [])
