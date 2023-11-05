# s = "100200102"
# a = str(s)
# print(a.count("0"))
#####################################################

# z = 0
# s = 100200100
# while (s % 10 == 0):
#  s //= 10
#  z += 1
# print(z)
#####################################################################
# my_list_1 = [1, 2, 3, 4]
# my_list_2 = [5, 6, 7, 8]
# my_result = my_list_1[0::2] + my_list_2[0::2]
# print(my_result)
##################################################################
# my_list_1 = [1, 2, 3, 4]
# new_list = my_list_1[1::]
# new_list.append(my_list_1[0])
# print(new_list)
################################################################
# my_list_1 = [1, 2, 3, 4]
# pop_value = my_list_1.pop(0)
# my_list_1.append(pop_value)
# print(my_list_1)
#################################################################
# m = []
# line = "43 більше ніж 34, але менше ніж 56"
# l = line.replace(",", "").split()
# for i in l:
#  if i.isdigit():
#   m.append(int(i))
# print(sum(m))
##############################77777777777777####################
# list =[2, 4, 1, 5, 3, 9, 0, 7]
# count =0
# for i in range(len(list[1:-1])):
#     if list[i] > list[i - 1] + list[i + 1]:
#       count += 1
# print(count)


##################################888888888888888888888888#######################
# my_list =[1, 2, 3, "11", "22", 33]
# new_list=[]
# for i in my_list:
#  if isinstance(i,str):
#   new_list.append(i)
# print(new_list)
###########################999999999999999999999#################################3
# my_str = "123412341234"
# my_list=[]
# for i in my_str:
#     my_list.append(i)
# my_list = set(my_list)
# print(my_list)

# my_str = "123412341234"
# my_list = []
# my_list = set(my_str)
# print(list(my_list))
#####################################10 10 10 10 10###########################
# my_str_1 = "1122334455"
# my_str_2 = "67892550"
# my_str = []
# my_str_1 = set(my_str_1)
# my_str_2 = set(my_str_2)
# my_str =list( my_str_1.union(my_str_2))
# print(my_str)

####################################### 11 11 11 11 11####################
str1 = "aaaasdf1"
str2 = "asdfff2"
my_list = []
my_list_1 =[]
set1 = set(str1)
set2 = set(str2)
my_list = set1.intersection(set2)
for i in my_list:
    if str1.count(i)==1 and str2.count(i) ==1:
        my_list_1.append(i)
print(my_list_1)
