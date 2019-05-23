minikube start
kubectl create -f flask-deployment.yml
kubectl create -f flask-service.yml
kubectl apply -f minikube-ingress.yml
minikube dashboard
echo "$(minikube ip) api.aistream" | sudo -i tee -a /etc/hosts