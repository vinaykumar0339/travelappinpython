-- Sample Data for Places
INSERT INTO Place (name, location, description, cost, image_url) VALUES
('Eiffel Tower', 'Paris, France', 'Iconic wrought-iron lattice tower.', 25.00, 'https://example.com/images/eiffel_tower.jpg'),
('Great Wall of China', 'Beijing, China', 'Ancient series of walls and fortifications.', 30.00, 'https://example.com/images/great_wall.jpg'),
('Machu Picchu', 'Peru', 'Incan citadel set high in the Andes Mountains.', 40.00, 'https://example.com/images/machu_picchu.jpg');

-- Sample Data for Hotels
INSERT INTO Hotels (name, location, place, price_per_night, available_rooms) VALUES
('Hotel Paris', 'Paris, France', 1, 150.00, 10),
('Beijing Grand Hotel', 'Beijing, China', 2, 120.00, 5),
('Machu Picchu Sanctuary Lodge', 'Peru', 3, 200.00, 8);

-- Sample Data for Cart
INSERT INTO Cart (user_id, place_id, people, days) VALUES
(3, 1, 2, 3),
(3, 2, 1, 5),
(3, 3, 4, 2);

-- Sample Data for Hotel Bookings
INSERT INTO hotel_bookings (user_id, hotel_id, check_in_date, check_out_date, number_of_rooms, total_price) VALUES
(3, 1, '2024-05-01', '2024-05-05', 1, 600.00),
(3, 2, '2024-06-10', '2024-06-15', 2, 600.00),
(3, 3, '2024-07-20', '2024-07-25', 1, 1000.00);