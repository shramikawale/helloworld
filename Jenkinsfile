pipeline {
    agent any
 stages {
  stage('Docker Build and Tag') {
           steps {
              
                sh 'docker build -t groot049/test1:latest .'
                sh 'docker tag groot049/test1:latest groot049/test1:$BUILD_NUMBER'
          }
        }
     
 stage('Publish image to Docker Hub') {
          
            steps {
        withDockerRegistry([ credentialsId: "dockerhub", url: "" ]) {
          sh  'docker push groot049/test1:$BUILD_NUMBER'
        }
                  
        }
    }
  }
}
