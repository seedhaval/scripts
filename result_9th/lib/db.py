from lib import sql_template
from lib.codehelper import sqlite_exec_query, fetch_sqlite_rows
from collections import defaultdict


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


def get_marks_map(subject, division):
    qry = sql_template.get_marks_for_subject
    args = [subject, division]
    data = [tuple(x) for x in fetch_sqlite_rows(qry, args)]
    md = defaultdict(dict)
    for examid, sid, marks in data:
        md[sid][str(examid)] = marks
    return md
