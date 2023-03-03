delete_marks_for_div_subject = """
delete from student_marks
where exam_id in (
  select exam_id
  from exam_details
  where subject = ?
)
and student_id in (
  select student_id
  from student_info
  where division = ?
)
"""


delete_marks_for_div_exam = """
delete from student_marks
where exam_id = ?
and student_id in (
  select student_id
  from student_info
  where division = ?
)
"""

get_student_marks_for_exam = """
select
  a.student_id
  ,a.roll_no
  ,a.student_name
  ,b.exam_id
  ,coalesce(c.marks,-999)
  ,b.total_marks
from student_info a 

left outer join exam_details b
on b.subject = ?
and b.exam_category = ?
and b.exam_sub_category = ?

left outer join student_marks c
on a.student_id = c.student_id
and b.exam_id = c.exam_id

where a.division = ?
"""

get_subject_list = """
select subject
from exam_details
group by 1
""".strip()

get_exam_category_list = """
select exam_category
from exam_details
where subject = ?
group by 1
order by exam_id
"""

get_exam_sub_category_list = """
select exam_sub_category
from exam_details
where subject = ?
and exam_category = ?
group by 1
order by exam_id
"""

get_division_list = """
select division
from student_info
group by 1
order by student_id
"""

get_students_in_div = """
select
  student_id
  ,roll_no
  ,student_name
from student_info
where division = ?
"""

get_exam_info_for_subject = """
select
  exam_id
  ,case when exam_category = exam_sub_category then exam_category
      else exam_category || ' - ' || exam_sub_category end as exam_name
  ,total_marks
from exam_details
where subject = ?
"""

get_marks_for_subject = """
select
  a.exam_id
  ,a.student_id
  ,a.marks
from student_marks a

inner join exam_details b
on a.exam_id = b.exam_id
and b.subject = ?
"""

get_marks_for_all_subjects = """
select
  a.exam_id
  ,a.student_id
  ,a.marks
from student_marks a

inner join student_info b
on a.student_id = b.student_id
and b.division = ?
"""

exam_details_delete = """
delete from exam_details
"""

student_info_delete = """
delete from student_info
"""

student_marks_delete = """
delete from student_marks
"""