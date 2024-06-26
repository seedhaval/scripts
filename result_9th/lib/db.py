from collections import defaultdict

from lib import sql_template
from lib.codehelper import sqlite_exec_query, fetch_sqlite_rows


def delete_marks_for_div_subject(subject, div):
    qry = sql_template.delete_marks_for_div_subject
    args = [subject, div]
    sqlite_exec_query(qry, args)


def bulk_insert_marks(ar):
    qry = "insert into student_marks values " + ",\n".join(ar)
    sqlite_exec_query(qry, ())


def get_subject_list():
    qry = sql_template.get_subject_list
    return sorted([x[0] for x in fetch_sqlite_rows(qry, ())])


def get_division_list():
    qry = sql_template.get_division_list
    return sorted([x[0] for x in fetch_sqlite_rows(qry, ())])


def get_student_map(div):
    qry = sql_template.get_students_in_div
    args = [div]
    return [tuple(x) for x in fetch_sqlite_rows(qry, args)]


def get_exam_map(subject):
    qry = sql_template.get_exam_info_for_subject
    args = [subject]
    data = [tuple(x) for x in fetch_sqlite_rows(qry, args)]
    return {x[0]: (x[1], x[2]) for x in data}


def get_exam_map_for_all_subjects():
    qry = sql_template.get_exam_info_for_all_subjects
    data = [tuple(x) for x in fetch_sqlite_rows(qry, [])]
    return {x[0]: (x[1], x[2]) for x in data}


def get_marks_map(subject, division):
    qry = sql_template.get_marks_for_subject
    args = [subject, division]
    data = [tuple(x) for x in fetch_sqlite_rows(qry, args)]
    md = defaultdict(dict)
    for examid, sid, marks, addl_grace in data:
        md[sid][str(examid)] = marks
        md[sid]['additional_grace'] = addl_grace
    return md


def get_marks_map_for_all_subjects(div):
    qry = sql_template.get_marks_for_all_subjects
    data = [tuple(x) for x in fetch_sqlite_rows(qry, [div])]
    md = defaultdict(dict)
    for examid, sid, marks, addl_grace in data:
        md[sid][str(examid)] = marks
        md[sid]['additional_grace'] = addl_grace
    return md


def delete_marks_for_div_exam(examid, div):
    qry = sql_template.delete_marks_for_div_exam
    args = [examid, div]
    sqlite_exec_query(qry, args)


def get_student_marks_for_exam(subject, ctgy, subctgy, div):
    qry = sql_template.get_student_marks_for_exam
    args = [subject, ctgy, subctgy, div]
    return [tuple(x) for x in fetch_sqlite_rows(qry, args)]


def get_exam_categories(subject):
    qry = sql_template.get_exam_category_list
    args = [subject]
    return [x[0] for x in fetch_sqlite_rows(qry, args)]


def get_exam_sub_categories(subject, ctgy):
    qry = sql_template.get_exam_sub_category_list
    args = [subject, ctgy]
    return [x[0] for x in fetch_sqlite_rows(qry, args)]


def exam_details_delete():
    qry = sql_template.exam_details_delete
    sqlite_exec_query(qry, ())


def bulk_insert_exam_details(ar):
    qry = "insert into exam_details values " + ",\n".join(ar)
    sqlite_exec_query(qry, ())


def student_info_delete():
    qry = sql_template.student_info_delete
    sqlite_exec_query(qry, ())


def bulk_insert_student_info(ar):
    qry = "insert into student_info values " + ",\n".join(ar)
    sqlite_exec_query(qry, ())


def student_marks_delete():
    qry = sql_template.student_marks_delete
    sqlite_exec_query(qry, ())


def bulk_insert_reg_info(ar):
    qry = "insert into reg_info values " + ",\n".join(ar)
    sqlite_exec_query(qry, ())


def reg_info_delete():
    qry = sql_template.reg_info_delete
    sqlite_exec_query(qry, ())


def create_reg_info_if_not_exists():
    qry = sql_template.check_if_reg_info_exists
    exst = len([x for x in fetch_sqlite_rows(qry, [])])
    if exst == 0:
        qry = sql_template.create_reg_info
        sqlite_exec_query(qry, [])

def get_reg_info():
    qry = sql_template.get_reg_info
    out = defaultdict(lambda: ('',''))
    for row in fetch_sqlite_rows(qry, []):
        out[str(row[0])] = (row[1], row[2])
    return out
