# 📝 Blogging Platform

A simple and aesthetic mini-blogging app built with **FastAPI** (backend) and **HTML + Bootstrap** (frontend). Users can create, view, and manage blog posts via a clean UI and fast API responses.

---

## 🌟 Features

- ➕ Create blog posts with title, content, and author  
- 📃 View all blog posts  
- 🔄 Real-time display after submission  
- ⚡ Fast and lightweight backend using FastAPI  
- 💅 Clean responsive UI using Bootstrap 5  

---

## 🛠️ Tech Stack

| Layer    | Technology         |
|----------|--------------------|
| Frontend | HTML, Bootstrap    |
| Backend  | FastAPI (Python)   |
| Data     | In-Memory List     |
| Tools    | VS Code, GitHub    |

---

## 📁 Folder Structure
```
Blogging-Platform/
│
├── main.py              # FastAPI backend
├── index.html           # Frontend UI
├── README.md            # Project guide
└── requirements.txt     # Python dependencies
```

<br>

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/miss-panchal/Blogging-Platform.git
cd Blogging-Platform
```

### 2️⃣ Create Virtual Environment
```
python3 -m venv .venv
source .venv/bin/activate  # for Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install fastapi uvicorn
```

### 4️⃣ Run the FastAPI Server

```
uvicorn main:app --reload
```

App will run at: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc


## 5️⃣ Start creating blog posts and see them update live! 🚀

📸  1: Form UI 


<img width="1373" alt="Screenshot 2025-05-15 at 4 24 12 PM" src="https://github.com/user-attachments/assets/1802be8c-97aa-4b91-81ad-59efe9f70f1f" />


 
📸  2: Displayed Posts 


<img width="1349" alt="Screenshot 2025-05-15 at 4 31 25 PM" src="https://github.com/user-attachments/assets/1f071846-34f1-44d7-8a58-c437f9cdff93" />



<br>

## 🔧 API Endpoints Summary

| Method | Endpoint      | Description          |
|--------|---------------|----------------------|
| POST   | `/posts/`     | Create a new post    |
| GET    | `/posts/`     | Get all posts        |
| GET    | `/posts/{id}` | Get a post by ID     |
| PUT    | `/posts/{id}` | Update a post by ID  |
| DELETE | `/posts/{id}` | Delete a post by ID  |

---

## 💡 Future Improvements

- ✅ Save posts to a database (SQLite/Postgres)  
- ✅ Add edit/delete buttons to UI  
- ✅ Authentication for authors  
- ✅ Image upload support  

---

## 🙋‍♀️ Author

Made with ❤️ by [@miss-panchal](https://github.com/miss-panchal)

⭐ Star this repo if you found it useful!  
📬 Open an issue if you’d like to contribute or suggest improvements.

<br>

## 💡 Future Improvements
✅ Save posts to a database (SQLite/Postgres)

✅ Add edit/delete buttons to UI

✅ Authentication for authors

✅ Image upload support





