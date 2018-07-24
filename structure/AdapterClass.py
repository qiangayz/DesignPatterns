from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元"%money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元"%money)

#------待适配的类-----
class WeChatPay:
    def fuqian(self,money):
        print('微信支付%s元'%money)

#------类适配器------
class RealWeChatPay(Payment,WeChatPay):
    def pay(self, money):
        return self.fuqian(money)

#-----对象适配器-----
class PayAdapter(Payment):
    def __init__(self,payment):
        self.payment=payment
    def pay(self, money):
        return self.payment.fuqian(money)

#RealWeChatPay().pay(100)

p=PayAdapter(WeChatPay())
p.pay(200)