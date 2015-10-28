from Amazonia import amazonia
import pymysql

root_path = "G:/Insanity/Web/Apache24/htdocs/Volapp"
connection = connection = pymysql.connect(
	host='localhost',
	user='root',
	password='',
	db='',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
) 

class MainApp(amazonia.WebApp):
	
	def __call__(self, env, resp):
		if self.fetch_request(env) == "GET":
			return self.fetch_static(env, resp)
		elif self.fetch_request(env) == "POST":
			return self.fetch_static(env, resp)

amazonia.Server(MainApp(root_path))
