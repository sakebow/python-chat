import json
from result import ResultSet
from config import *
'''
some utils
'''
class Utils:
  # package result into a json object
  @staticmethod
  def RESPONSE_LOGIN_RESULT(success, nick, user):
    login_result = ResultSet(PROTOCOL_FLAG.RESPONSE_LOGIN_FLAG.value, success, nick, user, None)
    # __dist__() can list all fields except from inline functions
    return json.dumps(login_result.__dict__)
    pass
  pass