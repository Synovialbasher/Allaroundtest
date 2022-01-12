pipeline {
  agent { docker { image 'python:3.10.1-alpine' } }
  stages {
    stage('Build') {
      steps {
        print("Going to test everything now!")
        sh 'python testfile.py'
        print("Just did the first test file.")
        sh 'python additionalfile.py'
        print("Just did the second test file.")
        sh 'pytest'
        print("Moving on to the second stage.")
      }
    }
    stage {'Test'}
    {
      print("Going to run the pytest!")
      sh 'pytest'
    }
  }
}
