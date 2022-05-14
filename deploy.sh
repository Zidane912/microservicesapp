# # refresh build
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
docker network rm apinetwork

# Build Images
docker build -t service1 api1/application
docker build -t service2 api2/application
docker build -t service3 api3/application
docker build -t service4 api4/application

# Create Docker Network
docker network create apinetwork

# Run Containers
docker run -d -p 5000:5000 --network apinetwork --name service1 service1
docker run -d -p 5001:5001 --network apinetwork --name service2 service2
docker run -d -p 5002:5002 --network apinetwork --name service3 service3
docker run -d -p 5003:5003 --network apinetwork --name service4 service4