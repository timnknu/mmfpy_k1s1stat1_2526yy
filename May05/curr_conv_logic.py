rates = {
    'USD': {'UAH': 36.57, 'EUR': 0.92, 'USD': 1},
    'EUR': {'UAH': 39.78, 'EUR': 1, 'USD': 1.09},
    'UAH': {'UAH': 1, 'EUR': 0.025, 'USD': 0.027}
}

# cFrom = 'UAH'
# cTo = 'USD'
# k = rates[cFrom][cTo]
# print(k)

class InvalidFormatError(Exception):
    pass
class UnknownCurrencyError(Exception):
    pass
class NegativeAmountError(Exception):
    pass


def convert_currencies(s):
    d = s.split()
    if len(d) != 2:
        raise InvalidFormatError
    try:
        v = float(d[0])
    except:
        raise InvalidFormatError
    if v < 0:
        raise NegativeAmountError

    cFrom = d[1]
    if cFrom not in rates.keys():
        raise UnknownCurrencyError

    k = rates[cFrom]['UAH']
    res = v * k
    return res