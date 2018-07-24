from abc import ABCMeta, abstractmethod

#抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

#实体
class RealSubject(Subject):
    def __init__(self,filename):
        print('读取文件%s内容'%filename)
        f = open(filename)
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

#远程代理
class ProxyA(Subject):
    def __init__(self,filename):
        self.subj =RealSubject(filename)
    def get_content(self):
        return self.subj.get_content()

#虚代理
class ProxyB(Subject):
    def __init__(self,filename):
        self.filename = filename
        self.subj = None
    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

#保护代理
class ProxyC(Subject):
    def __init__(self,filename):
        self.subj = RealSubject(filename)
    def get_content(self):
        return '???'


#客户端
filename = 'abc.txt'
username = input('>>')
if username!='alex':
    p=ProxyC(filename)
else:
    p=ProxyB(filename)

print(p.get_content())