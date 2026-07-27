-- Which fund house has the highest number of schemes?

SELECT
fund_house,
COUNT(*) AS total
FROM "01_fund_master"
GROUP BY fund_house
ORDER BY total DESC
LIMIT 1;

-- Which category has the highest number of schemes?

SELECT
category,
COUNT(*) AS total
FROM "01_fund_master"
GROUP BY category
ORDER BY total DESC
LIMIT 1;

-- Total NAV Records

SELECT COUNT(*)
FROM "02_nav_history";