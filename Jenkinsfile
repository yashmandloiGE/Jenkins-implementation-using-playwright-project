pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m venv venv
                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    venv\\Scripts\\pytest.exe test_automation.py --junitxml=results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}