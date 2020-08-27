# test json
# from utils import *
# from result import *
# import json

# test server
from server import *
from config import *
import socket

'''
test file
'''
# test server
def test():
  # mock a socket from a client
  csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  csocket.connect((SERVER_CONFIG.SERVER_IP.value, SERVER_CONFIG.SERVER_PORT.value))
  while True:
    msg = input('say...')
    csocket.send(msg.encode(SOCKET_CONFIG.SOCKET_CHARSET_ENCODING.value))
    recv_data = csocket.recv(SOCKET_CONFIG.SOCKET_MAX_CACHE.value)
    print(recv_data.decode(SOCKET_CONFIG.SOCKET_CHARSET_ENCODING.value))
  # close util all done, not the time when message arrives server
  csocket.close()
  pass

if __name__ == "__main__":
  # test util - package object to json
  # print(Utils.RESPONSE_LOGIN_RESULT(True, 'nick', 'user'))
  
  # test client - see if clients and server run correctly
  test()
  pass