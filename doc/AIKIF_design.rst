====================
 AIKIF Design
====================
This document is a scratch pad area for design notes during the development of AIKIF

.. contents::


Mapper
------------------------------
The mapping class contains the business rules engine to control how information is passed

Mapper.py will be the main method to read the rules from CSV (or YAML) and apply them

A domain is a collection of rules and information that makes it easier to manage for humans entering the data. These include concepts such as ‘study, work, play’ or concrete things like ‘small business’, plumber, write a play, do food shopping.

A domain can get based on other domains so that it uses those rules and information - there can be many to many links, and collisions are listed and must be overridden. e.g. Plumber derives from Tradeskill and Small business



Mapping Hierarchies
``````````````
physics - rules that SHALL be obeyed according to natural law (eg drop something -> it will fall)
law - rules that are governed by law. e.g. All sales must be reported to IRS / ATO
generic - generic laws, eg Emails flagged spam > move to spam folder
profession specific - eg Software developers -> emails from RegNow are sales, carpenters -> profit = sale - (cost_wood + time + tool_wear)
situational - e.g. Work mode -> hide Reddit, Game mode -> turn off notifications, Sales mode -> ringer volume loud
[YOUR_MAPPING] = add all own mappings which if duplicated, override above

Domains (Mapping Examples)
------------------------------
The idea is to have everything mapped that you do in your world. A full ontology contains roughly 98% of items that do not appear in your horizon, so it is not infeasible to record the things YOU do.

Core Domains
``````````````
These are generic core domains that many other things are based on - they have presetup rules so you dont need to manually add everything.
Note that for these domains it might be easier to extract data from big ontology rather than type it all in 
Business - the act of running a business to make a profit
Project - doing something non trivial, pretty much everything can be a project
Student - the act of studying something to learn, test yourself, apply it, put on resume
Worker - A job. ie learning, using and implementing a tradeskill or degree to make money
Materials - things like wood, pipe, hard disk space that are needed to do a Task
Tools - anything that is needed or will help do a task
Tradeskill - a recognised group of skills, such as woodworking, plumber, programmer the uses physical tools and materials to produce things 
Task - in instance of a job to do - may involve materials, special tradeskills
Play - the act of relaxing. This is here to specify methods such as turn off phone, book holidays, close emails
Methods - functions that actually do something, which can be automated logged. Initially most methods are manual with links to doco, but it is still important to link them here so that they can be tracked on the web application and logged. In the future as methods are broken down you will be able to implement with python OR outsource to other people

Domain - Small business
``````````````
see examples in aikif - this is sort of a ROOT domain which many other things can be derived from
goal = make money, build reputation, sell business

how to get to the goal?
plan = build products, get customers, make sales, reduce costs

tasks (linked to goals) 
build products -> research competition, work out demand, prototype, test, manufacture
get customers -> plan campaign, write flyers, build website, social media, cold calling
make sales -> 
reduce costs -> rank expenses, 


methods (these are ACTUAL things the AI knows how to do which can assist automation)
Note that initially ALL the methods will default to ‘manual’ with a link to documentation, but eventually in some domains the automation rate can be reasonable (eg software deployment, data quality checking, estimating and quoting on woodwork jobs


tables (info) - this is where you store [LINKED to ontologies] information for your domain

Domain - Graphic Designer
``````````````
derives from small business
derives from artist

Domain - Carpenter
``````````````
derives from small business
derives from tradeskill


Bias
------------------------------
The Bias network has weightings based on sources which determine the probable accuracy of the source data


Agents
------------------------------
Agents are run to do the collection and aggregation of source data


Environments
------------------------------
This is a data structure which allows agents to run in worlds

Logging
------------------------------
This is the main part of AIKIF

