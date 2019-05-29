gcloud container clusters get-credentials ml-flask-1
kubectl create -f flask-deployment.yml
kubectl create -f flask-service.yml
kubectl apply -f gcp-ingress.yml