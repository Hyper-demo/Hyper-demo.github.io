# 将整个应用初始化
# 主要工作
#     1：构建flask应用以及各种配置
#     2：构建SQLAlchemy的应用

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
#from flask_login import LoginManager
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

#login_manager = LoginManager()
#login_manager.login_view = 'auth.login'

def create_app(config_name):
    print(config_name)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    bootstrap.init_app(app)
    moment.init_app(app)
    #login_manager.init_app(app)
    #数据库的初始化
    db.init_app(app)

    #将main蓝图程序与app关联到一起
    from .main import main as main_blueprint
    # 注册名为main的app
    app.register_blueprint(main_blueprint)

    #from .auth import auth as auth_blueprint
    #app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
