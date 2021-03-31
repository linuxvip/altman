from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from config import config_map


# 数据库
db = SQLAlchemy()

# 创建redis连接
redis_store = None

# 为flask补充csrf防护
csrf = CSRFProtect()

def create_app(config_name):
    app = Flask(
        __name__,
        template_folder='template',
        static_folder='static'
    )

    # 根据配置模式的名字获取配置参数类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # # 使用app初始化db
    # db.init_app(app)

    # 初始化
    csrf.init_app(app)


    # 注册引入的蓝图实例
    from apps.users import users as users_blueprint
    from apps.ablum import ablum as ablum_blueprint

    app.register_blueprint(ablum_blueprint, url_prefix='/api/ablum')
    app.register_blueprint(users_blueprint, url_prefix='/api/user')
    # 添加前缀  http://127.0.0.1:5000/user/list/

    return app
