import json
import requests


def main():
    """ 
    r 读取 （默认）
    w 写入（会先截断之前的内容）
    x 写入，如果文件已经存在会产生异常
    a 追加，将内容写入到已有文件的末尾
    b 二进制模式
    t 文本模式（默认）
    + 更新（既可以读又可以写）
    """

    f = open("./d6.py", "r", encoding="utf-8")
    # with open("./d6.py", "r", encoding="utf-8") as f:
    # 通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
    try:
        f.read()
    except FileNotFoundError:
        print("无法打开指定文件")
    except LookupError:
        print("指定了未知的编码")
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        f.close()

    f2 = open("../file/test.txt", "w", encoding="utf-8")

    json.dump({
        "name": "jojo",
        "age": 24,
        "tags": ["youngman", 13]
    }, f2)

    f2.close()

    resp = requests.get("https://api.500px.com/v1/photos?feature=popular")
    html = open("../file/photos.json", "w", encoding="utf-8")
    html.write(resp.text)


if __name__ == "__main__":
    main()
