<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>pepperRestAPI</title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><p><strong>Pepper Task - TODO Rest API</strong></p>
<h2 id="list-all-todos"><strong>List All TODOs</strong></h2>
<p>Return JSON with all TODOs in the database</p>
<ul>
<li>
<p><strong>URL</strong></p>
<p>/TODOs/</p>
</li>
<li>
<p><strong>Method:</strong></p>
<p><code>GET</code></p>
</li>
<li>
<p><strong>URL Params</strong></p>
<p><code>None</code></p>
</li>
<li>
<p><strong>Data Params</strong></p>
<p><code>None</code></p>
</li>
<li>
<p><strong>Success Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong>  <code>200 OK</code></p>
<p><strong>Content:</strong>  <code>[ { "id": 2, "td_state": "I", "td_duedate": "2019-12-31", "td_text": "Updated Text" }, { "id": 4, "td_state": "D", "td_duedate": "2019-01-20", "td_text": "New text" }, { "id": 6, "td_state": "T", "td_duedate": "2019-01-22", "td_text": "Past due task" } ]</code></p>
</li>
</ul>
</li>
<li>
<p><strong>Error Response:</strong></p>
<p><code>None</code></p>
</li>
</ul>
<h2 id="create-one-or-more--todos"><strong>Create One or More  TODOs</strong></h2>
<p>Create one or more TODOs in the database from a JSON, and returns, in case of success, a JSON containing the created TODO with its ID</p>
<ul>
<li>
<p><strong>URL</strong></p>
<p>/TODOs/</p>
</li>
<li>
<p><strong>Method:</strong></p>
<p><code>POST</code></p>
</li>
<li>
<p><strong>URL Params</strong></p>
<p><code>None</code></p>
</li>
<li>
<p><strong>Data Params</strong></p>
<p><strong>Single creation</strong></p>
<p><code>{ "td_state" : "I|T|D" , "td_duedate" : "YYYY-MM-DD" , "td_text" : "Text of the TODO" }</code></p>
<p><strong>Multiple Creation</strong></p>
<p><code>[ { "td_state" : "I|T|D" , "td_duedate" : "YYYY-MM-DD" , "text" : "Text of the TODO #1" }, ... , { "td_state" : "I|T|D" , "td_duedate" : "YYYY-MM-DD" , "text" : "Text of the TODO #2" } ]</code></p>
</li>
<li>
<p><strong>Success Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong>  <code>201 CREATED</code></p>
<p><strong>Content:</strong>  <code>[ { "id": 49, "td_state": "T", "td_duedate": "2019-01-22", "td_text": "Meeting - Presentation" }, "id": 50, "td_state": "T", "td_duedate": "2019-01-30", "td_text": "Meeting - Presentation #2" } ]</code></p>
</li>
</ul>
</li>
<li>
<p><strong>Error Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong> <code>400 BAD REQUEST</code></p>
<p><strong>Content:</strong> <code>{ "message" : "It was not possible to proceed with TODO creation request" }</code></p>
</li>
<li>
<p><strong>Code:</strong> <code>422 UNPROCESSABLE ENTITY</code></p>
<p><strong>Content:</strong> <code>{ "message": "The state : Z informed does not exist. One or more TODOs could not have been created before." }</code></p>
</li>
<li>
<p><strong>Code:</strong> <code>422 UNPROCESSABLE ENTITY</code></p>
<p><strong>Content:</strong> <code>{ "message": "The Data Params informed could not be in a proper format. One or more TODOs could have been added before. See API documentation." }</code></p>
</li>
</ul>
</li>
</ul>
<h2 id="delete-a--one-or-more-todos"><strong>Delete a  One or More TODOs</strong></h2>
<p>Delete one or more TODOs from the database</p>
<ul>
<li>
<p><strong>URL</strong></p>
<p>/TODOs/:Id</p>
</li>
<li>
<p><strong>Method:</strong></p>
<p><code>DELETE</code></p>
</li>
<li>
<p><strong>URL Params</strong></p>
<p><code>Id=[integer]</code></p>
<p><em>Used exclusively if just one TODO is wanted to be deleted</em></p>
</li>
<li>
<p><strong>Data Params</strong></p>
<p><code>[ Id1, Id2, ..., Idn ]</code></p>
<p><em>Used if more than one TODOs are wanted to be deleted</em><br>
<em>Once a list is informed, it overrides the Id informed as URL Param</em></p>
</li>
<li>
<p><strong>Success Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong>  <code>202 ACCEPTED</code></p>
<p><strong>Content:</strong>  <code>{ "message": "TODO with id: 22 was deleted as per your request" }</code></p>
</li>
</ul>
</li>
<li>
<p><strong>Error Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong> <code>422 UNPROCESSABLE ENTITY</code></p>
<p><strong>Content:</strong> <code>{ "message": "The Data Params informed could not be in a proper format. See API documentation." }</code></p>
</li>
<li>
<p><strong>Code:</strong> <code>422 UNPROCESSABLE ENTITY</code></p>
<p><strong>Content:</strong> <code>{ "message": "TODO with id: 5 does not exist. One or more TODOs could have been deleted before." }</code></p>
</li>
<li>
<p><strong>Code:</strong> <code>422 UNPROCESSABLE ENTITY</code></p>
<p><strong>Content:</strong> <code>{ "message" : "It was not possible to proceed with TODO deletion request" }</code></p>
</li>
</ul>
</li>
</ul>
<h2 id="update-a-todo"><strong>Update a TODO</strong></h2>
<p>Update a TODO into the database and returns, in case of success a JSON containing the update TODO</p>
<ul>
<li>
<p><strong>URL</strong></p>
<p>/TODOs/:Id</p>
</li>
<li>
<p><strong>Method:</strong></p>
<p><code>PUT</code></p>
</li>
<li>
<p><strong>URL Params</strong></p>
<p><code>Id=[integer]</code></p>
</li>
<li>
<p><strong>Data Params</strong></p>
<p><code>{ "td_state": "T", "td_duedate": "2019-12-31", "td_text": "Updated Text" }</code></p>
</li>
<li>
<p><strong>Success Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong>  <code>202 ACCEPTED</code></p>
<p><strong>Content:</strong>  <code>{ "id": 23, "td_state": "T", "td_duedate": "2019-12-31", "td_text": "Updated Text" }</code></p>
</li>
</ul>
</li>
<li>
<p><strong>Error Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong> <code>422 UNPROCESSABLE ENTITY</code></p>
<p><strong>Content:</strong> <code>{ "message": "The Data Params informed could not be in a proper format. See API documentation." }</code></p>
</li>
<li>
<p><strong>Code:</strong> <code>422 UNPROCESSABLE ENTITY</code></p>
<p><strong>Content:</strong> <code>{ "message": "TODO with id: 5 does not exist." }</code></p>
</li>
<li>
<p><strong>Code:</strong> <code>422 UNPROCESSABLE ENTITY</code></p>
<p><strong>Content:</strong> <code>{ "message" : "It was not possible to proceed with TODO update request" }</code></p>
</li>
</ul>
</li>
</ul>
<h2 id="search-a-todo-by-id"><strong>Search a TODO by Id</strong></h2>
<p>Search a TODO in the database by its Id and return a JSON of the TODO found</p>
<ul>
<li>
<p><strong>URL</strong></p>
<p>/TODOs/:Id</p>
</li>
<li>
<p><strong>Method:</strong></p>
<p><code>GET</code></p>
</li>
<li>
<p><strong>URL Params</strong></p>
<p><code>Id=[integer]</code></p>
</li>
<li>
<p><strong>Data Params</strong></p>
<p><code>None</code></p>
</li>
<li>
<p><strong>Success Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong>  <code>200 OK</code></p>
<p><strong>Content:</strong>  <code>{ "id": 2, "td_state": "I", "td_duedate": "2019-12-31", "td_text": "Updated Text" }</code></p>
</li>
</ul>
</li>
<li>
<p><strong>Error Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong> <code>404 NOT FOUND</code></p>
<p><strong>Content:</strong> <code>{ "message": "TODO with id: 9 does not exist" }</code></p>
</li>
</ul>
</li>
</ul>
<h2 id="search-todos-by-state"><strong>Search TODOs by State</strong></h2>
<p>Search all TODOs in the database with a State and return a JSON with them</p>
<ul>
<li>
<p><strong>URL</strong></p>
<p>/TODOs/state/:State</p>
</li>
<li>
<p><strong>Method:</strong></p>
<p><code>GET</code></p>
</li>
<li>
<p><strong>URL Params</strong></p>
<p><code>State=[char]</code></p>
</li>
<li>
<p><strong>Data Params</strong></p>
<p><code>None</code></p>
</li>
<li>
<p><strong>Success Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong>  <code>200 OK</code></p>
<p><strong>Content:</strong>  <code>[ { "id": 4, "td_state": "D", "td_duedate": "2019-01-20", "td_text": "New text" }, { "id": 43, "td_state": "D", "td_duedate": "2019-01-22", "td_text": "Niver" } ]</code></p>
</li>
</ul>
</li>
<li>
<p><strong>Error Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong> <code>404 NOT FOUND</code></p>
<p><strong>Content:</strong> <code>{ "message": "There isn't any TODO with the state : T" }</code></p>
</li>
<li>
<p><strong>Code:</strong> <code>404 NOT FOUND</code></p>
<p><strong>Content:</strong> <code>{ "message": "The state : Z searched does not exist" }</code></p>
</li>
</ul>
</li>
</ul>
<h2 id="search-todos-by-duedate"><strong>Search TODOs by Duedate</strong></h2>
<p>Search all TODOs in the database with a Duedate and return a JSON with them</p>
<ul>
<li>
<p><strong>URL</strong></p>
<p>/TODOs/duedate/:Duedate</p>
</li>
<li>
<p><strong>Method:</strong></p>
<p><code>GET</code></p>
</li>
<li>
<p><strong>URL Params</strong></p>
<p><code>Duedate=[char]</code></p>
<p><em>Obs - The date format shall be ‘YYYY-MM-DD’</em></p>
</li>
<li>
<p><strong>Data Params</strong></p>
<p><code>None</code></p>
</li>
<li>
<p><strong>Success Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong>  <code>200 OK</code></p>
<p><strong>Content:</strong>  <code>[ { "id": 50, "td_state": "D", "td_duedate": "2019-04-30", "td_text": "Meeting #1" }, { "id": 51, "td_state": "D", "td_duedate": "2019-04-30", "td_text": "Meeting #2" } ]</code></p>
</li>
</ul>
</li>
<li>
<p><strong>Error Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong> <code>404 NOT FOUND</code></p>
<p><strong>Content:</strong> <code>{ "message": "TODO with duedate: 2100-01-01 does not exist" }</code></p>
<ul>
<li><strong>Code:</strong> <code>404 NOT FOUND</code></li>
</ul>
<p><strong>Content:</strong> <code>{ "message": "Duedate: 2019-09-80 informed is not in a valid format. See API Documentation." }</code></p>
</li>
</ul>
</li>
</ul>
<h2 id="search-todos-by-state-andor-duedate"><strong>Search TODOs by State <em>and/or</em> Duedate</strong></h2>
<p>Search all TODOs in the database with a Duedate and return a JSON with them</p>
<ul>
<li>
<p><strong>URL</strong></p>
<p>/TODOs/search/:State/:Oper/:Duedate</p>
</li>
<li>
<p><strong>Method:</strong></p>
<p><code>GET</code></p>
</li>
<li>
<p><strong>URL Params</strong></p>
<p><code>State=[char]</code><br>
<code>Oper=[char]</code><br>
<code>Duedate=[char]</code></p>
<p><em>Oper = “and” | “or”</em><br>
<em>The date formar shall be ‘YYYY-MM-DD’</em></p>
</li>
<li>
<p><strong>Data Params</strong></p>
<p><code>None</code></p>
</li>
<li>
<p><strong>Success Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong>  <code>200 OK</code></p>
<p><strong>Content:</strong>  <code>[ { "id": 2, "td_state": "T", "td_duedate": "2019-04-11", "td_text": "Meeting2" }, { "id": 4, "td_state": "D", "td_duedate": "2019-04-11", "td_text": "Code Review" } ]</code></p>
</li>
</ul>
</li>
<li>
<p><strong>Error Response:</strong></p>
<ul>
<li>
<p><strong>Code:</strong> <code>404 NOT FOUND</code></p>
<p><strong>Content:</strong> <code>{ "message": "TODO with state : I and duedate: 2029-04-11 does not exist" }</code></p>
</li>
<li>
<p><strong>Code:</strong> <code>404 NOT FOUND</code></p>
<p><strong>Content:</strong> <code>{ "message": "The TODO state Z searched does not exist" }</code></p>
</li>
<li>
<p><strong>Code:</strong> <code>404 NOT FOUND</code></p>
<p><strong>Content:</strong> <code>{ "message": "Operator : foo is not permited" }</code></p>
</li>
</ul>
</li>
</ul>
</div>
</body>

</html>
