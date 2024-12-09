Travel Guide Application
📖 Description:
The Travel Guide Application is a user-friendly platform designed to assist travelers in planning their trips with ease. The application provides features such as searching for destinations, adding favorite places to a cart, exploring and booking hotels, and managing bookings. Built using modern web technologies, the app ensures a seamless user experience, making travel planning an enjoyable task.


🛠 Technologies Used:
Backend: Flask (Python)
Frontend: HTML, CSS, Bootstrap
Database: MySQL (for storing user, places and booking data)
Tools:
PyCharm (for development)
Virtual Environment (for dependency management)

🚀 Features:
--> User Management
User Sign-Up and Login functionality.
Secure authentication using hashed passwords.
Admin functionalities to manage places and hotels.
--> Destinations
Search for popular destinations based on preferences.
Add favorite places to a cart for future reference.
--> Hotels
Search for hotels based on check-in and check-out dates and number of rooms.
Book hotels with the number of rooms required.
View booking details in the user profile.

📋 Requirements

* Python 3.8 or above
* PyCharm community edition (or any Python IDE)
*  Postgre sql (version 15.7)
* Python Libraries like Flask, render_template, request, redirect, url_for, session, flash.

The required libraries are listed in the requirements.txt file. Key libraries include:
* Flask
* Flask-WTF
* Flask-SQLAlchemy
* Werkzeug
* MySQL-connector-python

💻 How to Set Up and Run the Application:
1. Clone the Repository
   git clone https://github.com/<your-usernam>/travel-guide.git
   cd travel-guide
2. Set Up a Virtual Environment
   python -m venv venv
3. Activate the Virtual Environment
   venv\Scripts\activate
  Windows:
 venv\Scripts\activate
  Mac/Linux:
 source venv/bin/activate
4. Install Dependencies
   pip install -r requirements.txt
5. Configure the Database
  * Create a MySQL database named travel_guide.
  * Update the database configuration in the app.py file
  db_host = "localhost"
  db_user = "your_username"
  db_password = "your_password"
  db_database = "travel_guide"
6. Initialize the Database
   Run the following command to create necessary tables:
   python db.py
7. Start the Application
   python app.py
8. Open the Application
   Open your browser and navigate to:
   http://127.0.0.1:5000/


🔍 Functionalities:
1. User Authentication
Users can register and log in securely.
Admin users can manage places and hotels.
2. Destinations
Users can browse and search for places.
Add places to the cart for easy trip planning.
3. Hotel Booking
Search for available hotels by specifying check-in/out dates and room requirements.
Book hotels and view booking details in the user profile.

🛠 Development Workflow:
Directory Structure
travel-guide/
│
├── travel_booking/  
│   ├── static/              # CSS and image assets
│   ├── templates/           # HTML templates
│   ├── app.py               # Main application file
│   └── db.py                # Database operations
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

-->Key Files:
app.py: Contains Flask routes for the application.
db.py: Handles database operations for users, places, and hotels.
templates/: Includes HTML files for pages like login, signup, destinations, and booking.
static/: Contains stylesheets and images for the application.

🔧 How to Run in PyCharm
1. Open PyCharm and Import the Project
Launch PyCharm and open the travel-guide folder.

2. Set Up the Virtual Environment
Go to File > Settings > Project > Python Interpreter.
Add the venv virtual environment created earlier.

3. Run the Application
Open app.py and click the green run button.

4. Access the Application
The app will be hosted locally at http://127.0.0.1:5000.


