import psycopg2
from psycopg2 import sql
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Class to handle database connections
class DatabaseConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
        except psycopg2.DatabaseError as e:
            logger.error(f"Database connection error: {str(e)}")
            raise e
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
        if exc_type is not None:
            logger.error("Exception occurred: %s", exc_value)
        print("Database connection closed.")

# Class to hold place details
class PlaceDetails:
    def __init__(self, place_id, name, location, description, cost, image_url, history=None):
        self.id = place_id
        self.name = name
        self.location = location
        self.description = description
        self.cost = cost
        self.image_url = image_url
        self.history = history or ""

    def __str__(self):
        return (f"place_id: {self.id}, Name: {self.name}, Description: {self.description[:60]}..., "
                f"Location: {self.location}, Cost: {self.cost}, Image URL: {self.image_url}")

# Class to manage places in the database
class Place:
    def __init__(self, host, database, user, password):
        self.db_params = (host, database, user, password)

    def fetch_places(self, search_term=None):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT place_id, name, location, description, cost, image_url FROM place"
            if search_term:
                query += " WHERE name ILIKE %s OR location ILIKE %s"
                cursor.execute(query, (f'%{search_term}%', f'%{search_term}%'))
            else:
                cursor.execute(query)
            places_data = cursor.fetchall()
            cursor.close()
        places = [PlaceDetails(*place_data) for place_data in places_data]
        return places or []

    def get_place_by_id(self, place_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT place_id, name, location, description, cost, image_url FROM place WHERE place_id = %s"
            cursor.execute(query, (place_id,))
            place_data = cursor.fetchone()
            cursor.close()
        if place_data:
            return PlaceDetails(*place_data)  # Ensure this fetches image_url
        return None

    def add_place(self, name, location, description, cost, image_url):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO place (name, location, description, cost, image_url)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, location, description, cost, image_url))
            conn.commit()
            cursor.close()

    def remove_place(self, place_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM place WHERE place_id = %s"
            cursor.execute(query, (place_id,))
            conn.commit()
            cursor.close()

# Class to manage user operations in the database
class User:
    def __init__(self, host, database, user, password):
        self.connection = psycopg2.connect(host=host, database=database, user=user, password=password)
        self.cursor = self.connection.cursor()
        self.db_params = (host, database, user, password)

    def authenticate(self, email, password):
        query = "SELECT * FROM Users WHERE email = %s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()
        if result and check_password_hash(result[3], password):
            return result[0]
        return None

    def get_user_name(self, user_id):
        query = "SELECT name FROM Users WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close(self):
        self.cursor.close()
        self.connection.close()

    def add_user(self, name, email, password):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            try:
                cursor.execute(query, (name, email, hashed_password))
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error("Error adding user: %s", str(e))
                raise e
            finally:
                cursor.close()

    def verify_user(self, email, password):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT password FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()
        if result and check_password_hash(result[0], password):
            return True
        return False

    def get_user(self, email):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT name, email FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()
        if result:
            return {"name": result[0], "email": result[1]}
        return None

    def update_user(self, current_email, name, email, password):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            hashed_password = generate_password_hash(password) if password else None
            query = "UPDATE users SET name = %s, email = %s"
            params = [name, email]
            if hashed_password:
                query += ", password = %s"
                params.append(hashed_password)
            query += " WHERE email = %s"
            params.append(current_email)
            try:
                cursor.execute(query, tuple(params))
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error("Error updating user: %s", str(e))
                raise e
            finally:
                cursor.close()

# Class to manage cart operations in the database
class Cart:
    def __init__(self, host, database, user, password):
        self.db_params = (host, database, user, password)

    def add_to_cart(self, user_id, place_id, people, days):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO cart (user_id, place_id, people, days)
                VALUES (%s, %s, %s, %s)
            """
            try:
                cursor.execute(query, (user_id, place_id, people, days))
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error("Error adding to cart: %s", str(e))
                raise e
            finally:
                cursor.close()

    def remove_from_cart(self, user_id, place_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM cart WHERE user_id = %s AND place_id = %s"
            try:
                cursor.execute(query, (user_id, place_id))
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error("Error removing from cart: %s", str(e))
                raise e
            finally:
                cursor.close()

    def get_cart_items(self, user_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = """
                SELECT p.name, p.description, p.location, p.image_url, c.people, c.days, p.place_id
                FROM cart c
                JOIN place p ON c.place_id = p.place_id
                WHERE c.user_id = %s
            """
            cursor.execute(query, (user_id,))
            cart_items = cursor.fetchall()
            cursor.close()
        return cart_items


class HotelDetails:
    def __init__(self, hotel_id, name, location, place, price_per_night):
        self.id = hotel_id
        self.name = name
        self.location = location
        self.place = place
        self.price_per_night = price_per_night
    def __str__(self):
        return (f"Hotel ID: {self.id}, Name: {self.name}, Location: {self.location}, "

                f"Place: {self.place}, Price per Night: {self.price_per_night}")
class Hotels:
    def __init__(self, db_host, db_database, db_user, db_password):
        self.db_host = db_host
        self.db_database = db_database
        self.db_user = db_user
        self.db_password = db_password
        self.db_params = (db_host, db_database, db_user, db_password)

    def fetch_hotels(self, search_term=None):
        query = "SELECT id, name, location, place, price_per_night, available_rooms FROM hotels"
        params = []

        if search_term:
            query += " WHERE name ILIKE %s OR location ILIKE %s"
            params = [f'%{search_term}%', f'%{search_term}%']

        with psycopg2.connect(
            host=self.db_host,
            database=self.db_database,
            user=self.db_user,
            password=self.db_password
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                hotels = cursor.fetchall()

        return hotels


    def add_hotel(self, name, location, place, price_per_night):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = """ 
                INSERT INTO hotels (name,location,place,price_per_night) 
                VALUES (%s, %s, %s,%s) 
            """
            cursor.execute(query, (name, location, place, price_per_night))
            conn.commit()
            cursor.close()
    def remove_hotel(self, hotel_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM hotels WHERE id = %s"
            cursor.execute(query, (hotel_id,))
            conn.commit()
            cursor.close()


class HotelBooking:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def get_connection(self):
        """Creates and returns a new database connection."""
        return psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def create_booking(self, user_id, hotel_id, check_in_date, check_out_date, number_of_rooms, total_price):
        """Inserts a new booking into the hotel_bookings table."""
        query = """
            INSERT INTO hotel_bookings (user_id, hotel_id, check_in_date, check_out_date, number_of_rooms, total_price)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (user_id, hotel_id, check_in_date, check_out_date, number_of_rooms, total_price)

        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()

    def get_bookings_by_user(self, user_id):
        """Fetches all bookings for a specific user from the hotel_bookings table."""
        query = "SELECT * FROM hotel_bookings WHERE user_id = %s"

        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (user_id,))
                return cur.fetchall()

    def get_available_hotels(self, check_in_date, check_out_date, number_of_rooms):
        """Fetches available hotels based on the provided dates and number of rooms."""
        query = """
            SELECT hotels.*
            FROM hotels
            LEFT JOIN hotel_bookings ON hotels.id = hotel_bookings.hotel_id
            WHERE hotels.available_rooms >= %s 
            AND (
                hotel_bookings.check_out_date <= %s 
                OR hotel_bookings.check_in_date >= %s 
                OR hotel_bookings.hotel_id IS NULL
            )
            GROUP BY hotels.id
        """
        params = (number_of_rooms, check_in_date, check_out_date)

        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                return cur.fetchall()