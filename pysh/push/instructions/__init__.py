# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 15:34:38 2016

@author: Eddie
"""
from __future__ import absolute_import, division, print_function, unicode_literals

# Forces this directory to become a python package.

l = ['boolean', 'char', 'code', 'common', 'io', 'numbers', 'string', 'vectors']
__all__ = [str(x) for x in l]