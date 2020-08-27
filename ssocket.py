import socket
from config import *

'''
init base socket
'''
class ServerSocket(socket.socket):
  def __init__(self):
    super().__init__()
    # this is TCP socket
    super(ServerSocket, self).__init__(socket.AF_INET, socket.SOCK_STREAM)
    # bin address
    self.bind((SERVER_CONFIG.SERVER_IP.value, SERVER_CONFIG.SERVER_PORT.value))
    # listening open
    self.listen(128)
    pass
  pass