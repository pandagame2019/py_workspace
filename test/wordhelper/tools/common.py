import os
import re

def getfilenames(filepath='',filelist_out=[],file_ext='all'):
    '''
    获取指定目录下的文件
    filepath 要遍历的目录
    filelist_out:输出的文件列表
    file_ext：文件的扩展名，默认为任何类型的文件
    :return:
    '''
    for filename in os.listdir(filepath):
        fi_d=os.path.join(filepath,filename)
        if file_ext=='.doc':
            if os.path.splitext(fi_d)[1] in ['.doc','.docx']:
                filelist_out.append(fi_d)
            else:
                if file_ext=='all':
                    filelist_out.append(fi_d)
                elif os.path.splitext(fi_d)[1]==file_ext:
                    filelist_out.append(fi_d)
                else:
                    pass
    filelist_out.sort(key=indexSort)
    return filelist_out

def indexSort(elem):
    '''指定排列规则'''
    a=re.findall(r'第\d章',elem)
    if a==[]:
        return float('inf')# 返回一个无穷大的数，表示最大
    else:
        return int(a[0][1:-1])#返回数字（按照该数字排序）



if __name__=='__main__':
    pass








































