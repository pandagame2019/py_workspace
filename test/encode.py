import os
import tkinter.messagebox
import tkinter.filedialog
from string import digits
from tkinter import *
import time
import random


# import pystrich
# pip installpystrich -i https://pypi.tuna.tsinghua.edu.cn/simple

import qrcode

root=tkinter.Tk() # 标准图形界面接口

number='1234567890'
letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
allis='1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+'
i=0
ranstr=[]


def mainmenu():
    print('''
    *****************************************************************************
                                企业编码生成系统
    *****************************************************************************
        1、生成6位数防伪编码（123456型）
        2、生成9位系列产品数字防伪编码（123-123456型）
        3、生成25位混合产品序列号（B2R12-N7TE2-9IET2-FE350、-DW2K4型）
        4、生成含有数据分析功能的防伪编码（5A61M0583D2）
        5、智能批量生成带数据分析功能的防伪编码
        6、后续补加生成防伪码（5A61M0583D2）
        7、EAN-13条形码批量生成
        8、二维码批量输出
        9、企业粉丝防伪码抽奖
        0、退出系统
    ============================================================================
    通过数字键选择
    ============================================================================
    
    ''')


def mkdir(path):
    '''判断保存防伪码或者补充防伪码的文件是否存在，如果不存在则建立文件夹'''
    isexists=os.path.exists(path)
    if not isexists:
        os.mkdir(path)

def openfile(filename):
    '''d读取文本函数，主要读取保存产品编号和生成数量的文件mrsoft.mri，以及用户选择的已生成的编码文件'''
    f=open(filename,'r',encoding='utf-8')
    flist=f.read()
    f.close()
    return flist

def inputbox(showstr,showorder,length):
    '''输入验证判断函数，根据参数判断输入的是哪种类型，是否合法
    输入的编码的数量，编码的类型信息，这些信息有的是数字，字符串，有的需要输入固定位数的数据。
    函数实现对输入数字，字母和位数的验证
    参数：showstr :设置输入内容提示文字
          showorder:输入内容的类型 1 为数字，位数不限制 2为字母，位数由length决定 3为数字 位数由length决定
          length:内容位数 0 为不限制
s为字符串
s.isalnum() 所有字符都是数字或者字母
s.isalpha() 所有字符都是字母
s.isdigit() 所有字符都是数字
s.islower() 所有字符都是小写
s.isupper() 所有字符都是大写
s.istitle() 所有单词都是首字母大写，像标题
s.isspace() 所有字符都是空白字符、\t、\n、\r
    '''
    instr=input(showstr)
    if len(instr)!=0 :
        if showorder==1:
            if str.isdigit(instr):
                if instr==0:
                    print('输入为0，请重新输入！')
                    return '0'
                else:
                    return instr
            else:
                print('输入非法，请重新输入！')
                return '0'
        elif showorder==2:
            if str.isalpha(instr):
                if len(instr)==length:
                    return instr
                else:
                    print(f'必须输入{length}个字母，请重新输入！')
                    return '0'
            else:
                print('输入非法，请重新输入！')
                return '0'
        elif showorder==3:
            if str.isdigit(instr):
                if len(instr)==length:
                    return instr
                else:
                    print(f'必须输入{length}个数字，请重新输入！')
                    return '0'
            else:
                print('输入非法，请重新输入！')
                return '0'
    else:
        print('输入为空，请重新输入！')
        return '0'


def wfile(sstr,sfile,typeis,smsg,datapath):
    '''
    编码输出显示函数，通过屏幕输出和屏幕输出两种方式输出生成的防伪码信息
    读取已经生成的防伪编码信息，通过幕输出和屏幕输出两种方式输出生成的防伪码信息
    输出完成后，提示已经生成的防伪码数量和保存防伪码的文件存放路径
    参数：
    sstr：生成的防伪码
    sfile：保存防伪码的文件名
    typeis：是否显示 输出完成 的信息提示框 ""值时显示提示框 no时不显示提示框
    smsg 提示框显示的提示内容
    datapath：保存防伪码的路径
    python 去除如下字符串中 的所有中括号
    out=str.replace('[','').replace(']','')
    '''
    mkdir(datapath)
    datafile=datapath+'\\'+sfile
    wrlist=sstr
    file=open(datafile,'w',encoding='utf-8')# 创建文件
    pdate=''#p屏幕输出的防伪码信息
    wdata=''#保存到文本文件的防伪码信息
    for i in range(len(wrlist)):
        wdata=str(wrlist[i].replace('[','').replace(']',''))  #去掉中括号
        wdata=wdata.replace('\'','').replace('\'','')
        file.write(str(wdata))
        pdate=pdate+wdata

    file.close()
    print(wdata)
    if typeis !='no':
        tkinter.messagebox.showinfo('提示',smsg+str(len(sstr))+'\n 防伪码文件存放位置：'+datafile )
        root.withdraw()

