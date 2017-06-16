import base64
import os

from Crypto.Cipher import AES

class EnvVar(object):

    X = b'uWFBxsfP8tuajNGB'

    def __init__(self, name):
        self.name = name.upper()
        self.cipher = AES.new(self.__class__.X, AES.MODE_ECB)

    @property
    def value(self):
        raw_value = os.environ[self.name]
        return self.cipher.decrypt(base64.b64decode(raw_value)).strip()

    @value.setter
    def value(self, value):
        value_justified = value.rjust(32)
        encoded = base64.b64encode(self.cipher.encrypt(value_justified))
        os.system('setx %s %s' % (self.name, encoded))
