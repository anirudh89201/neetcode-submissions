    pipeline {
        agent any
        
        stages {
            stage('Debug') {
                steps {
                    bat 'docker --version'
                    bat 'where docker'
                }
            }
            stage('Checkout') {
                steps {
                    checkout scm
                }
            }

            stage('Install Dependencies') {
                steps {
                    bat '''
                        python -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pip install flake8 black
                        '''
                }
            }

            stage('Lint') {
                steps {
                    dir('app') {
                        bat '''
                            . venv/bin/activate
                            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                        '''
                    }
                }
            }
            stage('black'){
                steps{
                    bat '''
                    call venv/bin/activate.ps1
                    black app/*
                    '''
                }
            }
    }
}
