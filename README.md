# tournament-project
Udacity Tournament Project

## Included Files
 * tournament.sql - Table and View definitions which implement the tournament project including all extra credit.
 * tournament.py - Python API implementation, modified to cater for all extra credit.
 * tournament_test.py - Python file containing all test cases, including all extra credit.
 * README.md - this file.

## SQL Standards
* Tables are prefixed with 't_'.
* Views are prefixed with 'v_'.
* Indices are prefixed with 'i_'.
* "SELECT 1" is used in exists clause so the whole row isn't returned to the sub-query (better performance).
* COALESCE is used to make sure NULL's from left outer joins are counted as zeroes correctly.
* CASE statements are used to convert the existence of a value into a numeric values for SUM's
