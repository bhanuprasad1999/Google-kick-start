t = int(input())
even = []
evenindex = []
odd = []
oddindex = []
new_array = []z
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split(' ')]
    for i in range(len(a)):
        if a[i]%2 == 0:
            even.append(a[i])
            evenindex.append(i)
        else:
            odd.append(a[i])
            oddindex.append(i)
    even.sort()
    odd.sort()
    even = even[::-1]

    j = 0
    k = 0
    for i in range(len(a)):
        if a[i]%2 == 0:
            a[i] = even[j]
            j += 1
        else:
            a[i] = odd[k]
            k += 1
    print(f"Case #{_+1}: {a}")
    print('hello world')