def input_validation(insel):
    if str.isdigit(insel):
        if insel==0 :
            print('输入为0，请重新输入！')
            return 0
        else:
            return insel
    else:
        print('输入非法，请重新输入！')
        return 0

def scode1(schoice):
    '''生成6位数防伪编码（123456型）'''
    incount=inputbox('请输入要生成防伪码的数量：',1,0)
    while int(incount)==0:
        incount = inputbox('请输入要生成防伪码的数量：',1,0)
    ranstr.clear()
    for i in range(int(incount)):
        randfir=''
        for j in range(6):
            randfir=randfir+random.choice(number)
        randfir=randfir+'\n'
        ranstr.append(randfir)
    wfile(ranstr,'scode'+str(schoice)+'.txt','','已生成6位防伪编码:','codepath')


def scode2(schoice):
    '''生成9位系列产品数字防伪编码（123-123456型）'''
    ordstart=inputbox('请输入系列产品的数字起始号（3位）：',3,3)
    while  int(ordstart)==0:
        ordstart=inputbox('请输入系列产品的数字起始号（3位）:',3,3)
    ordcount=inputbox('请输入产品系列的数量:',1,0)
    while  int(ordcount)<1 or int(ordcount)>9999:
        ordcount=inputbox('请输入产品系列的数量:',1,0)
    incount=inputbox('请输入要生成的每个系列产品的防伪码数量：',1,0)
    while int(incount)==0:
        incount=inputbox('请输入要生成的每个系列产品的防伪码数量:',1,0)
    ranstr.clear()
    for i in range(int(ordcount)):
        for j in range(int(incount)):
            randfir=''
            for k in range(6):
                randfir=randfir+random.choice(number)
            ranstr.append(str(int(ordstart)+i)+randfir+'\n')
    wfile(ranstr,'scode'+str(schoice)+'.txt','','已生成9位系列产品防伪码:','codepath')


def scode3(schoice):
    '''生成25位混合产品序列号（B2R12-N7TE2-9IET2-FE350、-DW2K4型）'''
    incount=inputbox('请输入25位混合产品序列号的数量：',1,0)
    while int(incount)==0 :
        incount=inputbox('请输入25位混合产品序列号的数量：',1,0)
    ranstr.clear()
    for i in range(int(incount)):
        strone=''
        for j in range(25):
            strone=strone+random.choice(letter)
        strtwo=strone[:5]+'-'+strone[5:10]+'-'+strone[10:15]+'-'+strone[15:20]+'-'+strone[20:25]+'\n'
        ranstr.append(strtwo)
    wfile(ranstr,'scode'+str(schoice)+'.txt','','已生成25位混合产品序列号:','codepath')


def ffcode(scout,typestr,ismessage,schoice):
    '''将数据分析码随机插入到生成的6位防伪码中，3个字母的顺序不变
    参数：scout:防伪码的数量
    typestr:数据分析字符
    ismessage:在输出完成时是否显示提示信息，为no 不显示，其他为显示
    schoice:设置输出文件的文件名称
    '''
    ranstr.clear()
    for i in range(int(scout)):
        strone=typestr[0].upper()
        strtwo=typestr[1].upper()
        strthree=typestr[2].upper()
        randfir=random.sample(number,3)
        randsec=sorted(randfir)
        letterone=''
        for j in range(9):
            letterone=letterone+random.choice(number)
        sim=str(letterone[:int(randsec[0])])+strone+str(letterone[int(randsec[0]):int(randsec[1])])+strtwo+str(
            letterone[int(randsec[1]):int(randsec[2])])+strthree+str(
            letterone[int(randsec[2]):])+'\n'
        ranstr.append(sim)
    wfile(ranstr,'scode'+str(schoice)+'.txt',ismessage,'已生成含有数据分析功能的防伪编码：','codepath')


