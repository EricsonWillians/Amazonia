from Amazonia import amazonia
import pymysql

root_path = "G:/Insanity/Web/Apache24/htdocs/Volapp"
connection = connection = pymysql.connect(
	host='localhost',
	user='root',
	password='yourpasshere',
	db='exampledb',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
) 

class MainApp(amazonia.WebApp):
	
	def __call__(self, environ, start_response):
		self.path_info = environ["PATH_INFO"]
		
		return self.get_static_content(self.path_info, start_response)

amazonia.Server(MainApp(root_path))
