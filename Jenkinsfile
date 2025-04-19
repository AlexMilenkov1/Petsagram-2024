pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AlexMilenkov1/Petsagram-2024'
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                    python -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
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
