SELECT s.department, AVG(m.score) AS avg_score FROM students s
JOIN marks m ON m.student_id = s.id
GROUP BY s.department;