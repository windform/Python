import web
#import MySQLdb
#import MySQLdb.cursors

render = web.template.render('template')
        
urls = (
	'/index', 'index',
	'/blog/\d+', 'blog',
    '/(.*)', 'hello',
)
app = web.application(urls, globals())

''' 
class hello:        
    def GET(self, name):
    	webpage = open(r'static.html','r').read()
        return webpage
'''
class index:
	def GET(self):
		# query=web.input()
		return web.seeother('/hello')

class blog:
	def GET(self):
		return web.ctx.env
	def POST(self):
		data = web.input()
		return data

class hello:
	def GET(self,name):
		return render.static(name)

if __name__ == "__main__":
    app.run()