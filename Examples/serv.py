import sys
import os.path
import pymysql
from jinja2 import Template
sys.path.append("..")

import amazonia


root_path = "E:/Insanity/Web/Python/test"
"""
connection = connection = pymysql.connect(
	host='localhost',
	user='root',
	password='',
	db='',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
)""" 

class MainApp(amazonia.WebApp):
	
	def __call__(self, env, resp):
		if self.fetch_request(env) == "GET":
			return self.fetch_static(env, resp)
		elif self.fetch_request(env) == "POST":
			return self.fetch_static(env, resp)

amazonia.Server(MainApp(root_path))
