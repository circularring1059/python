def int_reverse(arg):
    #判断是否整数
    if isinstance(arg, int):
        # 判断正整数和零  or 负整数

        str_arg = str(arg)
        sign = 1 if arg >=0 else -1

        re_str_arg = str_arg[::-1] if arg >=0 else str_arg[:0:-1]
        return sign * int(re_str_arg)
    else:
        print("type error not a int")

print(int_reverse(-12000))
