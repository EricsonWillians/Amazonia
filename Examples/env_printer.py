#
#  env_printer.py
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

from Amazonia.main import WebApp

# This example class outputs the entire environment dictionary.

class EnvPrinter(WebApp):
    
    def __init__(self):
        WebApp.__init__(self, "Env Printer")
        
    def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-type", "text/html")])
        env_list = ["</br>" + str(item) for item in environ.items()]                               
        
        return [str.encode(str(env_list))]

application = EnvPrinter()
