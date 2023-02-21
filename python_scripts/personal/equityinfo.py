from nsepy.history import get_price_list
from datetime import date
import json

dates = {
    'latest': date(2023, 2, 17)
    , 'prv_mo_1': date(2023, 1, 11)
    , 'prv_mo_2': date(2023, 1, 25)
    , 'six_mo_1': date(2022, 8, 10)
    , 'six_mo_2': date(2022, 8, 23)
    , 'prv_yr_1': date(2021, 12, 7)
    , 'prv_yr_2': date(2021, 12, 21)
}

class Scrip:
    def __init__(self, d, nm):
        self.nm = nm
        self.latest = d['latest'].get(nm, None)
        self.prv_mo_1 = d['prv_mo_1'].get(nm, None)
        self.prv_mo_2 = d['prv_mo_2'].get(nm, None)
        self.six_mo_1 = d['six_mo_1'].get(nm, None)
        self.six_mo_2 = d['six_mo_2'].get(nm, None)
        self.prv_yr_1 = d['prv_yr_1'].get(nm, None)
        self.prv_yr_2 = d['prv_yr_2'].get(nm, None)

        if self.prv_mo_1 and self.prv_mo_2:
            self.prv_mo = (self.prv_mo_2+self.prv_mo_1)/2
        else:
            self.prv_mo = None

        if self.six_mo_1 and self.six_mo_2:
            self.six_mo = (self.six_mo_1+self.six_mo_2)/2
        else:
            self.six_mo = None

        if self.prv_yr_1 and self.prv_yr_2:
            self.prv_yr = (self.prv_yr_1+self.prv_yr_2)/2
        else:
            self.prv_yr = None

        if self.latest and self.prv_mo and self.six_mo and self.prv_yr:
            self.valid = True
        else:
            self.valid = False


def get_net_data():
    d = {}

    for k, v in dates.items():
        print(k)
        d[k] = {x[0]: x[5] for x in get_price_list(dt=v).values.tolist()}

    with open('out.json', 'w') as f:
        f.write(json.dumps(d, indent=2))


#get_net_data()
scrip_ar = []

with open('out.json', 'r') as f:
    d = json.load(f)

for k in d['latest'].keys():
    s = Scrip(d, k)
    if s.valid:
        scrip_ar.append(s)

out = []
for s in scrip_ar:
    if s.latest < 2000 and s.prv_yr < s.six_mo and s.prv_mo > s.latest:
        out.append([s.nm, s.latest, s.prv_mo])

for row in sorted(out, key=lambda x: (x[2] * 1.0) / x[1], reverse=True):
    print(row)
