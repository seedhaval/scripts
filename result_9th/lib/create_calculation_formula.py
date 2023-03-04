with open("../data/colnm_input", encoding='utf8') as f:
    data = [x.strip().split("\t") for x in f.readlines() if x.strip()]

cfg = [data[0][1]]
calc = []

for row in data:
    if row[0][0] in '123456789':
        if len(row) > 5:
            cfg.append(f"{row[0]}:{row[5]}")
        else:
            cfg.append(row[0])
    else:
        pfx = row[0].split('.')[0]
        val = f"{row[0]}:{row[2]}:{row[1]}"
        if len(row[3]) > 0:
            val += ":" + row[3]
        cfg.append(val)

        if len(row) > 4:
            val = " + ".join( f"md['{x}']" for x in row[4].split())
            assign = f"md['{row[0]}'] = {val}"

            code = f"if (type == 'all' or '{row[0]}' in cols) and isvalid('" \
                   f"{row[4]}',md):\n\t"
            code += assign
            calc.append(code)


print(",".join(cfg))
print("\n".join(calc))
