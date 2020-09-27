# Agent Selector
You are given the following data for agents <br>
agent :
* is_available
* available_since (the time since the agent is available)
* roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.) 

When an issue comes in we need to present the issue to 1 or many agents based on an agent selection mode. An agent selection mode can be all available, least busy or random. In “all available mode” the issue is presented to all agents so they pick the issue if they want. In least busy the issue is presented to the agent that has been available for the longest. In random mode we randomly pick an agent. An issue also has one or many roles (sales/support e.g.). Issues are presented to agents only with matching roles.

Implement a function that takes an input the list of agents with their data, agent selection mode and returns a list of agents the issue should be presented to.  

## Description
* Created a simple Django Web App to render a web UI for the problem
* Database used for storing Agents info - **sqlite**
* For viewing the Web App - <br>
Navigate to the Web App directory and type 
* **python manage.py makemigrations**
* **python manage.py migrate**
* **python manage.py runserver** in the terminal <br>

This will start the web app in the local server **127.0.0.1:8000/**.
Open the server and the home page of the web app will be started.