# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.users_controller import api as user_ns
from .main.controller.owners_controller import api as owners_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/users')
api.add_namespace(owners_ns, path='/owners')