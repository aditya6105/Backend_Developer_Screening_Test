SELECT s.name FROM students s
JOIN marks m ON m.student_id = s.id
GROUP BY s.id, s.name HAVING MIN(m.score) > 85;