# Agent Selector
You are given the following data for agents <br>
agent:
* is_available
* available_since (the time since the agent is available)
* roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.) 

When an issue comes in we need to present the issue to 1 or many agents based on an agent selection mode. An agent selection mode can be all available, least busy or random. In "all available mode" the issue is presented to all agents so they pick the issue if they want. In "least busy" the issue is presented to the agent that has been available for the longest. In "random mode" we randomly pick an agent. An issue also has one or many roles (sales/support e.g.). Issues are presented to agents only with matching roles.

Implement a function that takes an input the list of agents with their data, agent selection mode and returns a list of agents the issue should be presented to.  


## Description
Make sure to have git(https://git-scm.com/downloads) and python(https://www.python.org/downloads/) installed<br>
Download the project by git cloning either by one of the following ways-
* git clone https://github.com/SubhradeepSS/py-Agent-Query.git
* gh repo clone SubhradeepSS/py-Agent-Query

Open the project in any source code editor and follow the following steps.


### CLI Program
* Implemented python code for a CLI based interaction for the problem
* Used **pickle** to simulate as a simple database for storing Agents and their respective details
* To start the program, go to the **cli** directory and run the **main.py** script by typing **python main.py** in the terminal.

### Django Web App
* Created a simple Django Web App to render a web UI for the problem

* For viewing the Web App:
    * Install pip (if not already installed - https://pip.pypa.io/en/stable/installing/.)
    * Navigate to the **web** directory and install and Activate virtual environment (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
    * Inside the virtual environment, run **pip install -r requirements.txt**, which will install all the packages required for running the project.

* Type the following in the terminal(inside virtual environment):
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py createsuperuser (this will ask for username, email(optional) and password)
    * python manage.py runserver

* Log on to django admin site(http://127.0.0.1:8000/admin) using the superuser credentials and create some roles after opening the **Roles** section.

* Finally, open the http://127.0.0.1:8000/ link and the home page of the web-app will load.