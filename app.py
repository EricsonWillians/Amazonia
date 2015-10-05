#
#  app.py
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

class App(object):
    
    def __init__(self, name):
        self.name = name
        self.html = \
        str.encode("""
            <html>
                <head>
                    <title>{name}</title>
                </head>
                <body>
                    <h1>Amazonia App is working!</h1>
                </body>
            </html>
        """.format(name = self.name))
        
    def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-type", "text/html"),
                                        ('Content-Length', str(len(self.html)))])
        
        return [self.html]
