def mean_of_n(nums):
    return round(sum(iNums) / len(iNums),1)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

sNums = input('정수를 여러 개 입력하시오 :').split()
iNums = []
for i in sNums:
    iNums.append(int(i))

print('평균값은',mean_of_n(iNums))
print('최댓값은',max_of_n(iNums))
print('최솟값은',min_of_n(iNums))
