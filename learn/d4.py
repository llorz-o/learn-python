# 练习1：在屏幕上显示跑马灯文字。

import os
import time
import random


def main():
    content = "北京欢迎你为你开天辟地…………"
    while True:
        os.system("cls")
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


# 设计一个函数返回传入的列表中最大和第二大的元素的值。
def get_frist_second_big_number(l):
    a = None
    b = None
    for i in l:
        if a == None:
            a = i
        elif i > a:
            a, b = i, a
        elif b == None:
            b = i
    return a, b


# 打印出杨辉三角
"""
　　　　　　　　１
　　　　　　　１　１
　　　　　　１　２　１
　　　　　１　３　３　１
　　　　１　４　６　４　１
　　　１　５　10　10　５　１
　　１　６　15　20　15　６　１
　１　７　21　35　35　21　７　１
１　８　28　56　70　56　28　８　１
"""


def print_yanghui_triangle(l):
    rc = [[]] * l
    for row_i in range(len(rc)):
        rc[row_i] = [None] * (row_i + 1)
        for col_i in range(len(rc[row_i])):
            if col_i == 0 or col_i == row_i:
                rc[row_i][col_i] = 1
            else:
                rc[row_i][col_i] = rc[row_i-1][col_i - 1] + rc[row_i - 1][col_i]

    for row in rc:
        print(row)


# 随机选择六合彩号码
def get_liuhe():
    all_ball = [x for x in range(1, 50)]
    re = random.sample(all_ball, 7)
    print(re)

# 有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
# 有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
# 他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
# 由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒


def joseph_circle():
    circle = [True] * 30
    count = 0
    index = 0
    number = 0
    while count < 15:
        if circle[index]:
            number += 1
            if number == 9:
                circle[index] = False
                count += 1
                number = 0
        index += 1
        index %= 30
    print(circle)

# 井字棋游戏


def geme_jing():

    board = {
        "0": "0", "1": "1", "2": "2",
        "3": "3", "4": "4", "5": "5",
        "6": "6", "7": "7", "8": "8"
    }

    def format_print(board, reference=board):
        print(board['0'] + "|" + board['1'] + "|" + board['2'],
              reference['0'] + "|" + reference['1'] + "|" + reference['2'])
        print("-----")
        print(board['3'] + "|" + board['4'] + "|" + board['5'],
              reference['3'] + "|" + reference['4'] + "|" + reference['5'])
        print("-----")
        print(board['6'] + "|" + board['7'] + "|" + board['8'],
              reference['6'] + "|" + reference['7'] + "|" + reference['8'])

    turn = "x"
    begin = True
    counter = 0
    while begin:
        cur_board = board.copy()

        for k in cur_board:
            cur_board[k] = ' '

        while counter < 9:

            format_print(cur_board)

            pos = str(input(f"当前{turn}执子 请输入位置:"))

            if cur_board.get(pos, False) and cur_board[pos] == ' ':
                cur_board[pos] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            else:
                print("当前位已落子")

            os.system('cls')

        continue_game = input("是否继续:(yes|no)")
        if continue_game == "yes":
            counter = 0
        else:
            begin = False


if __name__ == "__main__":
    geme_jing()
