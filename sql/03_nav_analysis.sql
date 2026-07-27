-- Latest NAV

SELECT *
FROM "02_nav_history"
ORDER BY date DESC
LIMIT 20;

-- Highest NAV

SELECT *
FROM "02_nav_history"
ORDER BY nav DESC
LIMIT 10;

-- Lowest NAV

SELECT *
FROM "02_nav_history"
ORDER BY nav ASC
LIMIT 10;

-- Average NAV

SELECT AVG(nav)
FROM "02_nav_history";