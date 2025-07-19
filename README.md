# Django Real-Time Chat Application
A real-time chat application built using Django, Django Channels, and WebSockets, featuring user authentication, room-based messaging, and file sharing. Messages appear instantly without page reloads, and files can be uploaded and shared seamlessly between users.

Features
  User Authentication – Signup, Login, and Logout functionality.
  Real-Time Messaging – WebSocket-based instant chat with no page refresh.
  Room-based Chat – Join or create chat rooms dynamically.
  File Sharing – Share and download files directly in chat.
  Redis Integration – For efficient WebSocket message handling.
  Daphne Server – Runs the ASGI application for real-time support.

Tech Stack
  Backend: Django, Django Channels, ASGI
  Frontend: HTML, JavaScript
  Database: SQLite3 (default)
  WebSocket Server: Daphne
  Message Broker: Redis

Project Structure
  chat_project2/
  ├── chat_app/              # Main app (views, consumers, routing, templates)
  ├── chat_project2/         # Project settings and ASGI configuration
  ├── media/                 # Uploaded files storage
  ├── db.sqlite3             # Database
  └── manage.py              # Django management script
  
How to Run Locally

  1.Clone the repository:
      git clone https://github.com/yourusername/django-chat-app.git
      cd django-chat-app
      
  2.Create and activate a virtual environment:
      python -m venv .env
      .\.env\Scripts\activate
      
  3.Install dependencies:
      pip install -r requirements.txt
      
  4.Apply migrations:
      python manage.py migrate
      
  5.Start Redis server:
      redis-server
      
  6.Run the Daphne server:
      daphne -p 8000 chat_project2.asgi:application
      
  7.Open browser:
    http://127.0.0.1:8000/
