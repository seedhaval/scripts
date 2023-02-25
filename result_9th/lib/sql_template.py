
get_student_marks_for_exam = """
select
  a.student_id
  ,a.student_name
  ,b.exam_id
  ,coalesce(b.marks,-999)
from student_info a 

left outer join student_marks b 
on a.student_id = b.student_id 

left outer join exam_details c 
on b.exam_id = c.exam_id

where c.subject = ? 
and c.exam_category = ?
and c.exam_sub_category = ?
and a.division = ?
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