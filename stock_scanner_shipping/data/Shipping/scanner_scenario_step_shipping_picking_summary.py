# flake8: noqa
'Use <m> or <message> to retrieve the data transmitted by the scanner.'
'Use <t> or <terminal> to retrieve the running terminal browse record.'
'Put the returned action code in <act>, as a single character.'
'Put the returned result or message in <res>, as a list of strings.'
'Put the returned value in <val>, as an integer'

picking = model.search([('name', '=', message)])
picking.pack_operation_ids.unlink()
terminal.reference_document = picking.id

act = 'M'
res = [
    '%s: %g %s' % (move.product_id.name, move.product_qty, move.product_uom.name)
    for move in picking.move_lines.sorted(key=lambda record: (record.location_id.name, record.product_id.default_code, record.id))
    if not move.linked_move_operation_ids
]
