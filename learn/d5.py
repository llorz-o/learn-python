from abc import ABCMeta, abstractmethod


class Person(object):

    def __init__(self, name):
        self._name = name

    @classmethod
    def factory(cls, name):
        return cls(name)

    @staticmethod
    def static_show():
        print("这是静态方法")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# 抽象类
class Abstract(object, metaclass=ABCMeta):

    __slots__ = ("_name")

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def show(self):
        pass


if __name__ == '__main__':
    person = Person.factory(name='jojo')
    Person.static_show()
    person.static_show()

    print(person.name)
    person.name = 12
    print(person.name)
