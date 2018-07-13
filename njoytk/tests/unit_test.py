# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:54:04 2018

@author: Fiorito_L
"""

import pytest
import os

from njoytk import Njoy
from njoytk import data



@pytest.mark.njoy
@pytest.mark.pendf
def test_pendf(tmpdir):
    nj = Njoy(temps=[600, 900], free_gas=True, sig0=[1e10, 1e4], ptable=True, wdir=str(tmpdir))
    file = os.path.join(data.__path__[0], r"h1.endf")
    options = {
            "tape" : file,
            "mat" : 125,
            "tag" : "H1",
            }
    nj.get_pendf(**options)

@pytest.mark.njoy
@pytest.mark.ace
def test_ace_1(tmpdir):
    nj = Njoy(temps=[293.6], suffixes=[.03], wdir=str(tmpdir))
    file = os.path.join(data.__path__[0], r"h1.endf")
    options = {
            "tape" : file,
            "mat" : 125,
            "tag" : "H1",
            }
    nj.get_ace(**options)

@pytest.mark.njoy
@pytest.mark.ace
def test_ace_2(tmpdir):
    nj = Njoy(wdir=str(tmpdir))
    file = os.path.join(data.__path__[0], r"h1.endf")
    nj.get_ace(file)    