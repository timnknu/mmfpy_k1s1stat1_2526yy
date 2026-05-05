rates = {
    'USD': {'UAH': 36.57, 'EUR': 0.92, 'USD': 1},
    'EUR': {'UAH': 39.78, 'EUR': 1, 'USD': 1.09},
    'UAH': {'UAH': 1, 'EUR': 0.025, 'USD': 0.027}
}


# cFrom = 'UAH'
# cTo = 'USD'
# k = rates[cFrom][cTo]
# print(k)


def convert_currencies(s):
    d = s.split()
    v = float(d[0])
    cFrom = d[1]
    k = rates[cFrom]['UAH']
    res = v * k
    return res