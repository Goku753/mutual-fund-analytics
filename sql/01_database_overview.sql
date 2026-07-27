-- Show all tables
SELECT name
FROM sqlite_master
WHERE type='table';

-- Total tables
SELECT COUNT(*) AS total_tables
FROM sqlite_master
WHERE type='table';