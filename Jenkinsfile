pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/AlexMilenkov1/Petsagram-2024'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m venv venv || exit /b 1
                    call venv\\Scripts\\activate || exit /b 1
                    python -m pip install --upgrade pip || exit /b 1
                    pip install -r requirements.txt || exit /b 1
                '''
            }
        }


        stage('Trigger Render Deploy') {
            steps {
                bat 'curl -X POST "https://api.render.com/deploy/srv-d01mkt2dbo4c738toc3g?key=nqwk7W7TOdk" || exit /b 1'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline succeeded! Deployment triggered on Render.'
        }
        failure {
            echo '❌ Pipeline failed! Check logs.'
        }
        always {
            bat 'rmdir /s /q venv'  // Cleanup virtualenv
        }
    }
}