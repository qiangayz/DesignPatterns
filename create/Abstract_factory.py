from abc import abstractmethod, ABCMeta

# ------抽象产品------
class PhoneShell(metaclass=ABCMeta):

    @abstractmethod
    def show_shell(self):
        pass

class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

# ------抽象工厂------
class PhoneFactory(metaclass=ABCMeta):

    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

# ------具体产品------
class SmallShell(PhoneShell):
    def show_shell(self):
        print('小手机壳')

class BigShell(PhoneShell):
    def show_shell(self):
        print('大手机壳')

class AppleShell(PhoneShell):
    def show_shell(self):
        print('苹果机壳')

class SnapDragonCPU(CPU):
    def show_cpu(self):
        print('骁龙CPU')

class MediaTekCPU(CPU):
    def show_cpu(self):
        print('联发科CPU')

class AppleCPU(CPU):
    def show_cpu(self):
        print('苹果CPU')

class Andriod(OS):
    def show_os(self):
        print('安卓系统')

class IOS(OS):
    def show_os(self):
        print('iOS系统')

# ------具体工厂------
class MiFactory(PhoneFactory):
    def make_shell(self):
        return BigShell()

    def make_os(self):
        return Andriod()

    def make_cpu(self):
        return SnapDragonCPU()

class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

    def make_os(self):
        return Andriod()

    def make_cpu(self):
        return MediaTekCPU()

class AppleFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()

    def make_os(self):
        return IOS()

    def make_cpu(self):
        return AppleCPU()

# ------客户端------
class Phone:
    def __init__(self,shell,os,cpu):
        self.shell=shell
        self.os=os
        self.cpu=cpu

    def show_info(self):
        print('手机信息')
        self.cpu.show_cpu()
        self.shell.show_shell()
        self.os.show_os()

def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(shell,os,cpu)

p1 = make_phone(AppleFactory())
p1.show_info()