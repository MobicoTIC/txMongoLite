# -*- coding: utf-8 -*-
"""Test the txMongoLite API"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from twisted.trial import unittest
from twisted.internet import defer

from txmongolite import Connection, Document


#pylint: disable=missing-docstring
class TestApi(unittest.TestCase):
    @defer.inlineCallbacks
    def setUp(self):
        self.connection = yield Connection()
        yield self.connection.txmltest.drop_collection('txmongolite')
        self.col = self.connection['txmltest']['txmongolite']
        self.col.insert({'test': 'value'})

    @defer.inlineCallbacks
    def tearDown(self):
        yield self.connection.txmltest.drop_collection('txmongolite')
        yield self.connection.disconnect()

    @defer.inlineCallbacks
    def test_aggregate(self):
        class TestDoc(Document):
            pass
        self.connection.register([TestDoc])
        testdoc = self.col.TestDoc()
        resp = list((yield testdoc.aggregate([{"$match": {"test": "value"}}])))
        self.assertEqual(len(resp), 1)
