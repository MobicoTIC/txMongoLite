# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from txmongo.database import Database


class Database(Database):
    def __init__(self, *args, **kargs):
        super(Database, self).__init__(*args, **kargs)
