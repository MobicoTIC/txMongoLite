# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class Document(object):
    def __init__(self, doc=None, gen_skel=True, collection=None):
        self.collection = collection

    def __call__(self, doc=None, gen_skel=True):
        return self._obj_class(
            doc=doc,
            gen_skel=gen_skel,
            collection=self.collection)
