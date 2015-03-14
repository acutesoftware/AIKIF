====================
 AIKIF Requirements
====================

This document describes the goals and requirements of AIKIF. 
Note that these are fluid and still very much a work in progress.

.. contents::




Overall Goals
=============
There are 4 main goals:
- Framework to collect and map information to knowledge
- Process Automation
- Control of Personal data
- AI monitoring 

Intentions
----------
The intention of AIKIF is to allow **all** of your information to be locally accessible, searchable and managed by yourself.
This includes the general high level information, processes and metadata around it, as well as the content of the data.

If everything is specified in a machine readable format, then rather than manually perform computer related tasks, the methods can be catalogued and structured so they can be automated.


Requirements
============
Goal 1 - Framework to collect and map information to knowledge
-----

map data to knowledge using your own rules
``````````````

store disparate data locally, backup globally
``````````````

understanding of bias to monitor data inputs and sources
``````````````

Goal 2 - Process Automation
-----
automatic documentation of program development
``````````````

Log intent, progress and outcomes of all AI / Data processing tasks.
``````````````

automatic collection, validation and processing of data
``````````````

Context Monitor
``````````````
watches what you do, where you are and automatically provides ALL info for that thing.
eg.. fixing a fence, driving to shops, working on AIKIF, reading reddit
Methods of detection
- Mobile GPS coords
- Ip address lookup
- Pc name (user list of locations)
- what is running. Pc / phone / tablet
- Apps running (agent collect)
- Folders / files used
- Pc usage

Then use an automated project clustering process combined with optional user defined list of mapping usage to projects to figure out what user was working on.


Goal 3 - Control of Personal data
-----
get your data off the cloud and under your control
``````````````

agents to download data from various cloud hosts and store locally
``````````````

index data locally for simple unified search across all sources (facebook, email, documents, photo metadata, web favourites)
``````````````

Goal 4 - AI monitoring (future)
-----
Define methods an AI can use (aikif.toolbox)
``````````````

Log all results with useful milestones and checkpoints
``````````````

Regulate processes to allow automation
``````````````

black box monitoring of unknown software agents
``````````````

Monitor for friendliness (unlikely to be achievable)
``````````````
