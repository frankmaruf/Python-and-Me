def MergeSort(list):
    if len(list)>1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        MergeSort(left)
        MergeSort(right)
        a=0
        b=0
        c=0
        while a < len(left) and b < len(right):
            if left [a] < right[a]:
                list[c] = left[a]
                a = a+1
            else:
                list[c] = right[b]
                b = b+1
            c = c+1
        while a < len(left):
            list[c] = left[a]
            a = a+1
            c = c+1
        while b< len(right):
            list[c] = right[b]
            b = b+1
            c = c+1
    return list

List = [25,21,22,24,23,27,26]
MergeSort(List)