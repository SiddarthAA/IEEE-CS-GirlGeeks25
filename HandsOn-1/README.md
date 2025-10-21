# Docker Flask Hands-On

Welcome to the Docker hands-on workshop! This project demonstrates a simple Flask web application that is containerized using Docker.  

Students will extend the app, add a new page, and learn how Docker images and containers work.

---

## **Project Structure**

```

docker-flask-demo/
│
├── app.py               # Main Flask app
├── requirements.txt     # Python dependencies
├── Dockerfile           # Instructions to build Docker image
├── README.md            # This instruction file
└── templates/
├── index.html       # Home page
└── about.html       # About page

````

> The `contact.html` page is intentionally missing. Your task is to create it.

---

## **Project Overview**

- `app.py` → Contains the Flask app with `/` (Home) and `/about` routes  
- `templates/` → HTML templates for the pages  
- `Dockerfile` → Defines how the Docker image is built  
- `requirements.txt` → Lists Python dependencies  
- `CONTACT_EMAIL` → Environment variable used to display the contact email on the Contact page

When built and run, the app can be accessed via:

- Home: http://localhost:5000/  
- About: http://localhost:5000/about  

---

## **Hands-On Tasks**

Your goal is to extend this app and practice Docker concepts.

### **1. Add a Contact Page**
1. Create a new file `templates/contact.html`.  
2. Include the following in your page:
   - Your name or a demo contact form (optional)  
   - A link back to Home and About pages  
   - Display the contact email using the environment variable:

```html
<p>If you want to reach us, email: {{ contact_email }}</p>
````

---

### **2. Update the Flask App**

1. Open `app.py`
2. Add a new route for `/contact`:

```python
@app.route('/contact')
def contact():
    return render_template('contact.html', contact_email=CONTACT_EMAIL)
```

3. Ensure that `CONTACT_EMAIL` is read from the environment:

```python
import os
CONTACT_EMAIL = os.getenv("CONTACT_EMAIL", "not-set@example.com")
```

---

### **3. Set the Environment Variable**

The app uses the `CONTACT_EMAIL` environment variable to display the contact email. There are two ways to set it:

#### **Option A: In the Dockerfile (default email)**

1. Open the `Dockerfile`.
2. Add or modify this line:

```dockerfile
ENV CONTACT_EMAIL="your_email@example.com"
```

3. Rebuild the image after making the change:

```bash
docker build -t flask-hands-on .
```

> This sets the default email inside the Docker image. All containers created from this image will use this email unless overridden.

#### **Option B: At Runtime (override)**

1. You can also set the email when running the container:

```bash
docker run -d -p 5000:5000 -e CONTACT_EMAIL="student@example.com" flask-hands-on
```

> This overrides the value in the Dockerfile and demonstrates dynamic container configuration.

---

### **4. Rebuild and Run the Docker Image**

After adding `contact.html`, updating `app.py`, and optionally modifying the Dockerfile:

```bash
docker build -t flask-hands-on .
docker run -d -p 5000:5000 flask-hands-on
```

Visit the pages in your browser:

* Home: [http://localhost:5000/](http://localhost:5000/)
* About: [http://localhost:5000/about](http://localhost:5000/about)
* Contact: [http://localhost:5000/contact](http://localhost:5000/contact)

> The contact page should display the email. If it doesn’t, check that you rebuilt the image after changing the Dockerfile or used the `-e` flag to set the email at runtime.

---

## **Learning Outcomes**

By completing this hands-on exercise, students will:

* Understand Dockerfile structure and commands
* Learn how Docker images and containers work
* See how changes in app code and Dockerfile require a rebuild
* Learn the basics of Flask routing and templates
* Use **environment variables** to configure the app dynamically
* Build a minimal multi-page web app inside a container

---

## **Tips**

* Always rebuild the image after making changes to `app.py`, templates, or the Dockerfile.
* Use `docker ps` to list running containers and `docker logs <container_id>` to see output.
* Encourage experimenting with environment variables using `-e` at runtime.

---