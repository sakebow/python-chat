from ssocket import ServerSocket
from config import *
from wrapper import *
from utils import *

from threading import Thread

import socket
'''
main functions of server
'''
class Server:
  # init server socket according to base socket
  def __init__(self):
    self.server_socket = ServerSocket()
    pass

  def start(self):
    while True:
      
      # get connection of clients, containing socket and address
      
      soc, addr = self.server_socket.accept()
      # recieve - before using wrapper.py
      # recv_data = soc.recv(SOCKET_CONFIG.SOCKET_MAX_CACHE)
      # print(recv_data.decode(SOCKET_CONFIG.SOCKET_CHARSET_ENCODING))
      # soc.send('connect established'.encode(SOCKET_CONFIG.SOCKET_CHARSET_ENCODING))

      # after using wrapper.py
      client_soc = SocketWrapper(soc)
      
      # for a single client
      # while True:
      #   print(client_soc.recv_data())
      #   client_soc.send_data('connection established!')
      #   pass
      
      # multiple clients
      # t = Thread(target=self.request_handler, args=(client_soc,))
      # t.start()
      #  ----- simplify -----
      Thread(target = lambda: self.request_handler(client_soc)).start()

      # close socket after all done
      # never use if you create a sub thread
      # move it into sub thread, close client socket rather than close server socket
      # soc.close()
      pass
    pass
  
  '''
  1 - if there's message from client, run *socket.send* and *socket.recv*
  2 - if client is offline, close socket and release resources
  '''
  def request_handler(self, client_soc):
    while True:
      msg = client_soc.recv_data()
      client_soc.send_data(f'connection established! return value: {msg}')
      pass
    pass
  pass


# test server
if __name__ == '__main__':
  Server().start()
  pass