pipeline {
  agent { docker { image 'python:3.7.6' } }
  stages {
    stage('Source') { // Get code
      steps {
        // get code from our Git repository
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/daanlevi/python-ip-script.git']]])
      }
    }
    stage('build') {
      steps {
        sh 'mkvirtualenv --python=$(which python3) daniel'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('run') {
      steps {
        sh 'python main.py'
      }
    }
  }
}
