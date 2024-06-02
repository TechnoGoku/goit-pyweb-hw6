SELECT 
    students.fullname AS student_name,
    grades.grade,
    grades.grade_date
FROM 
    grades
JOIN 
    students ON grades.student_id = students.id
JOIN 
    subjects ON grades.subject_id = subjects.id
JOIN 
    groups ON students.group_id = groups.id
WHERE 
    groups.name = 'Анімешки'  -- Замените 'Название группы' на имя группы
    AND subjects.name = 'Біологія';  -- Замените 'Название предмета' на имя предмета
