# **Take-Away-Assignment: Dockerized Quotes & Jokes API**

---

## **🎯 Objective**

In this assignment, you will build a **Python REST API** that serves random quotes and jokes, and then **containerize it using Docker**.

By completing this assignment, you will:

* Write a simple REST API with Python
* Use JSON files as data sources
* Build a Dockerfile using multiple Docker commands
* Run and test containers locally
* Push Docker images to Docker Hub
* Learn real-world Docker workflows

---

## **📂 Project Structure**

Organize your project like this:

```
takeaway-docker-assignment/
│
├── app.py                # Python API application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker instructions
├── quotes.json           # Predefined quotes
├── jokes.json            # Predefined jokes
└── README.md             # Assignment instructions
```

> **Tip:** You can create a `data/` folder for JSON files if you want to organize files better.

---

## **📝 Application Requirements**

Your API should provide the following endpoints:

| Endpoint     | Description                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| `GET /`      | Returns a welcome message that includes the **APP_NAME** environment variable |
| `GET /quote` | Returns a random quote from `quotes.json`                                     |
| `GET /joke`  | Returns a random joke from `jokes.json`                                       |

> Ensure you include **at least 5–10 quotes and 5–10 jokes**.

---

### **Environment Variables**

* **APP_NAME**: Name of the application
* Optional: **DATA_PATH** to point to your JSON files
* Display `APP_NAME` in the welcome endpoint (`GET /`)
* **Tip:** Students can also experiment with passing other variables to configure behavior

---

### **API Response Example**

```json
GET /quote
{
    "quote": "The only limit to our realization of tomorrow is our doubts of today.",
    "author": "Franklin D. Roosevelt"
}

GET /joke
{
    "joke": "Why did the programmer quit his job? Because he didn't get arrays."
}
```

---

## **🐳 Docker Requirements**

Your Dockerfile should include the following features:

| Docker Feature       | Requirement / Example                                                       |
| -------------------- | --------------------------------------------------------------------------- |
| **FROM**             | Use a lightweight Python image (`python:3.10-slim`)                         |
| **WORKDIR**          | Set the working directory inside the container (`/app`)                     |
| **COPY / ADD**       | Copy application code and JSON files into the image                         |
| **RUN**              | Install dependencies (`pip install -r requirements.txt`)                    |
| **ENV**              | Set environment variables like `APP_NAME`                                   |
| **ARG**              | Optional: Pass build-time arguments                                         |
| **EXPOSE**           | Expose the API port (`5000`)                                                |
| **CMD / ENTRYPOINT** | Start the Flask/FastAPI server                                              |
| **VOLUME**           | Optional: Mount a volume for JSON files to allow updates without rebuilding |
| **HEALTHCHECK**      | Optional: Verify API availability inside the container                      |

> **Tip:** Encourage students to **use multiple layers** to see how Docker builds and caches them.

---

## **🚀 Step-by-Step Workflow**

### **Step 1: Write the Python API**

* Create `app.py` with the required endpoints (`/`, `/quote`, `/joke`)
* Read quotes and jokes from JSON files
* Include `APP_NAME` in the welcome endpoint

### **Step 2: Create `requirements.txt`**

* Include all Python dependencies, e.g., Flask:

```
Flask==2.3.2
```

### **Step 3: Write the Dockerfile**

* Use the **Docker requirements** table above as a guide
* Include **comments** to explain each command
* Make it **robust**, using ENV, COPY, RUN, EXPOSE, and CMD

### **Step 4: Build the Docker Image**

```bash
docker build -t quote-joke-api .
```

### **Step 5: Run the Container Locally**

```bash
docker run -d -p 5000:5000 quote-joke-api
```

* **Tip:** Verify logs to ensure the server started correctly:

```bash
docker logs <container_id>
```

### **Step 6: Test API Endpoints**

* Welcome endpoint:

```bash
curl http://localhost:5000/
```

* Quote endpoint:

```bash
curl http://localhost:5000/quote
```

* Joke endpoint:

```bash
curl http://localhost:5000/joke
```

### **Step 7: Optional Volume Mounting**

* Allow JSON files to be updated without rebuilding the image:

```bash
docker run -d -p 5000:5000 -v $(pwd)/data:/app/data quote-joke-api
```

### **Step 8: Push to Docker Hub**

```bash
docker tag quote-joke-api <username>/quote-joke-api:latest
docker push <username>/quote-joke-api:latest
```

* Verify the image can be pulled and run on another machine.

---

## **📌 Deliverables**

1. Python application code (`app.py`)
2. JSON files (`quotes.json`, `jokes.json`)
3. Dockerfile using multiple Docker features
4. `requirements.txt`
5. Docker Hub repository link
6. Optional screenshot showing API responses

---

## **💡 Tips for a Professional Dockerfile**

* Use **ARG** for build-time configuration
* Comment every Dockerfile instruction
* Minimize image size by cleaning caches or using multi-stage builds
* Add **HEALTHCHECK** for API availability
* Consider using a **volume** for JSON data for easy updates

---

## **🎯 Learning Outcomes**

By completing this assignment, you will:

* Build a REST API from scratch
* Understand how Docker layers work
* Use environment variables, ARGs, and volumes
* Build, run, and test containers locally
* Push Docker images to Docker Hub and make them portable

---

✅ **This assignment gives hands-on experience with writing Python apps, building Dockerfiles with multiple features, and deploying containerized applications.**

---
