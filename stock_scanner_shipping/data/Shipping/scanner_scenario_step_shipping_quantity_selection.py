# flake8: noqa
'Use <m> or <message> to retrieve the data transmitted by the scanner.'
'Use <t> or <terminal> to retrieve the running terminal browse record.'
'Put the returned action code in <act>, as a single character.'
'Put the returned result or message in <res>, as a list of strings.'
'Put the returned value in <val>, as an integer'

move = env['stock.move'].browse(int(terminal.tmp_val1))

act = 'Q'
res = [
    _('Product: %s') % move.product_id.name,
    _('Quantity: %g %s') % (move.product_qty, move.product_uom.name),
    _('Location: %s') % move.location_id.name,
    '',
    _('Quantity ?'),
]
val = move.product_qty - sum(move.linked_move_operation_ids.mapped('qty'))
