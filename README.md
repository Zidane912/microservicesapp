# Video Presentation Link

https://drive.google.com/file/d/1Aycw6nqWjSYPhbdxzjaUksuSkpI-aS_9/view?usp=sharing

# Architecture of Project
This is a basic microservices application that is is deployed over several virtual machines and IP addresses. The architeccture of this project follows the diagram as show below.

![Untitled Diagram drawio](https://user-images.githubusercontent.com/96538941/169118649-f17edc8a-587e-4004-a98d-a3d7e994c5ae.png)

Firstly the microservices:

1. Service 1:
Service 1 was used to both display and utilise get and post requests from the other services. This was start off by performing a get request from service 2.

2. Service 2:
This service contained a list of names for rpg roles such as Hero or Healer and the like upto ten items and to grab an item from this list a randint dependency was imprted. Service 2 would generate one of these names by random. Thereafter service 1 would make a get reuqest to service 2 to retirve said rpg role.

3. Service 3:
This service contained several statistic values based on what was generated from service 2. service 1, using the data generated from service 2, would make a post request to service 3 and depending on the data generated service 3 would provide a statistic for said rpg role such as 'HP: 300 MP: 3000'.

4. Service 4:
Service 1 would make a post request to this service that generated data based off services 2 and 3. So within service 1 the datas of service 2 and 3 were 
concatenate into a single string. There after this was posted to service 4 where it was split into two items in a single list thus allowing it to be indexed into the data from service 2 and the data from service 3 making both readily avaiable in service 4. Service 4 based on the conditions of service 2 and 3 would generate a descripton of this rpg role.

All of this is then generated and displayed on from service 1 which returns the various values from all services into the html file, below are some examples of what would be displayed:

![image](https://user-images.githubusercontent.com/96538941/169007588-1c869641-5235-47a1-a483-42153118cc54.png)

![image](https://user-images.githubusercontent.com/96538941/169007623-baabbbd6-65f8-4ef6-9309-2b88e909a2f1.png)

![image](https://user-images.githubusercontent.com/96538941/169007675-26a533cf-1467-431e-96b9-5a586baafd75.png)

As for the arhcitecture of the virtual machines (VM) themselves. VM1, using an Ansible playbook, dealt with the deployment of the application using an ansible play book to build and install onto VM2 (swarm manager) whereby the repository of the application was cloned to from GitHub to the swarm manager and thereafter a docker swarm was initialised and VM3 (swarm worker) was added to the swarm. The application was then build and deployed from the swarm manager and thus was avaiable on both the swarm worker and manager on port 5000 of their public IP addresses. The ansible playbook would also push images to docker hub, below is a screen shot of the images from docker hub used for the application:

![image](https://user-images.githubusercontent.com/96538941/169011519-9fe824bc-c191-4af2-8ad4-dbcaafb74474.png)

VM1 also deployed the application both on an nginx load balancer as well as deploying the application through a jenkins pipeline which were both available on ports 80 and 5000 respectively.

# Setup

This setup requires thrree virtual machines with the first virtual machine having the following dependencies installed Python, pytest, Flask, Docker, Docker-compose, Ansible, nginx, Jenkins and git. All three machines run Ubuntu and the ssh key generated from the first virtual machine must be inserted into the virtual machines of the other two via google cloud platform. Thereafter these commands are followed onto the first virtual machine,

1. git clone https://github.com/Zidane912/finalproject2.git && cd finalproject2
2. ansible-playbook -i inventory.yaml playbook.yaml

On the swarm manager or the swarm worker virtual machine, running the following will run the application in the terminal,

curl localhost:5000

Consequently the following could be typed into the browser:

[PUBLIC_IP_ADDRESS of either virtual machine]:5000

As for nginx, the following command is followed on the first virtual machine:

1. sudo nano /etc/nginx/nginx.conf
2. Insert the text from the nginx.conf file into the terminal once step 1 has been executed into the terminal, ensuring to replace the private IP addresses found on Google Cloud Platform.
3. curl localhost

The application should be running on port 80 now.

# Testing

Four tests were run using pytest, one for each microservice, giving an average of 93 % coverage, below are some screenshots of the report coverages:

Service 1

![image](https://user-images.githubusercontent.com/96538941/169017452-e3eb7296-7e9a-465a-ad42-cf41c5fc4c37.png)

Service 2

![image](https://user-images.githubusercontent.com/96538941/169013017-2494ca4e-188e-4684-a036-34eb7d9cb652.png)

Service 3

![image](https://user-images.githubusercontent.com/96538941/169013254-5f29fcd7-3ccb-4e3a-ab6f-284011f80a74.png)

Service 4

![image](https://user-images.githubusercontent.com/96538941/169013452-aa7cc6c5-48a5-4a56-b56e-03c57fcb880a.png)

# User Journey Story

![USJ drawio](https://user-images.githubusercontent.com/96538941/169002027-f6ed2e6a-a6ca-46df-8799-7f91055c503c.png)

# Kanban Board

Please refer to the project board on this repository or click on this link: https://github.com/Zidane912/finalproject2/projects/1

# Risk Assessment

![image](https://user-images.githubusercontent.com/96538941/169005321-eb23e3e5-ce90-45c5-abf1-b459e8560b93.png)

# Jenkins Pipeline and Webhooks

Here is the final set of build steps of the Jenkins pipeline:

![image](https://user-images.githubusercontent.com/96538941/169018009-a4a9e5e0-cfdb-4b39-8582-753ab415b9e1.png)

**NOTE:** Although the final step 'Deployment of Application gives an error, the pipeline still functtions perfectly. This error is due to ports already being assigned on this virtual machine, here is the error message that is shown on the console output:

Error response from daemon: driver failed programming external connectivity on endpoint finalproject2-service3-1 (370071175bd03098292c6662b5ec5e190661ef8998a89662527b7b830f2746d3): Bind for 0.0.0.0:5002 failed: port is already allocated

It is known that the pipeline still works as the port 5000 of the public address was checked before and after the build, before the build the application would not run and after the build the application does run as it would if all steps were shown to be completely successfully.

Webhooks was used to keep track of changes made to the project:

![image](https://user-images.githubusercontent.com/96538941/169018206-a87f17f5-dca6-485b-a16a-34b877492ed7.png)

# Continuous Integration and Delivery Diagram

![cicd drawio (1)](https://user-images.githubusercontent.com/96538941/169061203-3f35eb9d-42e3-43d4-a315-e4e8d11e4309.png)

# Future Improvements

* Integrate user input system, i.e. application displays name of user and data generated is associated with user
* Implement frontend with CSS to improve user experience
* Test all lines of code to ensure 100% test coverage
