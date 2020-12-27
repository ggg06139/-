def partition(alist):
    new_list = alist
    pivot = new_list[0]
    new = 0
    for i in range(1,len(new_list)-1):
        for j in range(len(new_list)-1,0,-1):
                if i < j and new_list[i]>pivot and new_list[j]<pivot:
                    new_list[i],new_list[j] = new_list[j],new_list[i]
                    new = i
    new_list[0],new_list[new] = new_list[new],new_list[0]
    return new_list

org_list = [ int(x) for x in input('임의의 정수를 입력하시오 : ').split() ]
print('org_list =',org_list)

part_list = partition(org_list)
print('part_list =',part_list)
