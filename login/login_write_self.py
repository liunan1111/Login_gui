#!/usr/bin/env python
# coding=utf-8
#  ustc liunan
from Tkinter import *
import requests
import tkMessageBox
import os
from _socket import timeout

def showPw():
    str_='\\'
    pathPw=os.getcwd()+str_+'pw'+str_+'pw.txt'

    if os.path.getsize(pathPw):
        file1=open(pathPw,'r')
        lines=file1.readlines()
        for line in lines:
    #         print line,
            list=line.split()
    #     print list[0],list[1]
        e.set(list[0])
        e2.set(list[1])
        file1.close()
    else:
        f=open(pathPw,'w')
        #     f.write(e.get())
        #     global e
        #     global e2
        f.write('')
        f.write(' ')
        f.write('')
        f.close()
        
#     print pathPw

def keepPw():
    path = 'pw'
    if not os.path.exists(path):
        os.makedirs(path)
    file_path=path+'/'+'pw'+'.txt'
    f=open(file_path,'w')
#     f.write(e.get())
#     global e
#     global e2
    f.write(e.get())
    f.write(' ')
    f.write(e2.get())
    f.close()
    
def show():
    tkMessageBox.showinfo('Author', 'Author:17 mse ustc liunannan')
#     Label(root,text='author:17 mse ustc liunannan',height=10,width='200').pack()
# for item in ['版权信息']:
#     about.add_command(label=item)
def quitNet():
#     print 'quit'
#     
#     posturl='http://wlt.ustc.edu.cn/cgi-bin/ip'
#     agent='Mozilla/5.0'
#     headers={'User-Agent':agent,
#              'Accept-Encoding':'gzip, deflate',
#              'Accept-Language':'zh-CN,zh;q=0.8',
#              'Referer': 'http://wlt.ustc.edu.cn/',
#              'Cookie': 'rn=717AEC554949B1C92BDBD98172AB5A0970C01844'           
#              }
#     name=e.get()
#     pw=e2.get()
#     value={'cmd':'login',
#           'url':'URL',
#           'ip':'114.214.186.32',
#           'name':name,
#           'password':pw,
#           'go':'��¼�ʻ�'}
#     s1=requests.Session()
#     s1.post(posturl, data=value, headers=headers)
#     r1=requests.get(posturl,timeout=3)
#     print r1.status_code
    posturl='http://wlt.ustc.edu.cn/cgi-bin/ip'
    agent='Mozilla/5.0'
    headers={'User-Agent':agent,
             'Accept-Encoding':'gzip, deflate',
             'Accept-Language':'zh-CN,zh;q=0.8'}
    name=e.get()
    pw=e2.get()
    value={'cmd':'login',
          'url':'URL',
          'ip':'114.214.186.32',
          'name':name,
          'password':pw,
          'set':'һ������'}
    s=requests.Session()
    s.post(posturl, data=value, headers=headers)
    posturl='http://wlt.ustc.edu.cn/cgi-bin/ip?cmd=set&type=8&exp=0&setdefault=+%CD%CB%B3%F6%B5%C7%C2%BC+'
    value={'cmd':'set',
          'url':'URL',
          'type':'8',
          'exp':'0',
          'setdefault':' �ر����� '}
    headers2={'User-Agent':agent,
             'Accept-Encoding':'gzip, deflate',
             'Accept-Language':'zh-CN,zh;q=0.8',
             'Referer': 'http://wlt.ustc.edu.cn/cgi-bin/ip',
             'Cookie': 'rn=5072EB6B16B99A955C61B53A1881F5EF4AFA8347'       
             }
    try:
        res=requests.get('www.baidu.com',params=value,timeout=3)
        print res.status_code
#         print res.text
    except:
        tkMessageBox.showerror(u'关闭网络', u'关闭成功')
        
def connectNet():
#     print 'hello'
    
    posturl='http://wlt.ustc.edu.cn/cgi-bin/ip'
    agent='Mozilla/5.0'
    headers={'User-Agent':agent,
             'Accept-Encoding':'gzip, deflate',
             'Accept-Language':'zh-CN,zh;q=0.8'}
    name=e.get()
    pw=e2.get()
    value={'cmd':'login',
          'url':'URL',
          'ip':'114.214.186.32',
          'name':name,
          'password':pw,
          'set':'һ������'}
    s=requests.Session()

    try:
        s.post(posturl, data=value, headers=headers)
#         res=requests.get(posturl,timeout=3)
    except:
        tkMessageBox.showerror(u'正在连接网络', u'请检查本地连接是否连接上!')
#         quit()
        exit()
        
        
    try:
        r=requests.get('https://www.baidu.com',timeout=3)
#             print r.status_code
        if r.status_code==200:
                tkMessageBox.showinfo(u'正在连接网络',u'网络连接成功！')
        else:
            tkMessageBox.showerror(u'正在连接网络',u'网络出现错误！')
#             quit()           
    except:
        tkMessageBox.showerror(u'正在连接网络',u'网络连接失败！账号或密码错误！')

    keepPw()
def mainPage():
    showPw()
    label=Label(root,text=u'账号:',width='+10').grid(row=1, stick=W, pady=10)
    
    entry=Entry(root,textvariable=e)
#     e.set('sa517211')
    entry.grid(row=1, column=1, stick=E)
    label2=Label(root,text=u'密码:',width=10).grid(row=2, stick=W, pady=10)

    entry2=Entry(root,textvariable=e2)
#     e2.set('sa517211')
    entry2.grid(row=2, column=1, stick=E)
    entry2['show']='*'
    
    b=Button(root,text=u'一键上网',command=connectNet).grid(row=3, stick=W, pady=10,padx=40)
    b2=Button(root,text=u'关闭网络',command=quitNet).grid(row=3, column=1, stick=E,padx=40)

    
def menuset():
    mainpage=Menu(menubar)
    mainpage.add_command(label=u'主界面',command=mainPage)
#     menubar.add_cascade(label='主界面',menu=mainpage)
    about=Menu(menubar)
    about.add_command(label=u'版权信息', command=show)
    menubar.add_cascade(label=u'关于',menu=about)
    root['menu']=menubar
    

                 
root =Tk()
root.title(u'科大网络通连接')
root.geometry('300x180')
root.resizable(width=False, height=False)
e=StringVar()
e2=StringVar()
menubar=Menu(root)
mainPage()
menuset()
# keepPw()
# showPw()
root.mainloop()