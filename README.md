# K8S with an API Gateway
---

This is a proof-of-concept for running managed containers within a 
kubernetes cluster with Traefik infront.

#### start kubernetes
`>> minikube start`

#### set docker context (per terminal) so we can use local docker images
`>> eval $(minikube docker-env)`

#### setup minikube tunnel to make sure we get an external ip
`minikube tunnel`

#### setup helm
`helm init`

#### install traefik with helm (should be able to pass in values with cli using --set)
`helm install --values resource-manifests/values.yml stable/traefik`

#### check external ip with the output of the prenumilate step
`kubectl get svc ... --namespace default -w`

#### add the external ip to /etc/hosts
`XXX.XXX.XXX.XXX  traefik-ui.minikube service-one.minikube service-two.minikube`

#### build the docker containers
`cd sa-service-1 && docker build -t sa-service-1 .`
`cd sa-service-2 && docker build -t sa-service-2 .`

#### create the cluster's deployments, services and ingresses
`
>> kubectl apply -f resource-manifests/service-one.yml
>> kubectl apply -f resource-manifests/service-two.yml
`

#### verify
`>> kubectl get all`

