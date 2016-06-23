# This file is part stock_form module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .location import *

def register():
    Pool.register(
        Location,
        module='stock_form', type_='model')
    Pool.register(
        # ProductByLocation,
        module='stock_form', type_='wizard')
