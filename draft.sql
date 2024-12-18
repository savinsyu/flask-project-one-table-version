CREATE TABLE [main] (
  [id] INTEGER AUTO_INCREMENT NULL,
  -- Команда
  [name] TEXT NOT NULL,
  -- Описание команды
  [description] TEXT NOT NULL,
  -- Категория записи(html, css, python ...)
  [category] TEXT NOT NULL,
  [date_add] TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  [date_edit] TEXT NULL,
  PRIMARY KEY ([id])
);

-- Перенос значений определенных полей одной таблицы в другую
INSERT INTO
  main (name, description, category, date_add, date_edit)
SELECT
  python_command,
  python_name,
  'python',
  datetime('now'),
  ''
FROM
  python;
DROP TABLE python;
-- Перенос значений полей одной таблицы в другую
INSERT INTO
  main
SELECT
  bash_id,
  bash_command,
  bash_name,
  'cli',
  datetime('now'),
  ''
FROM
  bash;
DROP TABLE table_example;
DELETE FROM
  table_example;
SELECT
  *
FROM
  table_example;
DROP TABLE table_example;
SELECT
  *
FROM
  sql;