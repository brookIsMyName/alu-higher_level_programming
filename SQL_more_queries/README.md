<!-- Describe the SQL exercises and how to run them. -->
# SQL More Queries

These exercises target MySQL 8.0.25 and cover user privileges, constraints,
subqueries, joins, and grouped counts.

Run scripts 1 and 2 with an administrative account to create the exercise
users. Run script 0 to display their grants. Scripts 3 through 5 use the
database selected on the MySQL command line.

Scripts 6 and 7 create the states and cities tables in `hbtn_0d_usa`.
Populate those tables before running scripts 8 and 9. Import the course
`hbtn_0d_tvshows.sql` dump into `hbtn_0d_tvshows` for scripts 10 through 16.

```sh
mysql -u root -p < 2-create_read_user.sql
mysql -u root -p hbtn_0d_2 < 3-force_name.sql
mysql -u root -p < 7-cities.sql
mysql -u root -p hbtn_0d_usa < 9-cities_by_state_join.sql
mysql -u root -p hbtn_0d_tvshows < 16-shows_by_genre.sql
```
