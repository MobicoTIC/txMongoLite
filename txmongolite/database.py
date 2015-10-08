# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from txmongo.database import Database

from .collection import Collection

class Database(Database):
    def __init__(self, *args, **kargs):
        print('creating database')
        self._collections = {}
        super(Database, self).__init__(*args, **kargs)

    def __getattr__(self, key):
        print('getattr in database')
        if key in self.connection._registered_documents:
            document = self.connection._registered_documents[key]
            return getattr(self[document.__collection__], key)
        else:
            if not key in self._collections:
                self._collections[key] = Collection(self, key)
            return self._collections[key]

    def __getitem__(self, key):
        print('getting items!!')
        return getattr(self, key)
