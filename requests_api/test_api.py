#pytest 的默认的测试用例规则
#1.模块名必须以test_或者_test结尾
#2.类名必须以Test开头
#3。测试用例名必须要以test_开头
#*args 和**kwargs 的区别 ,*args 是一个可变元祖，而**kwargs 是一个可变字典



'''
def get(url,params= None,**kwargs):
def post(url,data=None ,**kwargs):
def put(url,data= None,**kwargs):
def delste(url ,**kwargs):
    前面四个方法都会调用下面的方法
def request(methon,url,**kwargs): 根据method 传参的请求方式发送请求
前面这个方法调用下面的request方法
def session（）获取回话对象
def session (self,method,url,params=None....)

method ：请求方式
URL ：请求路径
params ： get 请求传参
data =None 可以是post或者put 的传参
json = None post的第二种传参方式
headers =None请求头
cookies=  None 请求头里面的cookies 信息
files = None 文件上传
stream = None 文件下载


返回内容
res.text  返回字符串
res.contesnt 返回字节数据
res.json()     返回json 数据，字典
res.status.code     返回状态码
res.resson       返回状态信息
res.cookies         返回响应cookie
res.encoding            返回响应编码
res.headers             返回响应头
res.request.xxx     返回请求的一些数据

'''
class TestApi:
    #
    def test_get_token(self):
        pass
if __name__=="__main__"
