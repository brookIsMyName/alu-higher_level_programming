<!-- Describe the SQL introduction project and how to run its scripts. -->
# SQL Introduction

These exercises cover MySQL database and table creation, queries, inserts,
updates, deletions, filtering, sorting, and aggregation. They target MySQL
8.0.25.

Run the scripts from this directory. Use the MySQL client to select the
database for the table exercises.

```sh
mysql -u root -p < 1-create_database_if_missing.sql
mysql -u root -p hbtn_0c_0 < 4-first_table.sql
mysql -u root -p hbtn_0c_0 < 7-insert_value.sql
mysql -u root -p hbtn_0c_0 < 6-list_values.sql
```

Run `9-full_creation.sql` to create and populate `second_table` before
running scripts 10 through 16. Script 2 drops the exercise database.
