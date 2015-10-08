# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from twisted.internet import defer


class Document(object):
    def __init__(self, doc=None, gen_skel=True, collection=None):
        self.collection = collection

    @defer.inlineCallbacks
    def aggregate(self, *args, **kargs):
        """TODO: Must add wrap support"""
        defer.returnValue((yield self.collection.aggregate(*args, **kargs)))
