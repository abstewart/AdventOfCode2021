#search until y starts hitting target
    while not yHitTarget(yvel, tgty):
        print('yel: ', yvel, "doesn't hit target")
        yvel += 1
    yvel = 102
    prev = yvel
    print('started to hit target at: ', yvel)
    print('prev = ', prev)
    #keep searching until you have a max y value
    while yHitTarget(yvel, tgty):
        print('yvel: ', yvel, 'hits target')
        prev = yvel
        yvel += 1
    print('part 1 y value: ', prev)
    print(yHitTarget(103, tgty))
    print('part 1 ans?: ', highestPtReached(102))
