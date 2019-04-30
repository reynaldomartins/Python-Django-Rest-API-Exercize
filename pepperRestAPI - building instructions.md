<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>pepperRestAPI - building instructions</title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><p>The TODO Rest API was build as a task demanded by Pepper Esports Inc.</p>
<p>Python version used - 3.7<br>
Database - sqlite<br>
GitHub Repository - <a href="https://github.com/reynaldomartins/pepperRestProj">https://github.com/reynaldomartins/pepperRestProj</a></p>
<p>General Instructions to Setup the API :</p>
<ul>
<li>Download all files from the root of the repository
<ul>
<li><em>remarks - “.gitinore” file was not update on time. It can happen that some files would be downloaded from GitHub which will not be used or will be updated after the migrations are executed and some other executions</em></li>
</ul>
</li>
<li>The project used pipenv, therefore, build the environment using Pipfile and Pipfile.lock which can be found in the repository root. The following installations shall run at your server which are necessary to run the API :
<ul>
<li>django</li>
<li>djangorestframework</li>
<li>django-cors-headers</li>
</ul>
</li>
<li>At pepperAPIProj dir, update <a href="http://settings.py">settings.py</a>, adding the host of the   server where the API will run, at ALLOWED_HOST list</li>
<li>Run the migrations and set the admin password
<ul>
<li>$ python <a href="http://manage.py">manage.py</a> migrate</li>
<li>$ python <a href="http://manage.py">manage.py</a> createsuperuser --email <a href="mailto:xxxx@yyyy.com">xxxx@yyyy.com</a> --username admin</li>
<li>$ python <a href="http://manage.py">manage.py</a> makemigrates pepperRestApp</li>
<li>$ python <a href="http://manage.py">manage.py</a> migrate</li>
</ul>
</li>
</ul>
<p>Runing the Tests ($ python <a href="http://manage.py">manage.py</a> test)</p>
<ul>
<li>The test batch includes 7 different test cases.</li>
<li>In each test cases more than 1 scenario can be run.</li>
<li>The test cases were build aimed to test regular situations as well as well as force some errors.</li>
<li>For each test cases is printed in the console the messages related to the response from the API</li>
<li>The database is presented before and after the test cases for those situtions where the data are modified.</li>
<li>There will be 3 failures messages regarding assertions done for using wrong data search keys.</li>
</ul>
<p>Activate the API to be accessed from a front-end ($python <a href="http://manage.py">manage.py</a> runserver)</p>
<p><em>The API were tested also using Google Chrome whenever the scenario permited inputs through the URL</em></p>
<p>The API documentation is at <a href="https://github.com/reynaldomartins/pepperRestProj/blob/master/pepperRestAPI.md">https://github.com/reynaldomartins/pepperRestProj/blob/master/pepperRestAPI.md</a></p>
<p>API further developments to be done</p>
<ul>
<li>In the case if creation or deletion of TODOs from a list fails, a   mechanism of roll-back shall be implemented, postponing the commit in the database until the moment all updates happen successfuly</li>
</ul>
<p>Runing the Tests On Line (JS React Front End)</p>
<ul>
<li>For the purpose of testing the API on-line, a very simple front-end were created using Node,js/React.</li>
<li>The programs can be obtained from GitHiub at <a href="https://github.com/reynaldomartins/pepperreactproj">https://github.com/reynaldomartins/pepperreactproj</a></li>
<li>The programa index.js at “src” directory shall be modified in order to call the domain where the API will be installed.
<ul>
<li>The following variable shall be modified (this.apiDomain = “<a href="https://956e8277.ngrok.io/">https://956e8277.ngrok.io/</a>”)</li>
</ul>
</li>
<li>All scenarios of the API methods can be tested, except creation and deletion of TODOs based on a list.</li>
<li>For each scenario, a response from the API will be shown (which can be a list of TODOs in a table or a confirmation or error message). The URL Params and Data Params of each call is shown also.</li>
<li>Known Error - It was not possible to handle and fix on time a crash in the program when a search key is informed as a string of one or more spaces. It crashes in the fetch function in the JS side.</li>
</ul>
</div>
</body>

</html>
