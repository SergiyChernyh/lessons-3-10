
############################ 1а

#value_str = "Foreverfree"
#print(value_str[2])

############################ 1b
# value_str = "Foreverfree"
# print(value_str[-2])

############################ 1c
# value_str = "Foreverfree"
# print(value_str[0:5])

###########################  1d
# value_str = "Foreverfree"
# print(value_str[0:-2])

###########################   1e

# value_str = "Foreverfree"
# print(value_str[::2])

###########################   1f

# value_str = "Foreverfree"
# print(value_str[1::2])

###########################   1g

# value_str = "Foreverfree"
# print(value_str[::-1])

###########################   1h
# value_str = "Foreverfree"
# print(value_str[::-2])

###########################   1i

# value_str = "Foreverfree"
# print(len(value_str))

######################################222222222222222222222#############################

# text = "Forever free dds sdfs sef"
# result = text.count(" ") +1
# print(result)

####################################333333333333333333333333###############################

# n = 0
#
# s = input("введите строку: ")
# for a in s:
#     if s [n] =="c" and s [n+1] == "h":
#      print(n)
#      n += 1
#     else:
#      n += 1

######################################4444444444444444####################################

s = "rddhhhhhddhr"
index_1 = s.find("h")

index_2 = s.rfind("h")
str_2 = s[index_1+1:index_2]
str2_2 = str_2.replace("h","H")

str_1 =s[0:index_1+1]
str_3 = s[index_2:]
str = str_1 + str2_2 + str_3
print(str)



