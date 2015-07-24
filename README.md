# tournament-project
Udacity Tournament Project

I have chosen to implement all extra credit features and test cases.

**Included Files**
 * `tournament.sql` - Table and View definitions which support the tournament API
 * `tournament.py` - Python Tournament API
 * `tournament_test.py` - Python file containing all test cases.
 * `README.md` - this file.

**SQL Standards**
 * Tables are prefixed with 't_'.
 * Views are prefixed with 'v_'.
 * Indices are prefixed with 'i_'.
 * "SELECT 1" is used in exists clause so the whole row isn't returned to the sub-query (better performance).
 * COALESCE is used to make sure NULL's from left outer joins are counted as zeroes correctly.
 * CASE statements are used to convert the existence of a value into a numeric values for SUM's

**Usage**
Load the DB Schema provided in tournament.sql into PSQL
```
psql -f tournament.sql
```
Execute the provided test cases to validate API.
```
python tournament_test.sql
```
