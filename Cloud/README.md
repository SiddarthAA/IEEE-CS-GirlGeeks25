# 🚀 Deploying a Dockerized Flask App on Google Cloud Run

Welcome to this hands-on workshop!
In this session, we’ll learn how to **containerize a simple Flask web application** using Docker, and then **deploy it on Google Cloud Run**, a fully managed serverless platform by Google Cloud.

By the end of this workshop, you’ll:

* Understand how to write a `Dockerfile`
* Build and test Docker images locally
* Push images to Google Cloud Registry
* Deploy them on **Google Cloud Run**
* View logs, metrics, and monitor the running service

---

## 🧩 Project Overview

We’ll create a small web app with two pages — a **Home page** and an **About page** — served via Flask.
Then, we’ll containerize it using Docker, and deploy that container to Cloud Run.

Here’s what the project structure looks like:

```
cloudrun-demo/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── templates/
│   ├── home.html
│   └── about.html
└── README.md
```

---

## ⚙️ Step 1: Set Up Your Environment

### 1. Install Required Tools

Before you begin, make sure you have:

| Tool                          | Purpose                   | Install Command / Link                                            |
| ----------------------------- | ------------------------- | ----------------------------------------------------------------- |
| **Python 3.10+**              | To run Flask locally      | [python.org/downloads](https://www.python.org/downloads/)         |
| **Docker Desktop / CLI**      | To build & run containers | [docker.com/get-started](https://www.docker.com/get-started)      |
| **Google Cloud SDK (gcloud)** | To interact with GCP      | [cloud.google.com/sdk](https://cloud.google.com/sdk/docs/install) |
| **A Google Cloud Account**    | To deploy on Cloud Run    | [cloud.google.com](https://cloud.google.com)                      |

After installing, verify:

```bash
docker --version
gcloud --version
```

---

## 🧱 Step 2: Build the Application

### 1. Create the Flask App

`app.py`

```python
from flask import Flask, render_template
import os, logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home page accessed")
    return render_template("home.html")

@app.route('/about')
def about():
    app.logger.info("About page accessed")
    return render_template("about.html")

@app.route('/healthz')
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
```

---

### 2. Add Templates

**`templates/home.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cloud Run Demo - Home</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f2f2f2; text-align: center; padding: 50px; }
        a { color: #0066cc; text-decoration: none; margin: 10px; }
    </style>
</head>
<body>
    <h1>🚀 Welcome to Flask on Cloud Run</h1>
    <p>This app is running inside a Docker container!</p>
    <p><a href="/about">Learn more →</a></p>
</body>
</html>
```

**`templates/about.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cloud Run Demo - About</title>
    <style>
        body { font-family: Arial, sans-serif; background: #fefefe; text-align: center; padding: 50px; }
        a { color: #0066cc; text-decoration: none; margin: 10px; }
    </style>
</head>
<body>
    <h1>About This App</h1>
    <p>This app demonstrates how to containerize and deploy a Flask app on Google Cloud Run.</p>
    <p><a href="/">Back Home</a></p>
</body>
</html>
```

---

### 3. Add Requirements File

**`requirements.txt`**

```
Flask==3.0.3
gunicorn==21.2.0
```

---

## 🐳 Step 3: Dockerize the Application

Create a `Dockerfile` in the root folder.

```dockerfile
# 1. Base image
FROM python:3.10-slim

# 2. Working directory
WORKDIR /app

# 3. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all files
COPY . .

# 5. Expose the port Cloud Run expects
EXPOSE 8080

# 6. Run the app with gunicorn
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 app:app
```

---

## 🧪 Step 4: Test Locally with Docker

Build the Docker image:

```bash
docker build -t cloudrun-demo .
```

Run the container locally:

```bash
docker run -p 8080:8080 cloudrun-demo
```

Visit [http://localhost:8080](http://localhost:8080) and check that it works.

> **Tip:**
> Use `docker ps` to list running containers and `docker logs <container_id>` to view logs.

---

## ☁️ Step 5: Deploy to Google Cloud Run

Now that our container works locally, let’s deploy it on GCP.

---

### 1. Authenticate and Select Project

```bash
gcloud auth login
gcloud config set project <your-project-id>
```

You can list projects using:

```bash
gcloud projects list
```

---

### 2. Enable Required APIs

```bash
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

---

### 3. Build and Push Image to Google Container Registry (GCR)

```bash
gcloud builds submit --tag gcr.io/<your-project-id>/cloudrun-demo
```

This command:

* Builds your Docker image in Google Cloud
* Pushes it to GCR under your project ID

---

### 4. Deploy to Cloud Run

```bash
gcloud run deploy cloudrun-demo \
  --image gcr.io/<your-project-id>/cloudrun-demo \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated
```

When prompted:

* Choose your region (`asia-south1` for Bangalore)
* Allow unauthenticated access → type `y`

---

### 5. Verify Deployment

You’ll get an output like:

```
Service [cloudrun-demo] revision [cloudrun-demo-00001] has been deployed and is serving traffic at:
https://cloudrun-demo-xyz123.asia-south1.run.app
```

Open this URL — your app is now live on the cloud!

---

## 📊 Step 6: Viewing Logs and Monitoring

All logs from your container are automatically sent to **Cloud Logging**.

To view logs:

```bash
gcloud logs read --project=<your-project-id> --limit=20
```

Or use the **Google Cloud Console**:

* Go to **Navigation Menu → Cloud Run → cloudrun-demo → Logs**

You’ll see entries like:

```
INFO:root:Home page accessed
INFO:root:About page accessed
```

---

## 🧹 Step 7: Cleanup (Important)

To avoid charges after the workshop, delete the service and image:

```bash
gcloud run services delete cloudrun-demo --region asia-south1
gcloud container images delete gcr.io/<your-project-id>/cloudrun-demo
```

---

## 🔍 Common Issues

| Error                      | Cause                           | Fix                                |
| -------------------------- | ------------------------------- | ---------------------------------- |
| `PORT not set`             | Forgot `$PORT` env var in Flask | Use `os.environ.get("PORT", 8080)` |
| `Docker not found`         | Docker not installed or running | Install Docker Desktop             |
| `gcloud permission denied` | Not logged in or no IAM access  | Run `gcloud auth login`            |
| `Image not found`          | Wrong GCR path                  | Double-check project ID            |

---

## 💡 Optional Enhancements (for advanced students)

| Enhancement                      | Description                                           |
| -------------------------------- | ----------------------------------------------------- |
| **Add API endpoint**             | Add `/predict` or `/data` route to simulate ML models |
| **Connect to Cloud SQL / Redis** | Show multi-service connectivity                       |
| **Add CI/CD**                    | Use GitHub Actions to auto-deploy                     |
| **Add environment variables**    | Pass configs using `--set-env-vars` flag              |
| **Use a custom domain**          | Map a domain via Cloud Run custom domain mapping      |

---

## 🎯 Learning Outcomes

By completing this workshop, you’ve learned how to:

✅ Containerize a Python Flask application
✅ Build, run, and test a Docker image locally
✅ Deploy the image on Google Cloud Run
✅ Observe logs and understand serverless scaling
✅ Manage and clean up cloud resources responsibly

---

## 🏁 Summary Commands (Quick Reference)

```bash
# Build locally
docker build -t cloudrun-demo .
docker run -p 8080:8080 cloudrun-demo

# Deploy to Cloud Run
gcloud builds submit --tag gcr.io/<your-project-id>/cloudrun-demo
gcloud run deploy cloudrun-demo \
  --image gcr.io/<your-project-id>/cloudrun-demo \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated

# Check logs
gcloud logs read --project=<your-project-id> --limit=20

# Clean up
gcloud run services delete cloudrun-demo --region asia-south1
gcloud container images delete gcr.io/<your-project-id>/cloudrun-demo
```
