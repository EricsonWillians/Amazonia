from Amazonia.main import WebPage, WebApp
from paste import httpserver

webpage = WebPage()
webpage.add_css("css/bootstrap.min.css", "font-awesome/css/font-awesome.min.css")

application = webApp(webpage)

# if __name__ == "__main__":
#	httpserver.serve(WebApp(webpage), host = "192.168.0.77", port = "8080")
