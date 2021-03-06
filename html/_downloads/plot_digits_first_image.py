#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
The Digit Dataset
=========================================================
This dataset is made up of 1797 8x8 images. Each image,
like the one shown below, is of a hand-written digit.
In order to ultilise an 8x8 figure like this, we'd have to
first transform it into a feature vector with lengh 64.

See 
`here <http://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits>`_ 
for more information about this dataset.
"""
print __doc__


# Code source: Gael Varoqueux
# Modified for Documentation merge by Jaques Grobler
# License: BSD

from sklearn import datasets

import pylab as pl

#Load the digits dataset
digits = datasets.load_digits()

#Display the first digit
pl.figure(1, figsize=(3, 3))
pl.imshow(digits.images[0], cmap=pl.cm.gray_r)
pl.show()

