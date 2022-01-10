pipeline {
  agent { docker { image 'python:3.10.1-alpine' } }
  stages {
    stage('Build') {
      steps {
        sh 'python testfile.py'
        sh 'python additionalfile.py'
      }
    }
  }
}
