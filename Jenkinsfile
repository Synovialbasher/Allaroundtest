pipeline {
  agent {any}
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
        echo "Going to see python!" 
        sh 'whoami'
        sh 'python --version'
        echo "Going to see pip!"
        sh 'pip --version'
        echo "Going to try and install pytest"
        sh 'sudo pip install pytest'
      }
    }
  }
}
