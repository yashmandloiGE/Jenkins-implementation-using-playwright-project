
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install playwright pytest pytest-html pytest-xdist'
            }
        }

        stage('Install Browser') {
            steps {
                bat 'python -m playwright install chromium'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat '''
                if not exist reports mkdir reports
                if not exist logs mkdir logs
                if not exist traces mkdir traces
                if not exist videos mkdir videos

                python -m pytest tests -v -s --html=reports/pytest-report.html --self-contained-html --junitxml=reports/junit.xml
                '''
            }
        }
    }

    post {

        always {

            stage('Archive Build Artifacts') {

                // Publish test results
                junit(
                    testResults: 'reports/junit.xml',
                    allowEmptyResults: true
                )

                // Archive all generated files
                archiveArtifacts(
                    artifacts: 'reports/**,logs/**,traces/**,videos/**',
                    fingerprint: true,
                    allowEmptyArchive: true
                )

                echo '======================================'
                echo 'BUILD ARTIFACT MANAGEMENT COMPLETED'
                echo '======================================'
                echo 'HTML Report: reports/pytest-report.html'
                echo 'JUnit Report: reports/junit.xml'
                echo 'Logs, Traces and Videos archived if generated.'
            }
        }
    }
}
