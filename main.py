#
#  main.py
#  
#  Copyright 2015 Ericson Willians (Rederick Deathwill) <EricsonWRP@ERICSONWRP-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from paste import httpserver
from bs4 import BeautifulSoup
from binascii import hexlify

class Server(object):
	
	def __init__(self, webapp, host="127.0.0.1", port="8080"):
		httpserver.serve(webapp, host, port)

class ServerResource(object):
	
	MEDIA_EXTENSIONS = [
		".jpg",
		".jpeg",
		".png",
		".gif",
		".wav",
		".mp3",
		".avi",
		".wma"
	]
	
	def __init__(self, path, enc="utf-8"):
		for ext in ServerResource.MEDIA_EXTENSIONS:
			if path.endswith(ext):
				with open(path, "rb") as f:
					self.content = f.read()
			else:
				with open(path, 'r', encoding=enc) as f:
					self.content = f.read()

class WebPage(object):
	
	def __init__(self, html=""):
		if html:
			self.html = html
		else:
			self.html = \
			"""
				<!DOCTYPE html>
				<html>
					<head>
						<title></title>
					</head>
					<body><h1>Amazonia App</h1></body>
				</html>
			"""
			self.soup = BeautifulSoup(self.html, "lxml")

	def add_meta_tags(self, **kwargs):
		if kwargs:
			for key in kwargs:
				if len(kwargs[key]) == 2:
					new_soup = BeautifulSoup('\
						<meta {attr_name}="{attr_value}" content="{content_value}">'.format(
							attr_name = key,
							attr_value = kwargs[key][0],
							content_value = kwargs[key][1]))
					self.soup.head.insert(0, new_soup.find("meta"))
				elif len(kwargs[key]) == 1:
					new_soup = BeautifulSoup('\
						<meta {attr_name}="{attr_value}">'.format(
							attr_name = key,
							attr_value = kwargs[key][0]))
					self.soup.head.insert(0, new_soup.find("meta"))
			self.update_document()

	def link_css(self, *links):
		if links:
			for link in links:
				new_soup = BeautifulSoup('<link rel="stylesheet", \
					href="{external_css}", type="text/css">'.format(external_css = link), "lxml")
				self.soup.head.insert(0, new_soup.find("link"))
			self.update_document()
	
	def link_js(self, *links):
		if links:
			for link in links:
				new_soup = BeautifulSoup('<script language="javascript", \
					src="{external_js}", type="text/javascript"></script>'.format(external_js = link), "lxml")
				self.soup.head.insert(0, new_soup.find("link"))
			self.update_document()
	
	def update_document(self):
		self.html = self.__str__()
		
	def __str__(self):
		return self.soup.prettify()

class WebApp(object):
	
	MIME_TABLE = {
		".txt": "text/plain",
		".css": "text/css",
		".js": "application/javascript",
		".jpg": "image/jpeg",
		".png": "image/png"
	}
	
	def __init__(self, root_path):
		self.root_path = root_path
	
	def __call__(self, environ, start_response):
		path_info = environ["PATH_INFO"]
		for ext in WebApp.MIME_TABLE.keys():
			if path_info.endswith(ext):
				if ext in ServerResource.MEDIA_EXTENSIONS:
					res = ServerResource(self.root_path + path_info).content
					start_response("200 OK", [("Content-type", WebApp.MIME_TABLE[ext])])
					return [res]
				else:
					res = ServerResource(self.root_path + path_info).content
					start_response("200 OK", [("Content-type", WebApp.MIME_TABLE[ext])])
					return [str.encode(res)]
			elif path_info == "/" or path_info == "/index.html":
				res = ServerResource(self.root_path + "/index.html").content
				start_response("200 OK", [("Content-type", "text/html")])
				return [str.encode(res)]
