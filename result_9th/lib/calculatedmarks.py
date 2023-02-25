def isvalid(txt, md):
    for idx in txt.strip().split():
        if idx not in md:
            return False
    return True


def calculate(md, type, cols):
    if (type == 'all' or 'mar.1' in cols) and isvalid("3 4 5 6", md):
        md["mar.1"] = md["3"] + md["4"] + md["5"] + md["6"]
    if (type == 'all' or 'mar.2' in cols) and isvalid("2 mar.1", md):
        md["mar.2"] = md["2"] + md["mar.1"]
    if (type == 'all' or 'mar.3' in cols) and isvalid("9 10 11 12", md):
        md["mar.3"] = md["9"] + md["10"] + md["11"] + md["12"]
    if (type == 'all' or 'mar.4' in cols) and isvalid("8 mar.3", md):
        md["mar.4"] = md["8"] + md["mar.3"]
    if (type == 'all' or 'mar.5' in cols) and isvalid("mar.2 mar.4", md):
        md["mar.5"] = md["mar.2"] + md["mar.4"]
    if (type == 'all' or 'mar.6' in cols) and isvalid("mar.5", md):
        md["mar.6"] = md["mar.5"] / 2
