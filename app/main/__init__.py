
#利用蓝图关联到app，让app能够处理视图views函数
from flask import Blueprint
#构建蓝图程序
main = Blueprint('main', __name__)
#导入当前包的路由和视图函数
from . import views, errors

