pipeline {
  stages {
    stage('Source') { // Get code
      // get code from our Git repository
      checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/daanlevi/python-ip-script.git']]])
    }
    stage('build') {
      steps {
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
