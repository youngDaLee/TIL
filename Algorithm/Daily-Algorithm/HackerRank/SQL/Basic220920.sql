-- Revising the Select Query 1
-- https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
SELECT *
FROM CITY
WHERE POPULATION > 100000
  AND CountryCode = 'USA';

-- Revising the Select Query 2
-- https://www.hackerrank.com/challenges/revising-the-select-query-2/problem?isFullScreen=true
SELECT NAME
FROM CITY
WHERE POPULATION > 120000
  AND CountryCode = 'USA';

-- Japanese Cities' Attributes
-- https://www.hackerrank.com/challenges/japanese-cities-attributes/problem?isFullScreen=true
SELECT *
FROM CITY
WHERE COUNTRYCODE ='JPN';

-- Japanese Cities' Names
-- https://www.hackerrank.com/challenges/japanese-cities-name/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'JPN';

-- SELECT ALL
SELECT * FROM CITY;

-- SELECT BY ID
-- https://www.hackerrank.com/challenges/select-by-id/problem?isFullScreen=true
SELECT *
FROM CITY
WHERE ID=1661;

-- Weather Observation Station 1
-- https://www.hackerrank.com/challenges/weather-observation-station-1/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
SELECT CITY, STATE
FROM STATION;

-- Weather Observation Station 3
-- https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zenSELECT CITY, STATE
SELECT DISTINCT CITY
FROM STATION
WHERE ID%2=0;
