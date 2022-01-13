pipeline {
  agent { docker { image 'python:3.10.1-alpine' } }
  stages {
    stage('Build') {
      steps {
        echo "Going to test everything now!"
        sh 'python testfile.py'
        echo "Just did the first test file."
        sh 'python additionalfile.py'
        echo "Just did the second test file."
        echo "Moving on to the second stage."
      }
    }
    stage ('Install pytest')
    {
      steps
      {
        echo "Going to install pytest!" 
        sh 'python3.9 --version'
      }
    }
  }
}
