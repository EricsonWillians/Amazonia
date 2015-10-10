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

from bs4 import BeautifulSoup

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
	
	def __init__(self, webpage):
		self.webpage = webpage
		
	def __call__(self, environ, start_response):
		start_response("200 OK", [("Content-type", "text/html")])
		
		return [str.encode(self.webpage.html)]
