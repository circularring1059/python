#从项目根路径下开始引包
import model.day1

print(model.day1.number)

print(model.day1.name)

print(model.day1.add(*[1,2,4,5]))

calculate = model.day1.Calculate("计算")

calculate.show()
calculate.show1()

