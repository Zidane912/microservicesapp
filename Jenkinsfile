pipeline{
    agent any
    stages{
        stage('Cloning Repository From GitHub'){
            steps{
                script{
                    if(fileExists('/home/jenkins/.jenkins/workspace/finalproject2')){
                        sh 'cd finalproject2 && git pull'
                    }
                    else{
                        sh 'git clone https://github.com/Zidane912/finalproject2.git'
                    }
                }
            }
        }
        stage('Dependency Installations'){
            steps{
                sh 'cd finalproject2 && pip3 install -r api1/application/requirements.txt'
                sh 'cd finalproject2 && pip3 install -r api2/application/requirements.txt'
                sh 'cd finalproject2 && pip3 install -r api3/application/requirements.txt'
                sh 'cd finalproject2 && pip3 install -r api4/application/requirements.txt'
            }
        }
        stage('Mock Testing'){
            steps{
                sh 'cd finalproject2/api1 && python3 -m pytest --cov=application'
                sh 'cd finalproject2/api2 && python3 -m pytest --cov=application'
                sh 'cd finalproject2/api3 && python3 -m pytest --cov=application'
                sh 'cd finalproject2/api4 && python3 -m pytest --cov=application'
            }
        }
        stage('Building Application and Pushing Images to DockerHub'){
            steps{
                sh 'cd finalproject2 && docker-compose build'
                sh 'cd finalproject2 && docker-compose push'
            }
        }
        stage('Deployment of Application'){
            steps{
                sh 'cd finalproject2 && docker-compose up -d'
            }
        }
    }
}