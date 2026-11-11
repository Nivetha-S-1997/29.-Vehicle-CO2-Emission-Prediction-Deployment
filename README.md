# Vehicle CO₂ Emission Prediction Deployment

## Project Overview

Developed a machine learning-based web application to predict vehicle CO₂ emissions (g/km) using engine size and combined fuel consumption.

The project uses a **Random Forest Regressor** integrated with a Flask web application, allowing users to enter vehicle parameters and obtain predicted emission values.

The application is organized into multiple deployment implementations using Google Cloud Platform (GCP), Docker, Kubernetes, and a CI/CD workflow.

## Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn, Random Forest Regression
- **Web Framework:** Flask
- **Containerization:** Docker
- **Cloud Platform:** Google Cloud Platform (GCP)
- **Cloud Services:** Google App Engine, Google Kubernetes Engine (GKE), Artifact Registry, Cloud Build
- **Orchestration:** Kubernetes
- **CI/CD:** GitHub Actions
- **Version Control:** Git, GitHub

## Machine Learning Model

**Objective:** Predict vehicle CO₂ emissions based on vehicle-related parameters.

**Input Features:**
- Engine Size (L)
- Combined Fuel Consumption (L/100 km)

**Target Variable:**
- CO₂ Emissions (g/km)

**Algorithm:** Random Forest Regressor

**Model Performance:** R² Score ≈ 0.976

The trained model is saved as a `.sav` file and loaded into the Flask application to generate predictions.

## Application Workflow

1. Users enter engine size and combined fuel consumption through the web interface.
2. Flask receives and processes the input values.
3. The trained Random Forest model predicts CO₂ emissions.
4. The predicted result is displayed on the output page in g/km.

## Deployment Methods

### 1. Google App Engine

Deployed the Flask application on Google App Engine using the `app.yaml` configuration file.

**Key Components:**
- Flask application
- Python runtime
- App Engine configuration
- GCP deployment using Google Cloud CLI

### 2. Docker Deployment

Containerized the Flask application using Docker to ensure a consistent execution environment.

**Key Components:**
- Dockerfile
- Python dependencies
- Gunicorn application server
- Docker image build and local container execution

The application was successfully tested through a locally running Docker container.

### 3. Kubernetes Deployment (GKE)

Deployed the containerized application on Google Kubernetes Engine (GKE).

**Key Components:**
- Kubernetes Deployment YAML
- Kubernetes Service YAML
- Docker image stored in Artifact Registry
- LoadBalancer service for external access
- Pod deployment and container management

The application was successfully accessed and tested using the external IP address assigned by the Kubernetes LoadBalancer.

### 4. CI/CD Pipeline

The project includes a CI/CD workflow using GitHub Actions and Google Cloud Platform for automating application delivery.

**Pipeline Workflow:**

1. Source code is maintained in GitHub.
2. Code changes trigger the CI/CD workflow.
3. Application dependencies are installed and automated checks are executed.
4. A Docker image is built for the application.
5. The Docker image is pushed to Google Cloud Artifact Registry.
6. The updated application is deployed to the configured cloud environment.

**Tools:** GitHub Actions, Docker, Google Cloud Platform, Artifact Registry.

## Repository Structure

```text
Vehicle-CO2-Emission-Prediction/
│
├── App-Engine/
│   ├── templates/
│   │   ├── input.html
│   │   └── output.html
│   ├── main.py
│   ├── app.yaml
│   ├── requirements.txt
│   └── Final_model_randomforest.sav
│
├── Docker/
│   ├── templates/
│   │   ├── input.html
│   │   └── output.html
│   ├── main.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── Final_model_randomforest.sav
│
├── Kubernetes/
│   ├── templates/
│   │   ├── input.html
│   │   └── output.html
│   ├── main.py
│   ├── Dockerfile
│   ├── co2-ml-deployment.yaml
│   ├── co2-ml-service.yaml
│   ├── requirements.txt
│   └── Final_model_randomforest.sav
│
└── README.md
```

## Key Learnings

- Integrating a trained machine learning model into a Flask web application.
- Deploying Python applications using Google App Engine.
- Building and running containerized applications with Docker.
- Managing Kubernetes Pods, Deployments and Services on GKE.
- Configuring Google Cloud IAM permissions and Artifact Registry access.
- Understanding CI/CD workflows for automated application delivery.

## Author

**Nivetha S.**
