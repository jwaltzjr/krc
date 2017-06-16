import base64
import os
import sys

from Crypto.Cipher import AES

class EnvVar(object):

    if (sys.version_info > (3, 0)): # Python 3
        X = b'uWFBxsfP8tuajNGB'
    else: # Python 2
        X = 'uWFBxsfP8tuajNGB'

    def __init__(self, name):
        self.name = name.upper()
        self.cipher = AES.new(self.__class__.X, AES.MODE_ECB)

    @property
    def value(self):
        raw_value = os.environ[self.name]
        if (sys.version_info > (3, 0)): # Python 3
            value = self.cipher.decrypt(base64.b64decode(raw_value)).strip()
        else: # Python 2
            value = self.cipher.decrypt(base64.b64decode(raw_value)).strip().decode('utf-8')
        return value

    @value.setter
    def value(self, value):
        value_justified = value.rjust(32)
        encoded = base64.b64encode(self.cipher.encrypt(value_justified))
        os.system('setx %s %s' % (self.name, encoded))
