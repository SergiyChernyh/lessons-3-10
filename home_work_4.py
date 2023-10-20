############################ 1а

#value_str = "Foreverfree"
#print(value_str[2])

############################ 1b
# value_str = "Foreverfree"
# print(value_str[-1])

############################ 1c
# value_str = "Foreverfree"
# print(value_str[0:4])

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

key1 = 0
key2 = 0

s = input("введите строку: ")
if s[0] == "h":
  key1 = 1
if s[-1] == "h":
  key2 = 1
str = s.replace("h", "H")
if key1 == 1:
  result = "h" + str[1:]
  str = result
if key2 == 1:
  result = str[:-1] +"h"
  str = result
  print(str)
