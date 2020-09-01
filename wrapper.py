from config import *
import socket

'''
package socket
'''
class SocketWrapper:
  def __init__(self, soc):
    self.soc = soc
    pass

  def recv_data(self):
    try:
      return self.soc.recv(SOCKET_CONFIG.SOCKET_MAX_CACHE.value).decode(SOCKET_CONFIG.SOCKET_CHARSET_ENCODING.value)
    except:
      return 'a client closed connection'
    pass

  def send_data(self, message):
    return self.soc.send(message.encode(SOCKET_CONFIG.SOCKET_CHARSET_ENCODING.value))
    pass

  def close(self):
    if self.soc is not None:
      self.soc.close()
      pass
    pass
  pass