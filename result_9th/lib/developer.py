import openpyxl

from lib.codehelper import get_safe_output_xls_path, data_path, \
    get_column_config_for_subject
from lib.db import get_exam_map_for_all_subjects
from lib.excelhelper import save_close_and_start, add_table


def get_column_ids(*args, **kwargs):
    filepath = get_safe_output_xls_path("column_id", False)
    wb = openpyxl.Workbook()
    sht = wb.active
    with open(data_path + "\\export_columns.csv", encoding='utf8') as f:
        subs = [x.strip().split(",")[0] for x in f.readlines() if x.strip()]
    exam_map = get_exam_map_for_all_subjects()
    out = [["Subject", "Exam", "Column ID"]]
    for sub in subs:
        colinfo = get_column_config_for_subject(sub)
        for col in colinfo:
            colnm = col['nm'] if 'nm' in col else exam_map[int(col['id'])][0]
            out.append([sub, colnm, str(col['id'])])
    add_table(sht, 1, 1, out)
    save_close_and_start(wb, filepath)


def create_calculation_formula():
    with open(data_path + "\\colnm_input", encoding='utf8') as f:
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
            if len(row) > 3 and len(row[3]) > 0:
                val += ":" + row[3]
            cfg.append(val)

            if len(row) > 4:
                val = " + ".join(f"md['{x}']" for x in row[4].split())
                assign = f"md['{row[0]}'] = {val}"

                code = f"if (type == 'all' or '{row[0]}' in cols) and " \
                       f"isvalid('" \
                       f"{row[4]}',md):\n\t"
                code += assign
                calc.append(code)

    print(",".join(cfg))
    print("\n".join(calc))
