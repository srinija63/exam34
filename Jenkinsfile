pipeline{
    agent any
    stages{
        stage('Build image'){
            steps{
                echo 'Building Docker image...'
                bat 'docker build -t mywebapp .'
            }
        }
        stage('docker login'){
            steps{
                echo 'Logging in to Docker Hub...'
                bat 'docker login -u saradasrinija -p @Srinadh63@'
            }
        }
        stage('Push image to docker hub'){
            steps{
                echo 'Pushing Docker image to Docker Hub...'
                bat 'docker tag mywebapp saradasrinija/sample:latest'
                bat 'docker push saradasrinija/sample:latest'
            }
        }
        stage('Deploy to kubernetes'){
            steps{
                echo 'Deploying to Kubernetes...'
                bat 'kubectl apply -f deplyment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post{
            success{
                echo 'Deployment successful!'
            }
            failure{
                echo 'Deployment failed.'
            }
        }
}
