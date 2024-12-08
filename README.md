***Microservices Application Deployment with CI/CD***

This repository contains microservices for Order, User, and Payment, designed for deployment on a Kubernetes cluster with a CI/CD pipeline.

**Microservices Overview**

Order: Handles order-related operations.

User: Manages user accounts and profiles.

Payment: Processes payment transactions.

Each microservice includes:

app.py: Main application code.

Dockerfile: Instructions to build the Docker image

requirements.txt: Python dependencies.

deployment.yaml: Kubernetes Deployment manifest.

service.yaml: Kubernetes Service manifest.


1. ***Build and Push Docker Images***
   
  1.1  Navigate to each microservice folder (order, user, payment).
  
  1.2  Build the Docker image:
         docker build -t CloudLabs.azurecr.io/<service-name>:latest .
         
  1.3  Push the image to Azure Container Registry:
         docker push CloudLabs.azurecr.io/<service-name>:latest
   
2. **Deploy to Kubernetes**
   
  2.1  Update deployment.yaml with your container image path.
  
  2.2  Apply the manifests to the Kubernetes cluster

         kubectl apply -f deployment.yaml
         kubectl apply -f service.yaml

         
3. **CI/CD with GitHub Actions**
   
A GitHub Actions workflow is set up to automate the process:

   Triggered on every push to the main branch.

   Builds and pushes Docker images to ACR.
   
   Deploys the latest changes to the Kubernetes cluster.


The workflow file is located in .github/workflows/ci-cd.yaml.

   

