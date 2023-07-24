def move_zeros(array):
    for i in range (0,len(array)-1):
        if array[i]==0:
            array.remove(array[i])
            array.append(0)
    return array
array=list(map(int,input().split()))
print(move_zeros(array))