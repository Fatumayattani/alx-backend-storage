-- Stored Procedure Script (6-bonus.sql)
DELIMITER $$
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(
    IN `user_id` INTEGER,
    IN `project_name` VARCHAR(255),
    IN `score` INTEGER
)
BEGIN
    INSERT INTO projects (name)
    SELECT project_name
    WHERE project_name NOT IN (SELECT name FROM projects);

    INSERT INTO corrections (user_id, project_id, score)
    VALUES(user_id, (SELECT id FROM projects WHERE name = project_name), score);
END $$
DELIMITER ;$$
