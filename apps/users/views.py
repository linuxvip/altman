from flask_restful import Resource
from apps import db
from flask import current_app

from .models import User


class IndexView(Resource):
    def get(self):
        return 'index page'

    def post(self):
        return {"errno": 1, "errmsg": "成功"}