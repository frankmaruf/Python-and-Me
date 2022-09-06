def ShellSort(list):
    distance  = len(list) // 2
    while distance  > 0:
        for i in range(distance ,len(list)):
            temp = list[i]
            j = i
            while j>=distance  and list[j - distance ] > temp:
                list[j] = list[j - distance ]
                j = j-distance 
            list[j] = temp
        distance = distance//2
    return list

List = [25,21,22,24,23,27,26]
print(ShellSort(List))