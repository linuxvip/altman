from flask_restful import Api
from . import ablum
from .views import IndexView

# 将 ablum 模块蓝图加入Api进行管理
api = Api(ablum)

# 进行路由分发，类似于Django中的url工作内容（视图处理类， 请求路径）
api.add_resource(IndexView, '/list')
