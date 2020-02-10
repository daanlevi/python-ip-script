pipeline {
  stages {
    stage('Source') { // Get code
      // get code from our Git repository
      git 'https://github.com/beerkeeper/python-ip-script.git'
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
