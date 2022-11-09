pipeline
{
  // This pipeline requires the following plugins:
  // * kubernetes Kubernetes Continuous Deploy PluginVersion 1.0.0

    agent { label 'agent1_for_website' }
    environment {
    			dockerhub=credentials('dockerhub')
			REPLICAS=2
                }

    stages {
        stage('Build docker image') {
                steps {
			sh 'sudo docker build -t doronamsalem/k8s_proj:weather_website_${BUILD_NUMBER} ./app_files/'
                }
        }


        stage('Test image') {
                steps {
                            echo "****building containers for testing*****"
                            sh '''
                                sudo docker run -dt --name test -p 80:8081 doronamsalem/k8s_proj:weather_website_${BUILD_NUMBER}
                                sudo docker ps   
                                '''
                            sh 'sleep 2.5'
                            sh 'python3 unit_tests/image_unittest.py'
                }
        }


        stage('Push to DockerHub') {
                steps {
			sh 'echo $dockerhub_PSW | sudo docker login -u $dockerhub_USR --password-stdin'
                        sh 'sudo docker push doronamsalem/k8s_proj:weather_website_${BUILD_NUMBER}'
			sh 'sudo docker logout'
                }
        }


        stage('Update deployment file') {
                steps {
			sh '''
				sed -i "s~doronamsalem/k8s_proj:weather_website_.*~doronamsalem/k8s_proj:weather_website_${BUILD_NUMBER}~" deployment.yml
                        	sed -i "s~replicas: .*~replicas: ${REPLICAS}~" deployment.yml
			'''
                }
        }


	stage('Deploying App to Master') {
		steps {
        		script {
          			kubernetesDeploy(configs: "deployment.yml", kubeconfigId: "k8s_project")
        		}
	        }
        }
	

        stage('Test for deployment') {
                steps {
                            sh 'python3 ./unit_tests/deployment_unittest.py'
                }
        }
    }


    post {
            always {
                        sh '''
				sudo docker stop test
				sudo docker rm test
				sudo docker rmi doronamsalem/k8s_proj:weather_website_${BUILD_NUMBER} 
			'''
                        deleteDir()
            }

            success {
                mail bcc: '', body: "Pipeline ${currentBuild.fullDisplayName} succeeded", cc: '', from: '', replyTo: '', subject: 'Pipeline status', to: 'doronamsalem100@yahoo.com'
            }

            failure {
                mail bcc: '', body: "Pipeline ${currentBuild.fullDisplayName} FAILED", cc: '', from: '', replyTo: '', subject: 'Pipeline status', to: 'doronamsalem100@yahoo.com'
            }
    }
}
