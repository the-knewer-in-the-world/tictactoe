pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = 'aditijadhav18/tictactoe'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/the-knewer-in-the-world/tictactoe.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKERHUB_REPO}:latest")
                }
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Run your tests here (pytest, unittest, etc.)"'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-cred') {
                        docker.image("${DOCKERHUB_REPO}:latest").push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                  docker rm -f tictactoe-container || true
                  docker run -d -p 5000:5000 --name tictactoe-container ${DOCKERHUB_REPO}:latest
                '''
            }
        }
    }
}
