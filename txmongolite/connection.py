# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from txmongo.connection import ConnectionPool

from .database import Database


class CallableMixin(object):
    def __call__(self, doc=None, gen_skel=True):
        return self._obj_class(
            doc=doc,
            gen_skel=gen_skel,
            collection=self.collection)


_iterables = (list, tuple, set, frozenset)


class Connection(ConnectionPool):
    def __init__(self, *args, **kargs):
        self._databases = {}
        self._registered_documents = {}
        super(Connection, self).__init__(*args, **kargs)

    def register(self, obj_list):
        decorator = None
        if not isinstance(obj_list, _iterables):
            decorator = obj_list
            obj_list = [obj_list]

        # register
        for obj in obj_list:
            CallableDocument = type(
                str("Callable{}".format(obj.__name__)),
                (obj, CallableMixin),
                {"_obj_class": obj,
                 "__repr__": object.__repr__}
            )
            self._registered_documents[obj.__name__] = CallableDocument

        if decorator is not None:
            return decorator

    def __getattr__(self, key):
        if key in self._registered_documents:
            document = self._registered_documents[key]
            try:
                return getattr(self[document.__database__]
                               [document.__collection__],
                               key)
            except AttributeError:
                raise AttributeError("{}: __collection__ attribute not found. "
                                     "You cannot specify the `__database__` "
                                     "attribute without the `__collection__` "
                                     "attribute".format(key))
        else:
            if key not in self._databases:
                self._databases[key] = Database(self, key)
            return self._databases[key]

    def __getitem__(self, key):
        return getattr(self, key)
