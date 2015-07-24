# tournament-project
Udacity Tournament Project

I have chosen to implement all extra credit features and test cases.

## Included Files
 * `tournament.sql` - Table and View definitions which support the tournament API
 * `tournament.py` - Python Tournament API
 * `tournament_test.py` - Python file containing all test cases.
 * `README.md` - The README file used for display on GitHub, contains usage.
 * `LICENSE.md` -

## SQL Standards
 * Tables are prefixed with 't_'.
 * Views are prefixed with 'v_'.
 * Indices are prefixed with 'i_'.
 * 'SELECT 1' is used in exists clause so the whole row isn't returned from 
   sub-query, which can result in better performance.
 * COALESCE is used to make sure NULL's from left outer joins are counted as
   zeroes correctly.
 * CASE statements are used to convert the existence of a value into a numeric
   values for SUM's

## Usage
Load the DB Schema provided in tournament.sql into PSQL
```
psql -f tournament.sql
```
Execute the provided test cases to validate API.
```
python tournament_test.sql
```

## References
* [Wizards of the Coast](http://www.wizards.com/dci/downloads/swiss_pairings.pdf)
* [tsh: Pairing Theory](http://www.poslarchive.com/math/software/tsh/doc/pairing.html#swiss)
* [SQL - NTILE examples](http://sqlandme.com/2011/06/30/sql-functions-ntile/)
* [Wikipedia - Swiss Tournament System](https://en.wikipedia.org/wiki/Swiss-system_tournament#Final_scores_and_tie-breaking)
