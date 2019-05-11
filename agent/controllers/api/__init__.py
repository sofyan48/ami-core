from flask import Blueprint
from flask_restful import Api
from .utils import *
from .inject import *


api_blueprint = Blueprint("api", __name__, url_prefix='/api')
api = Api(api_blueprint)
api.add_resource(AboutNow, '/about/')
##### UTIL API #####
api.add_resource(GetCpuInfo, '/info/cpu')
api.add_resource(GetMemInfo, '/info/memory')
api.add_resource(GetDiskInfo, '/info/disk')

##### INJECT ENDPOINT #####
api.add_resource(Inject, '/inject/<token>')

