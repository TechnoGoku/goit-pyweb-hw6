SELECT 
    subjects.name AS subject_name
FROM 
    grades
JOIN 
    subjects ON grades.subject_id = subjects.id
JOIN 
    students ON grades.student_id = students.id
WHERE 
    students.id = 1;  -- Замените 1 на нужный id студента
