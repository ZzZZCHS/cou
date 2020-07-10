class Person(object):
    """人物"""

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def nameOut(self):
        print('Name:%s' % self._name)

    def rename(self, name):
        self._name = name
        print('Name changed to %s' % self._name)

    def setPosition(self, position):
        self._position = position