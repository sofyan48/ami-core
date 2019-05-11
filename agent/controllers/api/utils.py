from flask_restful import Resource
from agent.helpers.rest import * 
from ami.libs import utils
from ami import __version__
import os

class AboutNow(Resource):
    def get(self):
        return response(200, message="AMI VERSION: "+__version__)

class GetCpuInfo(Resource):
    def get(self):
        cpu_info = utils.get_cpu_info()
        return response(200, data=cpu_info)

class GetMemInfo(Resource):
    def get(self):
        mem_info = utils.get_memory_info()
        return response(200, data=mem_info)

class GetDiskInfo(Resource):
    def get(self):
        disk_info = utils.get_disk_info()
        return response(200, data=disk_info)