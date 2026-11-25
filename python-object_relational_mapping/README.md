#!/usr/bin/python3

# Python Object-Relational Mapping

Scripts 0 through 5 query MySQL with MySQLdb. Scripts 7 through 14 use
SQLAlchemy ORM models from `model_state.py` and `model_city.py`.

The project targets Python 3.8, MySQL 8.0, mysqlclient 2.0.x, and
SQLAlchemy 1.4.x. Load the exercise schema and sample data before running
the scripts. Pass the MySQL username, password, and database name in that
order. Filtering scripts also take the state name.

```sh
./0-select_states.py root root hbtn_0e_0_usa
./3-my_safe_filter_states.py root root hbtn_0e_0_usa Arizona
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
```

Import both model modules before creating both tables with
`Base.metadata.create_all(engine)`.
