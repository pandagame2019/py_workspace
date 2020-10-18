import re
import os
filename='students.txt'
def menu():
    '''输出的菜单'''
    print('''
    ----------学生信息管理系统-----------
    ==============功能菜单===============
    |  1、录入学生信息                  |
    |  2、查找学生信息                  |
    |  3、删除学生信息                  |
    |  4、修改学生信息                  |
    |  5、排序                          |
    |  6、统计学生总人数                |
    |  7、显示所有的学生信息            |
    |  0、退出                          |
    ------------------------------------
    tip:可通过数字或者上下键选择
    ''')

def save(student):
    '''将学生信息保存到文件'''
    try:
        student_txt=open(filename,'a',encoding='utf-8') #以追加的模式打开
    except:
        student_txt=open(filename,'w',encoding='utf-8')
    for info in student:
        student_txt.write(str(info)+'\n')
    student_txt.close()

def insert():
    '''录入并保存学生信息'''
    studentList=[]
    mark=True
    while mark:
        id=input('请输入学生的id （例如1001）：')
        if not id :
            break
        name=input('请输入学生的姓名：')
        if not name :
            break
        try:
            english=int(input('请输入英语成绩：'))
            python=int(input('请输入python成绩：'))
            c=int(input('请输入c语言成绩：'))
        except Exception as e :
            print('输入的无效，请重新输入！')
            continue
        student={'id':id,'name':name,'English':english,'Python':python,'C语言':c}
        studentList.append(student)
        inputMark=input('是否继续添加（y/n）：')
        if inputMark=='n' or inputMark=='N':
            mark=False
        elif inputMark=='y'or inputMark=='Y':
            mark=True
        else:
            print('输入错误，默认为继续y/Y')
    save(studentList)

def show_student(studentList):
    '''显示信息的格式'''
    if not studentList :
        print('无数据')
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}'
    print(format_title.format('ID','名字','英语成绩','Python成绩','C语言成绩','总成绩'))
    format_data='{:^6}\t{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}'
    for info in studentList :
        print(format_data.format(
            info.get('id'),info.get('name'),str(info.get('English')),str(info.get('Python')),str(info.get('C语言')),
            str(info.get('English')+info.get('Python')+ info.get('C语言')).center(12)

        ))
def show():
    '''显示全部学生信息'''
    studen_new=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as obj:
            student_old=obj.readlines()
        for info in student_old:
            studen_new.append(eval(info))
        if  studen_new:
            show_student(studen_new)
    else:
        print('文件不存在，无学生信息！')

def delete():
    '''根据学生id删除学生信息'''
    mark=True
    while mark:
        studentId=input('请输入要删除的学生id：')
        if studentId is not '':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as obj:
                    student_old=obj.readlines()
            else:
                student_old=[]
            ifdel=False
            if student_old:
                d={}
                with open(filename,'w',encoding='utf-8') as obj1:
                    for info in student_old:
                        d=dict(eval((info)))
                        if d['id']!=studentId:
                            obj1.write(str(d)+'\n')
                        else:
                            ifdel=True
                    if ifdel:
                        print(f'{studentId}的信息已被删除！')
                    else:
                        print('无该id的学生信息！')
            else:
                print('文件中无学生信息！')
            show()
            inputMark=input('是否继续删除！（y/n）:')
            if inputMark=='n' or inputMark=='N' :
                mark=False
            elif inputMark=='Y' or inputMark=='y':
                mark=True
            else:
                print('输入错误，默认为继续Y!')




def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as obj2:
            student_old=obj2.readlines()
    else:
        return
    studentId=input('请输入要修改的学生id：')
    with open(filename,'w',encoding='utf-8') as obj3:
        for info in student_old:
            d=dict(eval(info))
            if d['id']==studentId:
                print(f'已找到学生id为{studentId}的信息,可以做如下修改！')
                while True:
                    try:
                        d['name']=input('请输入姓名：')
                        d['English']=int(input('请输入英语成绩:'))
                        d['Python']=int(input('请输入python成绩：'))
                        d['C语言']=int(input('请输入c语言成绩:'));
                    except Exception as e:
                        print('输入有误，请重新输入！')
                    else:
                        break

                info=str(d)
                obj3.write(info+'\n')
                print('修改成功！')
            else:
                obj3.write(info)
    mark=input('是否继续修改！（y/n）:')
    if mark=='Y'or mark=='y':
        modify()
    else:
        print('本次修改结束！')



def search():
    mark=True
    student_query=[]
    while mark:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按id查输入1，按姓名查输入2：')
            if mode=='1':
                id=input('请输入id：')
            elif mode=='2':
                name=input('请输入姓名：')
            else:
                print('输入有误，请重新输入！')
                continue
            with open (filename,'r',encoding='utf-8') as robj:
                student=robj.readlines()
            for info in student:
                d=dict(eval(info))
                if id is not '':
                    if d['id']==id:
                        student_query.append(d)
                if name is not '':
                    if d['name']==name:
                        student_query.append(d)
            show_student(student_query)
            student_query.clear()
            inputMark=input('是否继续查询，y/n:')
            if inputMark=='y'or inputMark=='Y':
                mark=True
            elif inputMark=='n'or inputMark=='N':
                mark=False
            else:
                print('输入错误，默认为继续Y!')
        else:
            print('无学生信息！')


def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as file:
            student=file.readlines()
        if student:
            print('共有%d名学生'%(len(student)))
        else:
            print('还未录入学生！')
    else:
        print('无学生信息！')

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as file:
            student_old=file.readlines()
        student_new=[]
        for info in student_old:
            d=dict(eval(info))
            student_new.append(d)
    else:
        return
    ascORdesc=input('请选择：（0 升序；1 降序）：')
    if ascORdesc=='0':
        ascORdescbool=False
    elif ascORdesc=='1':
        ascORdescbool=True
    else:
        print('输入错误!')
        sort()
    mode=input('请选择排列的方式：（1-English；2-python；3-C语言）：')
    if mode=='1':
        student_new.sort(key=lambda x:x['English'],reverse=ascORdescbool)
    elif mode=='2':
        student_new.sort(key=lambda x: x['Python'], reverse=ascORdescbool)
    elif mode=='3':
        student_new.sort(key=lambda x: x['C语言'], reverse=ascORdescbool)
    else:
        print('输入错误!')
        sort()
    show_student(student_new)
        


def main():
    crtl=True
    while (crtl):
        menu()
        option=input('请选择：')
        option_str=re.sub('\D','',option)
        if option_str in ['0','1','2','3','4','5','6','7']:
            option_int=int(option_str)
            if option_int==0 :
                crtl=False
                print('退出')
                break
            elif option_int==1:
                print('录入学生信息')
                insert()
            elif option_int==2:
                print('查找学生信息')
                search()
            elif option_int==3:
                print('删除学生信息 ')
                delete()
            elif option_int==4:
                print('修改学生信息')
                modify()
            elif option_int==5:
                print('排序')
                sort()
            elif option_int==6:
                print('统计学生总人数')
                total()
            elif option_int==7:
                print('显示所有的学生信息 ')
                show()
        else:
            print('输入选择有误，请重新输入！')


if __name__=='__main__':
    # menu()
    main()
    # stu=[1,2,3,4,5]
    # save(stu)
    # insert()
    # dicts=[{'id': '1001', 'name': '刘东名', 'English': 100, 'Python': 100, 'C语言': 100},
    #        {'id': '1002', 'name': '史盼迪', 'English': 100, 'Python': 100, 'C语言': 100}]
    # show_student(dicts)
    # modify()

    # search()
    # total()
    # sort()


