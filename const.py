import sys
class const(object):
    class ConstError(): pass
    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise Exception(self.ConstError, "Changing const.%s" % key)
        else:
            self.__dict__[key] = value
    def __getattr__(self, key):
        if self.__dict__.has_key(key):
            return self.key
        else:
            return None
sys.modules[__name__] = const()

const.PITCH_TEXT = 'Pitch : '