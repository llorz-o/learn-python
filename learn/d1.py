# 练习1：华氏温度转换为摄氏温度。
# c = (f - 32) / 1.8

c = (float(input("please input F:")) - 32) / 1.8

print(f"current temperature C:{c:.1f}")


# 练习2：输入圆的半径计算计算周长和面积。
r = float(input("please input the radius:"))
circumference = 2 * 3.1415926 * r
area = 3.1415926 * r * r

print(f"the circle circumference:{circumference:.1f}")
print(f"the circle area:{area:.1f}")

# 练习3：输入年份判断是不是闰年。
year = int(input("please input year:"))
is_leap = (year % 4) == 0 and year % 100 != 0 or\
    year % 400 == 0
if is_leap:
    leap_str = "is leap"
else:
    leap_str = "not leap"

print(f"the year:{year}", leap_str)
