# This file is part stock_form module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction
from trytond.modules.stock_calculation import StockMixin


class Location(StockMixin):
    __metaclass__ = PoolMeta
    __name__ = 'stock.location'
    input_quantity = fields.Function(fields.Float('Input Quantity'),
        'get_input_output_quantity')
    output_quantity = fields.Function(fields.Float('Output Quantity'),
        'get_input_output_quantity')

    @classmethod
    def get_input_output_quantity(cls, locations, names):
        pool = Pool()
        Product = pool.get('product.product')
        Date = pool.get('ir.date')

        context = Transaction().context

        res = {}
        location_ids = [l.id for l in locations]
        for name in names:
            res[name] = {}.fromkeys(location_ids, 0.0)

        product_id = context.get('product')
        stock_date_end = context.get('stock_date_end', Date.today())

        if product_id:
            product = Product(product_id)
            with Transaction().set_context(stock_date_end=stock_date_end,
                    locations=[l.id for l in locations]):
                input_stock = cls.get_input_output_location([product], 'input_stock')[product.id]
                output_stock = cls.get_input_output_location([product], 'output_stock')[product.id]
            for l in locations:
                if l.id in output_stock:
                    res['output_quantity'].update({l.id: output_stock[l.id]})
                if l.id in input_stock:
                    res['input_quantity'].update({l.id: input_stock[l.id]})
        return res
