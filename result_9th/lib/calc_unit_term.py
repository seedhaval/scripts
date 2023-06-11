from lib.calchelper import add, multiply, oneof, get_fail_count, \
    get_fail_count_lt, get_grade


def calc_unit_1(md):
    add(md, 'tmp.1', '37 38')
    add(md, 'tmp.2', '106 107')
    add(md, 'gc1.6', '70 71')
    add(md, 'gc1.7', '86 87')
    oneof(md, 'gc1.1', '13 25 tmp.1')
    oneof(md, 'gc1.2', 'tmp.2 122')
    add(md, 'gc1.3', '1 gc1.1 58 gc1.6 gc1.7 gc1.2')
    multiply(md, 'gc1.4', 'gc1.3', 0.71428)
    get_fail_count(md, 'gc1.fcount',
                   '1:7 gc1.1:7 58:7 gc1.6:14 gc1.7:7 gc1.2:7')
    if 'gc1.fcount' not in md:
        return
    md['gc1.5'] = 'Pass' if md['gc1.fcount'] == 0 else f"F{md['gc1.fcount']}"


def calc_unit_2(md):
    add(md, 'tmp.1', '47 48')
    add(md, 'tmp.2', '114 115')
    add(md, 'gc2.6', '78 79')
    add(md, 'gc2.7', '96 97')
    oneof(md, 'gc2.1', '19 31 tmp.1')
    oneof(md, 'gc2.2', 'tmp.2 125')
    add(md, 'gc2.3', '7 gc2.1 64 gc2.6 gc2.7 gc2.2')
    multiply(md, 'gc2.4', 'gc2.3', 0.71428)
    get_fail_count(md, 'gc2.fcount',
                   '7:7 gc2.1:7 64:7 gc2.6:14 gc2.7:7 gc2.2:7')
    if 'gc2.fcount' not in md:
        return
    md['gc2.5'] = 'Pass' if md['gc2.fcount'] == 0 else f"F{md['gc2.fcount']}"


def calc_term_1(md):
    oneof(md, 'ps.1', 'hin.2 snsk.2 ssh.3')
    add(md, 'ps.2', 'eng.2 ps.1 mar.2')
    add(md, 'ps.3', 'sci.3 mat.3')
    oneof(md, 'ps.4', 'soc.6 tec.2')
    add(md, 'ps.5', 'ps.2 ps.3 ps.4')
    multiply(md, 'ps.6', 'ps.5', 0.1666)
    get_grade(md, 'ps.10', 'ncc.1')
    get_fail_count_lt(md, 'ps.fcount', 'ps.7',
                      'mar.2 ps.1 eng.2 mat.3 sci.3 ps.4', 35)


def calc_term_2(md):
    oneof(md, 'ds.1', 'hin.4 snsk.4 ssh.6')
    add(md, 'ds.2', 'eng.4 ds.1 mar.4')
    add(md, 'ds.3', 'sci.6 mat.6')
    oneof(md, 'ds.4', 'soc.13 tec.4')
    add(md, 'ds.5', 'ds.2 ds.3 ds.4')
    multiply(md, 'ds.6', 'ds.5', 0.1666)
    get_grade(md, 'ds.10', 'ncc.2')
    get_fail_count_lt(md, 'ds.fcount', 'ds.7',
                      'mar.4 ds.1 eng.4 mat.6 sci.6 ds.4', 35)
