# a = [1,1,2,3,1]
# b = [1,2,1,1,2,4]
# c = [1,1,2,1,2,3]
#
#
# def arrarCheck(nums):
#     for i in range(len(nums)-2):
#         if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
#             return True
#     return False
# result = arrarCheck(c)
# print (result)




# a = 'Hello'
# b = 'Hi'
# c = 'Heeololeo'
#
# def stringBits(str):
#     result = ""
#     for i in range(len(str)):
#         if i % 2 == 0:
#             result = result+str[i]
#     return result
#
# result = stringBits(c)
# print(result)

# def end_other(a,b):
#     a = a.lower()
#     b = b.lower()
# return a[-(len(b)):] == b or a == b[-(len(a)):]


# a = 1
# b = 14
# c = 3
#
# def no_teen_sum(a,b,c):
#     return fix_teen(a)+fix_teen(b)+fix_teen(c)
#
# def fix_teen(n):
#     if n in [13,14,17,18,19]:
#         return 0
#     return n
#
# result = no_teen_sum(a,b,c)
# print(result)

# a = [2,2,1,3,4,5]
# b = [1,2,5,6,2,11]
# c = [2,6,77,34,2,11]
#
# def count_evens(nums):
#     count = 0
#     for element in nums:
#         if element%2 == 0:
#             count += 1
#     return count
# 
# result = count_evens(a)
# print (result)
