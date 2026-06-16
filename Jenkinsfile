pipeline {
    agent any

    stages {

        stage('Create Venv') {
            steps {
                bat 'D:\\python314\\python.exe -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python -m pytest -v
                '''
            }
        }
    }
}