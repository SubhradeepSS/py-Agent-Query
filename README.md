<br />
<p align="center">
  <h3 align="center">py-Agent-Query</h3>

  <p align="center">
    A CLI based program in Python along with a Django application, for selecting agents for incoming issues based on different factors. 
    <br />
    <br />
    <a href="https://github.com/SubhradeepSS/py-Agent-Query"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#local">Local</a></li>
        <li><a href="#deployment">Deployment</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
You are given the following data for agents
* is_available
* available_since (the time since the agent is available)
* roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.) 

When an issue comes in we need to present the issue to 1 or many agents based on an agent selection mode. An agent selection mode can be all available, least busy or random. 
* In "all available mode" the issue is presented to all agents so they pick the issue if they want. 
* In "least busy" the issue is presented to the agent that has been available for the longest. 
* In "random mode" we randomly pick an agent. An issue also has one or many roles (sales/support e.g.).

Issues are presented to agents only with matching roles.

Implement a function that takes an input the list of agents with their data, agent selection mode and returns a list of agents the issue should be presented to.  

<br/>

**CLI Program:**
Implemented python code for a CLI based interaction for the problem. Used [pickle](https://docs.python.org/3/library/pickle.html) to simulate as a simple database for storing Agents and their respective details.

**Django Web App**:
Created a simple Django Web App to render a web UI for the problem.

### Built With
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)


<!-- GETTING STARTED -->
## Getting Started
To setup the project locally, follow the given steps:

### Prerequisites
Following software needs to be setup in the system
* [git](https://git-scm.com/downloads)
* [python](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [python virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)  (optional)
* [github-cli](https://github.com/cli/cli) (optional)

### Installation

1. Clone the repo by
   ```sh
   git clone https://github.com/SubhradeepSS/py-Agent-Query.git
   ```
   or (if [github-cli](https://github.com/cli/cli) is installed)
   ```sh
   gh repo clone SubhradeepSS/py-Agent-Query
   ```
2. Open the project in any source code editor.

##### CLI Program
1. Navigate to the **cli** directory and start the cli program by running in terminal the following command:
    ```sh
    python main.py
    ```
##### Django Web App
1. Navigate to the **web** directory.
2. Activate python virtual environment (see here for [reference](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments))
3. Inside the virtual environment, run
   ```sh
   pip install -r requirements.txt
   ```



<!-- USAGE EXAMPLES -->
## Usage
##### CLI Program
The CLI Program will start once the ```main.py``` script is activated and will start interacting with the user.

##### Django Web-App
For running the project, navigate to the **web** directory and follow the given instructions:

* Type the following in the command line(inside the virtual environment):
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    # this will ask for username, email(optional) and password. Enter some credentials to be used later for django admin functionality.
    python manage.py runserver
  ```
* Log on to [django admin site](http://127.0.0.1:8000/admin) using the superuser credentials and create some roles after opening the **Roles** section.

* Finally, open the http://127.0.0.1:8000/ link and the home page of the web-app will load.


<!-- CONTRIBUTING -->
## Contributing
Any contributions made to the project are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
