pipeline {
  agent { docker { image 'python:3.10.1-alpine' } }
  stages {
    stage('Build') {
      steps {
        print("Going to test everything now!")
        sh 'python testfile.py'
        sh 'python additionalfile.py'
        sh 'pytest'
      }
    }
  }
}
