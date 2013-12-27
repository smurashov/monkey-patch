from gevent import monkey

monkey.patch_all(socket=True, dns=True, time=True, select=True,
                 thread=True, os=True, ssl=True, httplib=False,
                 subprocess=False, sys=False, aggressive=True,
                 Event=False)
from bfg import BFGPlugin
