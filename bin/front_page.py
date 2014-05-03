import web

urls = (
  '/', 'index'
)

front_page = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hello World"
        return greeting

if __name__ == "__main__":
    front_page.run()
