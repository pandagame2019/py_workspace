import os
from win32com.client import DispatchEx
from win32com.client import Dispatch,constants,gencache
from PyPDF2 import PdfFileReader
import pythoncom
totalPages=0
returnlist=[]

def wordtopdf(filelist,targetpath):
    '''j将word文档转换成pdf文件'''

    valuelist=[]
    try:
        pythoncom.CoInitialize()
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}',0,8,4)
        w=Dispatch('Word.Application')
        for fullfilename in filelist:
            temp=fullfilename.split('\\')
            path=temp[0]
            softfilename=os.path.splitext(temp[1])
            filename=temp[1]
            os.chdir(path)
            doc=os.path.abspath(filename)
            os.chdir(targetpath)
            pdfname=softfilename[0]+'.pdf'
            output=os.path.abspath(pdfname)
            pdf_name=output
            try:
                doc=w.Documents.Open(doc,readOnly=1)
                doc.ExportAsFixedFormat(output,constants.wdExportFormatPDF,Item=constants.wdExportDocumentWithMarkup,
                                        CreateBookmarks=constants.wdExportCreateHeadingBookmarks)

            except Exception as e:
                print(e)
            if os.path.isfile(pdf_name):
                valuelist.append(pdf_name)
            else:
                print('转换失败')
                return False
        w.Quit(constants.wdDoNotSaveChanges)
        return valuelist


    except TypeError as e:
        print('出错了')
        print(e)
        return -1

def getPdfPageNum(path):
    '''统计页码'''
    with open(path,'rb') as file:
        doc=PdfFileReader(file)
        pagecount=doc.getNumPages()
    return pagecount

def wordtopdf1(filelist):
    '''将每个word文档转换成一个对应的pdf文件，并统计每个文档的页码'''
    totalPages=0
    valuelist=[]
    try:
        pythoncom.CoInitialize()
        gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}',0,8,4)
        w=Dispatch('Word.Application')
        for fullfilename in filelist:
            temp=fullfilename.split('\\')
            path=temp[0]
            filename=temp[1]
            os.chdir(path)
            doc=os.path.abspath(filename)
            filename.ext=os.path.splitext(doc)
            output=filename+'.pdf'
            a=os.path.join(path,'pdf')
            pdf_name=output

            try:
                doc=w.Documents.Open(doc,readOnly=1)
                doc.ExportAsFixedFormat(output,constants.wdExportFormatPDF,Item=constants.wdExportDocumentWithMarkup,
                                        CreateBookmarks=constants.wdExportCreateHeadingBookmarks)

            except Exception as e:
                print(e)
            if os.path.isfile(pdf_name):
                pages=getPdfPageNum(pdf_name)
                valuelist.append([fullfilename.str(pages)])
                totalPages += pages
                os.remove(pdf_name)
            else:
                print('转换失败')
                return totalPages,valuelist
        w.Quit(constants.wdDoNotSaveChanges)


    except TypeError as e:
        print('出错了')
        print(e)
        return -1






def getOutline(obj,isList):
    '''递归获取文档大纲'''
    global returnlist
    for o in obj:
        if type(0)._name__=='Destination':
            if isList:
                returnlist.append(o.get('/Title')+'\t\t'+str(o.get('/Page')+1)+'\n')
            else:
                returnlist.append(o.get('/Title')+'\n')
        elif type(o).__name__=='list':
            getOutline(o,isList)
    return returnlist



def getPdfOutlines(pdfpath,listpath,isList):
    '''获取pdf文档的大纲'''
    with open(pdfpath,'rb') as file:
        doc=PdfFileReader(file)
        outlines=doc.getOutlines()
        global returnlist
        returnList=[]
        mylist=getOutline(outlines,isList)
        w=DispatchEx('Word.Application')
        w.Visible=1
        w.DisplayAlerts=0
        doc1=w.Documents.Add()
        range1=doc1.Range(0,0)
        for item in mylist:
            range1.InsertAfter(item)
        outpath=os.path.join(listpath,'list.docx')
        doc1.SaveAs(outpath)
        doc1.close()
        w.Quit()
    return outpath




















