pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'python -m pip install -r requirements.txt'
                sh 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t sample-ci-app .'
            }
        }

        stage('Run Application') {
            steps {
                sh 'docker run --rm sample-ci-app'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}