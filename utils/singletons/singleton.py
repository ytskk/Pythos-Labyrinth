# class SingletonClass(object):
#     def __new__(cls):
#         if not hasattr(cls, "instance"):
#             cls.instance = super(SingletonClass, cls).__new__(cls)
#         return cls.instance


class MetaSingleton(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self._instances[self]
