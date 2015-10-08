# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from txmongo.collection import Collection

class Collection(Collection):
    def __init__(self, *args, **kargs):
        self._documents = {}
        self._collections = {}
        super(Collection, self).__init__(*args, **kargs)
        self._registered_documents = self.database.connection._registered_documents

    def __getattr__(self, key):
        if key in self._registered_documents:
            if key not in self._documents:
                self._documents[key] = self._registered_documents[key](
                    collection=self)
            return self._documents[key]
        else:
            newkey = u"{}.{}".format(self.name, key)
            if newkey not in self._collections:
                self._collections[newkey] = Collection(self.database, newkey)
            return self._collections[newkey]

    def __getitem__(self, key):
        return getattr(self, key)
