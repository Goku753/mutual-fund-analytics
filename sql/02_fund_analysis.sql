-- Total Funds
SELECT COUNT(*) AS total_funds
FROM "01_fund_master";

-- Fund Houses
SELECT COUNT(DISTINCT fund_house) AS total_fund_houses
FROM "01_fund_master";

-- List Fund Houses
SELECT DISTINCT fund_house
FROM "01_fund_master"
ORDER BY fund_house;

-- Category Distribution
SELECT
category,
COUNT(*) AS schemes
FROM "01_fund_master"
GROUP BY category
ORDER BY schemes DESC;

-- Top Fund Houses
SELECT
fund_house,
COUNT(*) AS schemes
FROM "01_fund_master"
GROUP BY fund_house
ORDER BY schemes DESC;