def hash_lists(n,m):
    hash_lists = [0]*11         #Creates a list of 11 zeros: [0,0,0,...,0].
    for num in n:               #For each num, increments the count at index num in hash_lists.
        hash_lists[num]+=1
    
    for num in m:
        if num < 1 or num > 10:
            print(0)
        else:
            print(hash_lists[num])
        return hash_lists
        
n = [1, 2, 2, 3, 10, 10, 5]
m = [2, 10, 11, 0, 5]
print(hash_lists(n, m))