def scode4(schoice):
    '''生成含有数据分析功能的防伪编码（5A61M0583D2）'''
    incount=inputbox('请输入含有数据分析功能的防伪编码：',1,0)
    while int(incount)==0 :
        incount=inputbox('请输入含有数据分析功能的防伪编码：',1,0)
    intype=inputbox('请输入数据分析编码（3位）：',2,3)
    while len(intype)!=3 or not str.isalpha(intype):
        intype = inputbox('请输入数据分析编码（3位）：', 2, 3)
    ffcode(incount,intype,'',schoice)


def scode5(schoice):
    '''智能批量生成带数据分析功能的防伪编码
    选择保存批量生成防伪信息的文件，批量生成防伪码信息
    '''
    defalt_dir=r'codeauto.mri'#默认路径
    file_path=tkinter.filedialog.askopenfilename(filetypes=[('Text File','*mri')],title=u'请选择智能批处理文件：',
                                                 initialdir=(os.path.expanduser(defalt_dir)))
    codelist=openfile(file_path)
    codelist=codelist.split('\n')
    print(codelist)
    for i in codelist:
        codeone=i.split(',')[0]
        codetwo=i.split(',')[1]
        ffcode(codetwo,codeone,'no',schoice)


    # root.destroy() #选择完后会留下一个名为tk()的窗体 ,强制关闭会卡死问题

def scode6(schoice):
    '''补加生成防伪码（5A61M0583D2）'''
    default_dir=r'D:\myworkspace\python\py_workspace\test\codepath\scode4.txt'
    path_file=tkinter.filedialog.askopenfilename(title=u'请选择已经生成的文件：',
                                                 initialdir=(os.path.expanduser(default_dir)))
    codelist=openfile(path_file)
    codelist.split('\n')
    codelist.remove('')
    strset=codelist[0]
    remove_digits=strset.maketrans('','',digits)
    res_letter=strset.translate(remove_digits)
    nres_letter=list(res_letter)
    letterone=nres_letter[0]
    lettertwo=nres_letter[1]
    letterthress=nres_letter[2]
    nres_letter=letterone.replace('\'','').replace('\'','')+lettertwo.replace('\'','').replace('\'','')+letterthress.replace('\'','').replace('\'','')
    card=set(codelist)
    tkinter.messagebox.showinfo('提示：','之前的防伪码数量总计：'+str(len(card)))
    root.withdraw()
    incount=inputbox('请输入补充生成防伪码的数量：',1,0)
    while int(incount)==0:
        incount = inputbox('请输入补充生成防伪码的数量：', 1, 0)
    for i in range(int(incount)*2):
        randfir=random.sample(3,number)
        randesc=sorted(randfir)
        addcount=len(card)
        strone=''
        for j in range(9):
            strone=strone+random.choice(number)
        sim=strone[:int(randesc[0])]+letterone+strone[int(randesc[0]):int(randesc[1])]+lettertwo+strone[int(
            randesc[1]):int(randesc[2])]+letterthress+strone[int(randesc[2]):9]+'\n'
        card.add(sim)


        if len(card)>addcount:
            ranstr.append(sim)
            addcount = len(card)
        if len(ranstr)>int(incount):
            print(int(len(ranstr)))
            break


    wfile(ranstr,nres_letter+'ncode'+str(choice)+'.txt',nres_letter,'已步生成防伪码数量：','codeadd')


