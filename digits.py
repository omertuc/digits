from math import log10, floor


for current_power in range(4, 1024):
    last_exp = floor(log10(2 ** current_power))

    fast = sum(
            ((10 ** current_10exp) - 10 ** (current_10exp - 1)) * current_10exp
            for current_10exp in range(1, last_exp + 1)
        ) + (2 ** current_power - 10 ** last_exp) * (last_exp + 1)

    # slow = sum(len(str(x)) for x in range(1, 2**current_power))

    print(
        current_power,
        fast,
        # slow,
        # slow / fast * 100,
    )
