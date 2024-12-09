TRAVEL GUIDE:

Overview:
Travel Guide is a web-based application designed to provide users with comprehensive information about various travel destinations. The application allows users to browse destinations, view details, and manage their profiles. The project is built using Python, PostgreSQL, HTML, CSS, and JavaScript, focusing on clean design and user-friendly functionality.

Features
User Authentication: Secure Signin and Signup pages to allow users to create accounts and access personalized content.
Profile Management: Users can view and update their profiles.
Destination Browsing: A 'Destinations' page that displays a list of all available travel destinations.
Detailed Destination Information: Each destination has detailed information, including location, description, and other relevant details.
Consistent UI/UX: The application maintains a consistent design across all pages with smooth transitions and a cohesive color scheme.
Technologies Used
Backend:

Python: Core logic and handling of server-side functionality.
PostgreSQL: Database management system to store and retrieve data.
Psycopg2: Python adapter for PostgreSQL to interact with the database.
Frontend:

HTML5: Structure of the web pages.
CSS3: Styling of the web pages, with specific files for Signin (signin.css) and Signup (signup.css) pages.
JavaScript: Enhances interactivity on the web pages.

Database Schema
The application uses a PostgreSQL database with the following key tables:

Users Table:-
user_id: Primary key, unique identifier for each user.
username: The username of the user.
email: The email address of the user.
password: The hashed password of the user.

Place Table:-
place_id: Primary key, unique identifier for each destination.
name: The name of the destination.
location: The geographical location of the destination.
description: A detailed description of the destination.
