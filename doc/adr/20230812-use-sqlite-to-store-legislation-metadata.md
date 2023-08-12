# Use SQLite to store legislation metadata

- Status: [accepted]
- Deciders: [Anabelle]

## Context and Problem Statement

I need some way to persistently store metadata about the current state of bills, committes, representatives, etc.


## Considered Options

- [SQLite]
- [Postgres]
- Plaintext [JSON] files
- [MariaDB] / [MySQL]


## Decision Outcome

I chose SQLite for a number of reasons:

- Using SQL seems like a no-brainer: The relationships between bills/representatives, reps/committees, and reps/constituents are complex. Storing them in JSON would require arrays of doubly-linked json objects.

- Storing a whole database as an ever-expanding plaintext JSON file feels hacky.

- Using a language-specific storage method like Python's [pickle]

- Client/Server DBMS Platforms add a decent bit of complexity:

  - Anyone wanting to run a fork has to stand up an SQL server

  - I'd have to keep track of login credentials & make sure they don't get uploaded to git.

  - The SQL server has to be kept up-to-date

### Positive Consequences <!-- optional -->

- Less complexity: SQLite allows us to use SQL without setting up / maintaining too many moving parts.
- Data Integrety: SQLite has lots of safeguards[^1] [^2] [^3] in place to prevent data corruption
- Easy Backups: SQLite databases reduce to a single file, which makes backups dead simple

### Negative Consequences <!-- optional -->

- Scalability: We're kindof limited to a single VM with SQLite. We'd have to migrate our database to MariaDB / MySQL / PosgreSQL if we ever want to deploy multiple VMs

- Onboarding: Some self-taught coders may not have learned SQL. This decreases the number of people who can maintain the project, which is important in a small group.

### External Links:
<https://sqlbolt.com/> - An interactive tutorial to SQL



[SQLite]: https://www.sqlite.org/index.html
[Postgres]: https://www.postgresql.org/
[MariaDB]: https://mariadb.org/
[MySQL]: https://www.mysql.com/
[JSON]: https://json.org/
[pickle]: https://docs.python.org/3/library/pickle.html
[^1]:https://www.sqlite.org/testing.html
[^2]:https://www.sqlite.org/howtocorrupt.html
[^3]:https://www.sqlite.org/atomiccommit.html