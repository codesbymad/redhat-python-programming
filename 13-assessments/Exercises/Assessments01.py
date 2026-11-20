for ngarrafas in range(99, 0, -1):
    if ngarrafas == 1:
        plural = ''
        proxima_garrafa = 'No more bottles'
    else:
        plural = 's'
        if ngarrafas - 1 == 1:
            proxima_garrafa = '1 bottle'
        else:
            proxima_garrafa = f'{ngarrafas - 1} bottles'

    print(f'{ngarrafas} bottle{plural} of water on the wall!')
    print(f'{ngarrafas} bottle{plural} of water!')
    print('Take one down')
    print('And pass it around')
    print(f'{proxima_garrafa} of water on the wall!')
    print()