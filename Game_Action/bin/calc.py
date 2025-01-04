def reshape_to_3d(lst, rows_per_page, cols_per_row):
    result = []
    page = []
    row = []
    for idx, value in enumerate(lst):
        row.append(value)
        if len(row) == cols_per_row:
            page.append(row)
            row = []
        if len(page) == rows_per_page:
            result.append(page)
            page = []
    if row:
        page.append(row)
    if page:
        result.append(page)
    return result
