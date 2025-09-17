pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred')   // Jenkins credential ID
        DOCKERHUB_REPO = 'aditijadhav18/tictactoe'    // Replace with your repo
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
                script {
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
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
                sh 'docker run -d -p 5000:5000 --name tictactoe-container aditijadhav18/tictactoe:latest'
            }
        }
    }
}
