
# 打印如下所示的三角形图案。
for v in range(9):
    out_str = ""
    for _ in range(v):
        out_str += "*"
    print(out_str)

# 输出乘法口诀表(九九表)
for i in range(1, 10):
    for j in range(i, 10):
        print(f"{i}x{j}={i*j}")

# 用for循环实现1~100之间的偶数求和
begin = 0
for i in range(100):
    if i % 2 == 0:
        begin += i
print(begin)

# 练习3：输入三条边长，如果能构成三角形就计算周长和面积。

a = int(input("line a:"))
b = int(input("line b:"))
c = int(input("line c:"))

if a + b > c and a + c > b and b + c > a:
    p = (a+b+c)/2
    area = (p * ((p-a) + (p-b) + (p-c))) ** 0.5  # 0.5 次方
    print(f"the triangle area:{area:.2f}")
else:
    print("not a triangle")
