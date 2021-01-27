# 水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
# 例如：$1^3 + 5^3+ 3^3=153$。

from random import randint
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100

    if num == low ** 3 + mid ** 3 + high**3:
        print(high, mid, low)

# 百钱百鸡问题。
# 说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# 翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


# 生成斐波那契数列的前20个数。
a = [1, 1, 2]
second_last = 1
last = 2
while len(a) < 20:
    a.append(second_last + last)
    temp = last
    last = second_last + last
    second_last = temp
print(a)

