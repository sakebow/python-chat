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
    return self.soc.recv(SOCKET_CONFIG.SOCKET_MAX_CACHE.value).decode(SOCKET_CONFIG.SOCKET_CHARSET_ENCODING.value)
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

'''
package the result
account result:
  - flag    - which result / protocol flag code
  - success - certificated or not / True or False
  - nick    - nickname, show on chat room / String
  - user    - username, hidden in system / String
  - message - None
message result:
  - flag    - which result / protocol flag code
  - success - reach or not / True or False
  - nick    - nickname, show on chat room / String
  - user    - None
  - message - text in input box / String
'''
class ResultSet:
  def __init__(self, flag, success, nick, user, message):
    self.flag = flag
    self.success = success
    self.nick = nick
    self.user = user
    self.message = message
    pass
  pass