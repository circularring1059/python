#calculate 为模块
from model.pkg import calculate

print(calculate.name)
calculate.show()

cal = calculate.Calculate("circularring1010")
cal.show()