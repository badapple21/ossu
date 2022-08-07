-- Keep a log of any SQL queries you execute as you solve the mystery.

-- this searches the crime scene reoprts for reports and july 28 in 2021
-- In the data base we see a report that states the the theft happned at the bakery and that the police got 3 interviews
SELECT * FROM crime_scene_reports  WHERE year = 2021 AND month = 7 AND day = 28;

-- this searches the crime scene reoprts for reports and july 28 in 2021
-- This tell us what the people said which was that they left within 10min they were at the atm withdraing early with Eugene they called someone and talked for less then a minute the were going o to leave town with the fist flight the next day
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;

-- this searches the bakery reoprts for reports and july 28 in 2021
-- We can start with possible plates they are
-- 5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28;

-- this gets the acount_number of Eugene which is 28579039
-- This allows us to see what tim Eugine was at the atm
SELECT * FROM bank_accounts WHERE person_id IN (SELECT id FROM people WHERE name = "Eugene");

-- 16153065, 25506511, 26013199, 28296815, 28500762, 49610011, 76054385, 81061156
--id 686048
--seat 4A
--passport 5773159633
-- name Bruce
--phone number (367) 555-5533
--des-4
--id 36

--phone number (375) 555-8161