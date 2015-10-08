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
    def setUp(self):
        print('creating')
        self.connection = Connection()
        print('getting subattributes')
        print(type(self.connection['txmltest']))
        self.col = self.connection['txmltest']['txmongolite']
        self.col.insert({'test': 'value'})

    def tearDown(self):
        pass

    @defer.inlineCallbacks
    def test_aggregate(self):
        class TestDoc(Document):
            pass
        self.connection.register([TestDoc])
        print('before TestDoc')
        testdoc = self.col.TestDoc()
        resp = list((yield testdoc.aggregate([{"$match": {"test": "value"}}])))
        self.assertEqual(len(resp), 1)
