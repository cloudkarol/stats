#!/bin/sh
cd postgres/config
./create-configmap.sh
cd ../..
kubectl apply -f postgres/postgres-creds-secret.yaml
kubectl apply -f postgres/postgres-volume.yaml
kubectl apply -f postgres/postgres-volume-claim.yaml
kubectl apply -f postgres/postgres-replica-statefulset.yaml
kubectl apply -f postgres/postgres-service.yaml
kubectl apply -f upskill-app-deployment.yaml
