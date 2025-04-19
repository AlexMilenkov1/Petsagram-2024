pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-v /tmp:/tmp'
        }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AlexMilenkov1/Petsagram-2024'
            }
        }

        stage('Set up Python') {
             steps {
                sh '''
                    python3 -m venv venv || exit 1
                    . venv/bin/activate || exit 1
                    pip install --upgrade pip || exit 1
                    pip install -r requirements.txt || exit 1
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    python manage.py test
                '''
            }
        }

        stage('Trigger Render Deploy') {
            steps {
                sh '''
                    curl -X POST https://api.render.com/deploy/srv-d01mkt2dbo4c738toc3g?key=nqwk7W7TOdk
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment triggered successfully.'
        }
        failure {
            echo '❌ Build failed. Check the logs.'
        }
    }
}
