### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  * PostgreSQL is an open-source object-relational database system

- What is the difference between SQL and PostgreSQL?
  * SQL is a database management system. PostgreSQL is an advanced database management system which provides support to different functions of SQL

- In `psql`, how do you connect to a database?
  * \c <database name>

- What is the difference between `HAVING` and `WHERE`?
  * WHERE filters the query itself, whereas HAVING tells the GROUP BY which results to show + how to show them

- What is the difference between an `INNER` and `OUTER` join?
 * INNER join returns only the results that match the condition in both tables. OUTER will take all rows from one table (or both if FULL) and the matching rows from the other.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  * LEFT OUTER will return all results from the first table combined with matching results from second table.
  * RIGHT OUTER will return all results from the second table combined with matching results from the first table

- What is an ORM? What do they do?
  * Object=Relational Mapping - lets you query and manipulate data from a database using an object-oriented paradigm.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  * AJAX
    * client-side origin
    * server has no knowledge of results
    * Can be manipulated by an attacker
  * Requests
    * Server-side origin
    * client has no knowledge of results
    * can validate/filter response before passing to client

- What is CSRF? What is the purpose of the CSRF token?
  * CSRF (Cross Site Request Forgery) Token
    * A secret, unique, unpredictable value as a server-side application generates in order to protect CSRF vulnerable resources.

- What is the purpose of `form.hidden_tag()`?
  * To include the CSRF token in the HTTP request sent from the client. the hidden input for the CSRF token in included in the html for the form.
