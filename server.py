import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import json

from robotics import robot3 as robot
 
from tornado.options import define, options
define("port", default=8080, help="run on the given port", type=int)
 
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
 
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('new connection')
        self.write_message("connected")
 
    def on_message(self, message):
        print 'message received %s' % message
        self.write_message('message received %s' % message)
        mapping = {
            # message from websocket to function called
            'forward': robot.forward,
            'reverse': robot.reverse,
	    'right' : robot.turn_right,
	    'left' : robot.turn_left,
            'pivotright' : robot.pivot_right,
            'pivotleft' : robot.pivot_left,
	    'stop' : robot.stop,
	        }

        message_dict = json.loads(message)
        for command, value in message_dict.items():
            if command in mapping:
                print("Launching command: '{}'".format(command))
                action = mapping[command]
                action(value)
            else:
                print("Unknown command: '{}'".format(command))
 
    def on_close(self):
        print 'connection closed'
 
if __name__ == "__main__":
    robot.init()

    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/ws", WebSocketHandler)
        ]
    )
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(options.port)
    print "Listening on port:", options.port
    tornado.ioloop.IOLoop.instance().start()
