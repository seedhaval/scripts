from nsepython import get_bhavcopy
from datetime import date
import json

dates = {
    'latest': date(2023, 4, 6)
    , 'prv_mo_1': date(2023, 3, 7)
    , 'prv_mo_2': date(2023, 3, 14)
    , 'six_mo_1': date(2022, 9, 29)
    , 'six_mo_2': date(2022, 9, 5)
    , 'prv_yr_1': date(2022, 1, 4)
    , 'prv_yr_2': date(2022, 1, 28)
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
            self.prv_mo = (self.prv_mo_2 + self.prv_mo_1) / 2
        else:
            self.prv_mo = None

        if self.six_mo_1 and self.six_mo_2:
            self.six_mo = (self.six_mo_1 + self.six_mo_2) / 2
        else:
            self.six_mo = None

        if self.prv_yr_1 and self.prv_yr_2:
            self.prv_yr = (self.prv_yr_1 + self.prv_yr_2) / 2
        else:
            self.prv_yr = None

        if self.latest and self.prv_mo and self.six_mo and self.prv_yr:
            self.valid = True
        else:
            self.valid = False


def get_net_data():
    d = {}

    for k, v in dates.items():
        print(k, v.strftime("%d-%m-%Y"))
        d[k] = {x[0]: x[9] for x in get_bhavcopy(
            date=v.strftime(
                "%d-%m-%Y")).values.tolist()}

    with open('out.json', 'w') as f:
        f.write(json.dumps(d, indent=2))


# get_net_data()
scrip_ar = []

with open('out.json', 'r') as f:
    d = json.load(f)

for k in d['latest'].keys():
    s = Scrip(d, k)
    if s.valid:
        scrip_ar.append(s)


def clause_1(scrip_ar):
    out = []
    for s in scrip_ar:
        if s.latest < 5000 and s.prv_yr < s.six_mo and s.prv_mo > s.latest:
            out.append([s.nm, s.latest, s.prv_mo, -(s.prv_mo * 1.0) / s.latest])
    return out

def clause_2(scrip_ar):
    out = []
    for s in scrip_ar:
        if s.latest < 5000 \
                and s.prv_yr < s.six_mo \
                and s.six_mo > s.latest:
            out.append([s.nm, s.latest, s.six_mo, -(s.six_mo * 1.0) / s.latest])
    return out

#out = clause_1(scrip_ar)
out = clause_2(scrip_ar)

for row in sorted(out, key=lambda x: x[3]):
    print(row)
