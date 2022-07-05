# QA-DevOps-Practical - 'Activity Generator' App:  
This GitHub repository contains my deliverable files for the QA DevOps pathway Core Practical Project.  

## Contents:
* [Project Requirements](#Project-Requirements)
* [Project Planning](#Project-Planning)
* [The App](#The-App)
* [Testing](#Testing)
* [CI Pipeline](#CI-Pipeline)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Requirements:
The project brief required me to create an application of my choosing which consists of four microservices. The microservices have to interact with each other using defined logic to generate objects. Further constraints are listed below:
* A Kanban board with full expansion on tasks needed to complete the project.
* A risk assessment outlining potential hazards with control measures and response actions.
* An Application fully integrated using the Feature-Branch model into a Version Control System (VCS) which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
* A Webhook should be used to automatically re-build and re-deploy the application through Jenkins when any changes are made and pushed to the VCS.
* The project must follow a Service-oriented architecture.
* The project must be deployed using containerisation and an orchestration tool.
* An Ansible Playbook must be created to provision the environment that the application needs to run.
* The project must make use of a reverse proxy.

### Constraints overview:
The tools I will use for each of the constraints are listed below:

* Kanban board: Trello
* Version Control: Git (GitHub) 
* CI server: Jenkins
* Configuration Manager: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX

## Project Planning:  
A Trello board was created to list and organise the objectives of the project. The inital Trello board is shown below:

![Trello Board](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/Trello1.png)

This was referred to and updated throughout the creation and documentation of the project in order to ensure no objectives were missed.  

The trello board can be accessed [HERE](https://trello.com/invite/b/pG5J7B15/6e0c56ff78baca453bc5671cec91ec8a/qa-project-2-trello) for in-depth viewing.  
  
Prior to beginning the project, a risk assessment was carried out. This was used to identify potential hazards, consider their implications and propose control measures for preventing/solving them. The risk assessment is shown below:

![Risk Assessment](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/Risk%20Assessment.png)

The outlined control measures were implemented during the creation of the project.  
The key included in the image explains the probability, impact and priority level of the potential hazards.

## The App
The application I have chosen to build is an Activity Generator tool.  
  
The purpose of this application is to choose a random activity from an array of activities and choose a random location from an array of cities.  
The end user of the application will be myself (The location costs are based on the area that I currently live).  
  
The application uses a microservice architecture, explained below:
* Service 1 - Front-End: This service creates and displays the part of the application that the user interacts with. It sends requests to the other services to generate a activity and location combination.
* Service 2 - Activity API: This service receives GET requests from service 1 and responds with a randomly selected activity from an array of activites. Each activity has a booking cost value associated with it.
* Service 3 - Location API: This service receives GET requests from service 1 and responds with a randomly selected location from an array of cities. Each location has a travel cost value associated with it.
* Service 4 - Cost API: This service receives POST requests from service 1, which provides the randomly generated activities and locations as JSON objects. Service 4 combines the activity and the location cost to be displayed as a total cost on the front-end
  
A reverse proxy via NGINX was implemented to listen on port 80  
  
The below image shows the front-end deployed via Jenkins, displayed via the external IP on port 80.

![Homepage](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/Homepage.png)

This is the page the user is directed to. It displays an activity, a location and the total cost.  
There is a 'New Activity' button which generates and displays a new combination and total cost each time it is pressed.  