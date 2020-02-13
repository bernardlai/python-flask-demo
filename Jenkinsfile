pipeline {
  agent any
  stages {
    stage('hhh') {
      parallel {
        stage('hhh') {
          steps {
            sh 'echo "laihh"'
            echo 'hello'
          }
        }

        stage('test') {
          steps {
            echo '1'
          }
        }

      }
    }

    stage('te2') {
      steps {
        sh 'exit1'
      }
    }

    stage('last') {
      parallel {
        stage('last') {
          steps {
            sh 'echo "laihh"'
          }
        }

        stage('last1') {
          steps {
            echo '2222'
          }
        }

        stage('last2') {
          steps {
            echo 'new'
          }
        }

        stage('') {
          steps {
            echo 'error'
          }
        }

      }
    }

    stage('new') {
      steps {
        sh 'echo "laihh"'
      }
    }

  }
}