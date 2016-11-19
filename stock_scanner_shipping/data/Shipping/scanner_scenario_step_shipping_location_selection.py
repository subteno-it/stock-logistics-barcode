# flake8: noqa
'Use <m> or <message> to retrieve the data transmitted by the scanner.'
'Use <t> or <terminal> to retrieve the running terminal browse record.'
'Put the returned action code in <act>, as a single character.'
'Put the returned result or message in <res>, as a list of strings.'
'Put the returned value in <val>, as an integer'

picking = model.browse(terminal.reference_document)
remaining_moves = picking.move_lines.filtered(lambda record: not record.linked_move_operation_ids).sorted(key=lambda record: (record.location_id.name, record.product_id.default_code, record.id))
move = remaining_moves[0]
next_move_index = 0

if tracer == 'loop':
    next_move_index = 1
    quantity = float(message)

    operation = env['stock.pack.operation'].with_context(no_recompute=True).create({
        'picking_id': picking.id,
        'product_id': move.product_id.id,
        'product_uom_id': move.product_uom.id,
        'product_qty': quantity,
        'location_id': move.location_id.id,
        'location_dest_id': picking.location_id.id,
        'linked_move_operation_ids': [(0, 0, {
            'move_id': move.id,
            'qty': quantity,
        })],
    })

if len(remaining_moves) > next_move_index:
    next_move = remaining_moves[next_move_index]
    terminal.tmp_val1 = next_move.id
    act = 'T'
    res = [
        _('Product: %s') % next_move.product_id.name,
        _('Quantity: %g %s') % (next_move.product_qty, next_move.product_uom.name),
        _('Location: %s') % next_move.location_id.name,
        '',
        _('Scan the location to confirm.'),
    ]
else:
    act = 'A'