def scode7(schoice):
    '''条形码批量生成
    EAN商品条形码共计13位，从左到右
    1-3 690-695 都是中国大陆的代码
    4-7  对应的是企业码
    8-12 ：企业商品代码
    13 校验位：
        取前12 的偶数位之和c1
        取前12 的奇数位之和c2
        将偶数位之和c1 的三倍与奇数位之和c2 相加=c3
        c3 的个位数值
        10-c3 的个位数值=校验位

    '''
    mainid=inputbox('请输入EN13的国家代码（3位）：',3,3)
    while int(mainid)<1 or len(mainid)!=3:
        mainid = inputbox('请输入EN13的国家代码（3位）：', 3, 3)
    compid=input('请输入EN13的企业代码（4位）：',3,4)
    while int(compid)<1 or len(compid)!=4:
        compid = input('请输入EN13的企业代码（4位）：', 3, 4)
    incount=inputbox('请输入要生成的条形码数量：',1,0)
    while int(incount)==0:
        incount = inputbox('请输入要生成的条形码数量：', 1, 0)
    mkdir('barcode')
    for i in range(int(incount)):
        strone=''
        for j in range(5):
            strone=strone+random.choice(number)
        barcode=mainid+compid+strone
        jishu=int(barcode[1])+int(barcode[3])+int(barcode[5])+int(barcode[7])+int(barcode[9])+int(barcode[11])
        oushu=int(barcode[0])+int(barcode[2])+int(barcode[4])+int(barcode[6])+int(barcode[8])+int(barcode[10])
        checkbit= int(10-((oushu*3+jishu)%10)%10)
        barcode=barcode+checkbit
        # encoder=EAN13Encoder(barcode)
        # encoder.save('barcode\\'+barcode+'.png')

#pip install qrcode -i https://pypi.tuna.tsinghua.edu.cn/simple



def scode8(schoice):
    '''二维码批量输出

    qr = qrcode.QRCode(
    version=2, 控制二维码的大小
    error_correction=qrcode.constants.ERROR_CORRECT_L, 控制二维码的错误纠错功能
    box_size=10,控制我二维码中每个格子包含的相素
    border=1 控制边框包含的格子数 默认4
)
qr.add_data("http://jb51.net/")
qr.make(fit=True)
img = qr.make_image()
img.save("dhqme_qrcode.png")

    '''
    incount=inputbox('请输入要生成的12位二维码数量：',3,12)
    while int(incount)==0 :
        incount = inputbox('请输入要生成的12位二维码数量：', 3, 12)
    mkdir('qrcode')
    for a in range(int(incount)):
        strone=''
        for b in range(12):
            strone=strone+random.choice(number)
        encode=qrcode.make(strone)
        # strone.save('qrcode//'+strone+'.png')
        print(encode)


def scode9(schoice):
    '''企业粉丝防伪码抽奖'''
    def_dir=r'lott.ini'
    path_file=tkinter.filedialog.askopenfile(filetypes=[('INi file','*ini')],title='请选择包含抽奖号码的抽奖文件：',initialdir=(os.path.expanduser(def_dir)))
    codelist=openfile(path_file)
    codelist=codelist.split('\n')
    incount=inputbox('请输入生成的抽奖数量：',1,0)
    while int(incount)==0 or len(codelist)<int(incount):
        incount=inputbox('请输入生成的抽奖数量：',1,0)
    strone=random.sample(codelist,int(incount))
    for i in range(int(incount)):
        wdata=str(strone[i].replace('[','')).replace(']','')
        wdata = str(strone[i].replace('\'', '')).replace('\'', '')
        print(wdata)






if __name__=='__main__':
    while True:
        mainmenu()
        choice=input('请输入选择的菜单选项：')
        if len(choice)==0:
            print('输入非法，请重新输入！')
            time.sleep(2)
        elif len(choice)==1:
            choice=int(input_validation(choice))
            if choice==1:
                print('生成6位数防伪编码（123456型）')
                scode1(str(choice))
            if choice==2:
                print('生成9位系列产品数字防伪编码（123-123456型）')
                scode2(str(choice))
            if choice==3:
                print('生成25位混合产品序列号（B2R12-N7TE2-9IET2-FE350、-DW2K4型）')
                scode3(choice)
            if choice==4:
                print('生成含有数据分析功能的防伪编码（5A61M0583D2）')
                scode4(choice)
            if choice==5:
                print('智能批量生成带数据分析功能的防伪编码')
                scode5(choice)
            if choice==6:
                print('补加生成防伪码（5A61M0583D2）')
                scode6(choice)
            if choice==7:
                print('条形码批量生成')
                scode7(choice)
            if choice==8:
                print('二维码批量输出')
                scode8(choice)
            if choice==9:
                print('企业粉丝防伪码抽奖')
                scode9(choice)
            if choice==0:
                print('正在退出系统！')
                break
        else:
            print('输入非法，请重新输入！')
            time.sleep(2)






    # path='code.txt'
    # mkdir(path)
    # mainmenu()
