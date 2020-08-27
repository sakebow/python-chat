from enum import Enum
'''
enum all allowed protocol flags
'''
class PROTOCOL_FLAG(Enum):
  REQUEST_LOGIN_FLAG = '10001'
  REQUEST_CHAT_FLAG = '10002'
  RESPONSE_LOGIN_FLAG = '90011'
  RESPONSE_CHAT_FLAG = '90012'
  pass

'''
config about server
'''
class SERVER_CONFIG(Enum):
  SERVER_IP = '192.168.1.111'
  SERVER_PORT = 2080
  pass

class SOCKET_CONFIG(Enum):
  SOCKET_MAX_CACHE = 1232896
  SOCKET_CHARSET_ENCODING = 'utf-8'
  pass