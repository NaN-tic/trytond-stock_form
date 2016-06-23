# This file is part stock_form module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class StockFormTestCase(unittest.TestCase):
    'Test Stock Form module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('stock_form')

    def test0005views(self):
        'Test views'
        test_view('stock_form')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockFormTestCase))
    return suite
