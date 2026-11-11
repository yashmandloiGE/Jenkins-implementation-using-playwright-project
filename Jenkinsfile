
pipeline {
    agent any

    stages {

        stage('Start') {
            steps {
                echo 'Starting Playwright Automation'
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m venv .venv
                    call .venv\\Scripts\\activate.bat
                    python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Install Playwright Browser') {
            steps {
                bat '''
                    call .venv\\Scripts\\activate.bat
                    python -m playwright install chromium
                '''
            }
        }

        stage('Run Automation Tests') {
            steps {
                bat '''
                    call .venv\\Scripts\\activate.bat
                    python -m pytest tests\\ -v -s
                '''
            }
        }
    }
}
