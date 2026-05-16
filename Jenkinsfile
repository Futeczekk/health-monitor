pipeline {
    agent any

    environment {
        IMAGE_NAME = "vps-health-monitor-ci"
        TEST_CONTAINER = "vps-health-monitor-ci-test"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies and check Python syntax') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    python -m py_compile app.py
                '''
            }
        }

        stage('Build Docker image') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME:$BUILD_NUMBER .
                '''
            }
        }

        stage('Run test container') {
            steps {
                sh '''
                    docker rm -f $TEST_CONTAINER || true
                    docker run -d \
                      --name $TEST_CONTAINER \
                      --network container:jenkins \
                      $IMAGE_NAME:$BUILD_NUMBER
                '''
            }
        }

        stage('Test health endpoint') {
            steps {
                sh '''
                    sleep 5
                    curl --fail http://localhost:5000/health
                '''
            }
        }
    }

    post {
        always {
            sh '''
                docker rm -f $TEST_CONTAINER || true
            '''
        }
    }
}
