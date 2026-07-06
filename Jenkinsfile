
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                "C:\\Users\\pavan\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe"
                "C:\\Users\\pavan\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                if not exist reports mkdir reports
                "C:\\Users\\pavan\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe"
                '''
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])
        }
    }
}

