SELECT s.name FROM students s
JOIN marks m ON m.student_id = s.id
WHERE s.admission_date >= (CURRENT_DATE - INTERVAL 6 MONTH)
GROUP BY s.id, s.name HAVING AVG(m.score) > 80;