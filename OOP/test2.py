class Nameofclass():
    class_attribute = 'value'
    def __init__(self,param1,param2):
        self._param1 = param1
        self._param2 = param2
    def method(self):
        return self._param2 + self._param1
    @classmethod
    def cls_methd(cls,param1,param2):
        return cls(param1,param2)
    @staticmethod
    def stc_methd(param1,param2):
        pass

