target=5
arr=[1,2,3,4]

def indices(arr, target):
    seen = {}

    for i in range(len(arr)):
        num = arr[i]
        need = target - num

        if need in seen:
            return [seen[need], i]

        seen[num] = i

print (indices(arr, target))