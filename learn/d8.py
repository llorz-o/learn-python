import re


def main():
    username = str(input("请输入用户名:"))
    qq = str(input("请输入qq号码:"))

    if not re.match(r'[A-z0-9_]{6,20}', username):
        print("用户名无效")

    if not re.match(r'[1-9][0-9]{4,11}', qq):
        print("qq号码无效")


if __name__ == '__main__':
    main()
