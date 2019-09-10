# Flask Backend

### Requirements

- python version 3.x
- pip
- [Postman](https://www.getpostman.com/)

Installation instructions for [Mac](https://github.com/hack4impact-uiuc/wiki/wiki/Mac-Setup) and [Windows](https://github.com/hack4impact-uiuc/wiki/wiki/Windows-Subsystem-for-Linux-Setup#setting-up-python).

Another great resource for anything on python, including installation is [The Hitchhiker's guide to python](https://docs.python-guide.org/).

Check if you have the correct versions by running the following commands in your terminal (if you don't have Python2 installed, you may need to replace python3 with python and pip3 with pip):

```
python3 -V
```

```
pip3 -V
```

### Setup

First, setup your virtual environment and install the python dependencies required to run this app. We're using virtualenv, which is a virtual Python environment isolated from other Python projects, incapable of interfering with or being affected by other Python programs on the same machine. You are thus capable of running different versions of the same package or even different python versions. In the backend directory, run the following commands:

```
pip3 install --user virtualenv
virtualenv -p python3 venv
```

You must be in this virtual environment to install dependencies and start this server. Once you do this, you will see `(venv)` preceding your prompts. To do thit:

```
source venv/bin/activate
```

Then to install dependencies, run:

```
pip install -r requirements.txt
```

Then, to start the server run:

```
python app.py
```

Note: This will remain a running process in your terminal, so you will need to open a new tab or window to execute other commands.

To stop the server, press `Control-C`.

To exit your virtual environment, run:

```
deactivate
```

### Overview

These exercises will walk you through creating a RESTful API using Flask! We don't want you to go through all the hassle of setting up a database instance, so we have created dummy data and a mock database interface to interact with it. For the sake of ease, the entire app logic minus the mockdb logic will by implemented in `app.py`. For larger projects, the API endpoints will usually be separated out into different files called `views`.

Before you start, take a good look at the `create_response` function and how it works. Make sure you follow the guidelines for how to use this function, otherwise your API will not follow the proper conventions!

Also take a look into the mock database. The initial dummy data is defined in `mockdb/dummy_data.py`. This is what will "exist" in the "database" when you start the server.

The functions defined in `mockdb/mockdb_interface.py` are how you can query the mockdb. In `app.py`, where you will be writing your API, this has been imported with the name `db`. Therefore when you write the code for your endpoints, you can call the db interface functions like `db.get('shows')`.

When you modify your code, the server will automatically update, _unless_ your code doesn't compile, in which case the server will stop running and you have to manually restart it after fixing your code.

For instructions on completing the exercise, look at the [README.md](../README.md) in the main directory.