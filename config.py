# import redis


class Config(object):
    """配置参数"""

    # 设置秘钥，在使用 CSRF 时必须
    SECRET_KEY = "adfadfadfadadfa"

    # # 连接数据库
    # SQLALCHEMY_DATABASE_URL = "mysql://root:123456@127.0.0.1:3306/db_flask"
    #
    # # 设置sqlalchemy自动跟踪数据库
    # SQLALCHEMY_TRACK_MODIFICATIONS = True

    # # redis
    # REDIS_HOST = '127.0.0.1'
    # REDIS_PORT = 6379
    #
    # # flask-session配置
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # # 对cookie中的session_id进行隐藏处理
    # SESSION_USE_SIGNER = True
    # # session数据的有效期，单位：秒
    # PERMANENT_SESSION_LIFETIME = 86499


class DevelopementConfig(Config):
    """开发模式的配置信息"""
    BEBUG = True


class ProductConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    'develop': DevelopementConfig,
    'product': ProductConfig,
}
