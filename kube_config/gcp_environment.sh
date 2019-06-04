gcloud container clusters get-credentials standard-cluster-1 --zone=enter_your_zone
kubectl create -f flask-deployment.yml
kubectl create -f flask-service.yml
kubectl apply -f gcp-ingress.yml