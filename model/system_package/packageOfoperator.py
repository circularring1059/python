import  operator

# digit
print(operator.lt(1, 2))    #Ture
print(operator.gt(1, 2))    #False
# operator.eq(a, b)
# operator.ne(a, b)
# operator.ge(a, b)
# operator.gt(a, b)
# operator.__lt__(a, b)
# operator.__le__(a, b)
# operator.__eq__(a, b)
# operator.__ne__(a, b)
# operator.__ge__(a, b)
# operator.__gt__(a, b)

# point
a = b = 1
c = d = "^&hojg("
print(operator.is_(a, b))
print(operator.is_(c, d))

# add  sub // /
print(operator.add(2, 3))
print(operator.sub(2, 3))
print(operator.truediv(2, 3))
print(operator.mod(3, 2))   #1
print(operator.mul(3, 2))   #6


# 算术取反
print(operator.neg(3))
# 逻辑取反
print(operator.not_(False))  #True


list1 = [1, 2, 3, 4, 5]
print(operator.getitem(list1, 2))  #3

# str add
print(operator.iadd("ring", "yuan"))

# list add
list2 = [2, 3]
list3 = [4, 5]
print(operator.iadd(list2, list3))  #[2, 3, 4, 5]
print(list2, list3) #[2, 3, 4, 5] [4, 5]
