pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/the-knewer-in-the-world/tictactoe.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("tictactoe-app")
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm tictactoe-app python -m unittest discover -s tests'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 --name tictactoe tictactoe-app'
            }
        }
    }
}
