pipeline{
    agent any
    stages{
        stage ('Build'){
            step{
                echo "Etapa BUILD no disponible"

            }
        }
        stage('Tests'){
            step{
                echo "Etapa TEST no disponible"
            }
        }
        stage ('Deploy'){
            steps{
                sh "docker-compose down -v"
                sh "docker-compose up -d --build"
            }
        }
    }
}