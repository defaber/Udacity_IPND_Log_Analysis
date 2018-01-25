# Project Log Analysis
## Project Overview

This project uses tools like vagrant, VirtualBox, Python, and PostgreSQL on a Linux VM. The objective is to cipher though the data inside the database “news”.  From there we will need to answer three questions.  

Those questions being:
1. What are the most popular three articles of all time?

2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?

This final project will test our ability to retrieve data within a database using SQL and Python through the means of a Python DB-API

## How to Run

A few things you’ll need in order to run this program:
- VirtualBox
- Vagrant
- [VM](https://github.com/udacity/fullstack-nanodegree-vm.) from Udacity
- [Newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Once all four of these are downloaded.  Vagrant will need brought up with the following commands:

`vagrant up`

`vagrant ssh`

To load the data, change directory `cd` into the vagrant directory that is shared between the user pc and the vm then use command `psql -d news -f newsdata.sql`

The news database consists of three tables that we’ll be examining:

1. The authors table includes information about the authors of articles.

2. The articles table includes the articles themselves.

3. The log table includes one entry for each time a user has accessed the site.

To execute the python code: inside the VM, from the command line run `python log.py`
