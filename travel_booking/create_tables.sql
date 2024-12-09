-- create_tables.sql

-- Create Users Table
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create Place Table
CREATE TABLE Place (
    place_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    image_url VARCHAR(255)
);

-- Create Cart Table
CREATE TABLE Cart (
    cart_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE,
    place_id INT REFERENCES Place(place_id) ON DELETE CASCADE,
    people INT NOT NULL,
    days INT NOT NULL
);

-- Create Hotels Table
CREATE TABLE Hotels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    place INT REFERENCES Place(place_id) ON DELETE CASCADE,
    price_per_night DECIMAL(10, 2) NOT NULL,
    available_rooms INT NOT NULL
);

-- Create Hotel Bookings Table
CREATE TABLE hotel_bookings (
    booking_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE,
    hotel_id INT REFERENCES Hotels(id) ON DELETE CASCADE,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    number_of_rooms INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL
);