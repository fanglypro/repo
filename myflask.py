from flask import Flask

app = Flask(__name__)   # python 特殊成员:  __name__   app就代表flask实例
print(__name__)

@app.route("/",methods = ['GET','POST'])  # 完成地址与方法的映射操作，使得方法可以接收前方的请求
def home():
    return "<h1> hello flask </h1>"

@app.route("/login",methods = ['post','get'])
def login():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


if __name__ == '__main__': #当前模块调用则运行，其他程序引入则不启动服务
    app.run()  # 启动了一个服务,默认端口5000