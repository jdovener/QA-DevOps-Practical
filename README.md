# QA-DevOps-Practical - 'Activity Generator' App:  
This GitHub repository contains my deliverable files for the QA DevOps pathway Core Practical Project.  

## Contents:
* [Project Requirements](#Project-Requirements)
* [Project Planning](#Project-Planning)
* [The App](#The-App)
* [Testing](#Testing)
* [CI Pipeline](#CI-Pipeline)
* [Updates](#Updates)
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
  
The below image shows the front-end deployed via Jenkins, displayed via a Docker Swarm VM external IP on port 80.

![Homepage](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/Homepage.png)

This is the page the user is directed to. It displays an activity, a location and the total cost.  
There is a 'New Activity' button which generates and displays a new combination and total cost each time it is pressed.  

# Testing

Unit testing is used to verify that individual aspects of the app function correctly. 

Pytest was used to conduct the unit testing. Below is an image of a pytest test session showing 15 tests passing successfully. The below coverage reports show each of the 4 services being tested and passing.

![Coverage1](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/Coverage1.png)
![Coverage2](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/Coverage2.png)  
  
In order to run these tests manually, I use a terminal to navigate to a service within the project. I then run the following command:  
  
```
python3 -m pytest --cov --cov-report term-missing
```
  
This command runs pytest on any files beginning with the word 'test'. It also makes the terminal produce a coverage report to show what percentage of the code has been covered. It is important to aim for 100% coverage to ensure everything works as intended. If areas of code have not been covered by the test, the 'term-missing' argument will provide the user with details of which file the missed code is in and which lines the missed code occupies.  
  
I appended the output of the command used in each of the services to a text file to compile the outputs and produce the above images.  
  
However, the project is now set up to automatically conduct tests via Jenkins every time a push is made to the GitHub repository.  

# CI Pipeline

One of the project constraints required the project to implement a CI pipeline. The stages of this pipeline include: project tracking, version control, development environment, CI server and Deployment environment.  
  
For project tracking, trello was used to create a tracking board. Examples of this and access to the trello board can be found in the [Project Design](#Project-Design) section of this README document.  
  
Git was used for the version control stage of the pipeline. The project repository was hosted on GitHub. Using Git allows for the project to be built incrementally and saves a history of all previous commits. These previous commits can be rolled back to in the event of errors to allow access to previous versions of the project.  
  
A Python3 virtual environment (venv) was used as a development environment. This was hosted on a virtual machine (on Google Cloud Platform) running Ubuntu 20.04. A venv allows for seperation of concerns meaning pip installs can be performed without affecting any conflicting pip installs within the same machine.  
  
Jenkins was used as a build server in order to automate the tests, the various build steps and deployment. This is achieved by creating a pipeline project via Jenkins, the project anisble and Docker Swarm to deploy the application. A webhook is used to continuously integrate changes whenever a commit is pushed to the GitHub Repository.  
  
Below is an image of the Jenkins stage view. If any stage fails, the subsequent stages will not continue until the issues is fixed. If all stages pass, there are no errors and the application is deployed to the Docker Swarm virtual machines' external IP address.  

![Jenkins Build](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/Jenkins%20Build.png)
  
Upon pushing a commit to the GitHub repo, a webhook activate the Jenkins pipeline project, which handles the following steps:
1. Runs unit tests for each of the 4 services
2. Runs the Ansible playbook, which installs relevant docker packages (See below images for further explanation)
3. Removes any existing images (this is to ensure the VM's memory does not fill up, thus making the Jenkins build idempotent)
4. Builds the service's images via docker-compose
5. Logs into DockerHub using Jenkins credentials and pushes the images to my DockerHub account
6. Copies the docker-compose.yaml file and the nginx.conf file to the Docker swarm manager VM and deploys the application from there
  
As mentioned in step 2 of the Jenkins pipeline project, the Ansible playbook is run as part of the pipeline. Below is an image of the initial execution of the Ansible playbook, connecting the project to the Docker Swarm manager and worker.

![Playbook1](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/Playbook1.png)

Once this has been executed, all subsequent executions will result in the IPs being shown as green in the terminal output. See the below image for illustration.
  
![playbook2](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/playbook2.png)
  
The purpose of using Docker Swarm is to automatically load balance the various services across the swarm VMs. The two VMs are shown in the below image  

![DockerVMS](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/DockerVMS.png)
  
The below image illustrates the structure of the CI/CD pipeline:

![Infrastructure](https://github.com/jdovener/QA-DevOps-Practical/blob/dev/images/Infrastructure.png)

# Updates
* 04/07/2022
    * Functional app has been created and containerised
    * Basic styling has been added

* 05/07/2022
    * Code has been refactored for efficiency and readability
    * Documentation has begun
    * Various changes to Jenkins pipeline

* 06/07/2022
    * Various changes to Jenkins pipeline to incorporate for Docker Swarm and Ansible
    * Documentation has been mostly completed

# Known Issues

* Integration testing has not been implemented. Thorough testing is essential to the production process, future work would include automating integration tests.

# Future Work

Besides fixing the known issue listed above, I would like to implement the following changes if I were to progress this project:
* Implement an SQL database to create and store a history of activities.
* Add futher styling to make the application more aesthetically pleasing.  
  