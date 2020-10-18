# \033[显示方式;前背景色;背景色m \033[1;37;41m
finish=False
flagNum=1
flagch='*'
x=0
y=0
print('\033[1;37;41m----简易五子棋游戏（控制台版）-----\033[0m')
#棋盘初始化
checkerboard=[]
for i in range(10):
    checkerboard.append([])
    for j in range(10):
        checkerboard[i].append('-')
while True:
    #打印棋盘
    print('\033[1;37;46m----------------------------------')
    print('   1  2  3  4  5  6  7  8  9  10')
    for i in range(len(checkerboard)):
        print(chr(i+ord('A'))+' ',end=' ')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j]+' ',end=' ')
        print()
    print('----------------------------------\033[0m')


    def msg():
        '''s输出最后胜利的棋盘'''
        print('\033[1;37;46m----------------------------------')
        print('   1  2  3  4  5  6  7  8  9  10')
        for i in range(len(checkerboard)):
            print(chr(i+ord('A'))+' ',end=' ')
            for j in range(len(checkerboard[i])):
                print(checkerboard[i][j] + ' ', end=' ')
            print()
        print('----------------------------------\033[0m')
        #输出赢家
        if (flagNum==1):
            print('\033[32m*棋胜利！***\033[0m')
        else:
            print('\033[32mo棋胜利！***\033[0m')


    # 棋子左侧

    if flagNum==1 :
        flagch='*'
        print('\033[1;37;45m 请*输入棋子坐标: \033[0m',end=' ')#粉子黑底
    else:
        flagch = 'o'
        print('\033[1;37;45m 请o输入棋子坐标: \033[0m', end=' ')#黑子绿底



    str=input()
    ch=str[0]
    x=ord(ch)-65
    y=int(str[1])-1


    #判断坐标是否在棋盘内
    if(x<0 or y<0 or x>9 or y>9):
        print('\033[31m***您输入的坐标有误请重新输入！***\033[0m')
        continue

    #判读坐标是否有棋子
    if (checkerboard[x][y])=='-':
        if (flagNum==1):
            checkerboard[x][y]='*'
        else:
            checkerboard[x][y]='o'
    else:
        print('\033[31m***您输入位置已经有其他棋子，请重新输入！***\033[0m')
        continue
    if (y-4>=0):
        if (checkerboard[x][y - 1] == flagch and
            checkerboard[x][y - 2] == flagch and
            checkerboard[x][y - 3] == flagch and
            checkerboard[x][y - 4] == flagch
        ):
            finish=True
            msg()
    # 棋子右侧
    if (y+4<=9):
        if (checkerboard[x][y + 1] == flagch and
            checkerboard[x][y + 2] == flagch and
            checkerboard[x][y + 3] == flagch and
            checkerboard[x][y + 4] == flagch
        ):
            finish=True
            msg()
    #棋子上方
    if (x-4>=0):
        if (checkerboard[x-1][y] == flagch and
            checkerboard[x-2][y] == flagch and
            checkerboard[x-3][y] == flagch and
            checkerboard[x-4][y] == flagch
        ):
            finish=True
            msg()
     #棋子下方
    if (x+4<=9):
        if (checkerboard[x+1][y] == flagch and
            checkerboard[x+2][y] == flagch and
            checkerboard[x+3][y] == flagch and
            checkerboard[x+4][y] == flagch
        ):
            finish=True
            msg()
    #棋子右上方
    if (x-4>=0 and y-4>0):
        if (
            checkerboard[x-1][y-1]==flagch and
            checkerboard[x - 2][y - 2] == flagch and
            checkerboard[x - 3][y - 3] == flagch and
            checkerboard[x - 4][y - 4] == flagch

        ):
            finish=True
            msg()
    #棋子右下方
    if (x+4<=9 and y-4>0):
        if (
            checkerboard[x+1][y-1]==flagch and
            checkerboard[x + 2][y - 2] == flagch and
            checkerboard[x + 3][y - 3] == flagch and
            checkerboard[x + 4][y - 4] == flagch

        ):
            finish=True
            msg()

    #棋子左上方
    if (x-4>=0 and y+4<=9):
        if (
            checkerboard[x+1][y+1]==flagch and
            checkerboard[x - 2][y +2 ] == flagch and
            checkerboard[x - 3][y + 3] == flagch and
            checkerboard[x - 4][y + 4] == flagch

        ):
            finish=True
            msg()
    #棋子左下方
    if (x+4<=9 and y+4<0):
        if (
            checkerboard[x+1][y+1]==flagch and
            checkerboard[x + 2][y + 2] == flagch and
            checkerboard[x + 3][y + 3] == flagch and
            checkerboard[x + 4][y + 4] == flagch

        ):
            finish=True
            msg()


    flagNum *= -1

    if finish:
        break;















