-- Sample Data
-- Add diverse books
INSERT INTO Book (Title, Author, Genre, PublicationYear, Synopsis) VALUES
('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951, 'A young man struggles with adolescence.'),
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, 'A young girl confronts racism in the American South.'),
('1984', 'George Orwell', 'Dystopian', 1949, 'A chilling depiction of a totalitarian regime.'),
('Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 'A tale of love and social standing in 19th-century England.'),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 1925, 'The story of Jay Gatsby and the American dream.'),
('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'Non-Fiction', 2011, 'A history of humanity from ancient times to the present.'),
('Dune', 'Frank Herbert', 'Science Fiction', 1965, 'A young man becomes the leader of a desert planet.'),
('Beloved', 'Toni Morrison', 'Historical Fiction', 1987, 'A former slave is haunted by her past.'),
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, 'A hobbit embarks on a quest to reclaim a treasure.'),
('The Da Vinci Code', 'Dan Brown', 'Thriller', 2003, 'A symbologist unravels a mystery hidden in art and history.'),
('The Fault in Our Stars', 'John Green', 'Young Adult', 2012, 'Two teens with cancer fall in love.'),
('The Art of War', 'Sun Tzu', 'Philosophy', -500, 'A classic treatise on military strategy.'),
('Becoming', 'Michelle Obama', 'Memoir', 2018, 'The life story of the former First Lady of the United States.'),
('Invisible Man', 'Ralph Ellison', 'Fiction', 1952, 'An exploration of race and identity in America.'),
('Crying in H Mart', 'Michelle Zauner', 'Memoir', 2021, 'A memoir about food, family, and loss.'),
('The Road', 'Cormac McCarthy', 'Post-Apocalyptic', 2006, 'A father and son journey through a devastated world.'),
('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 'Fantasy', 1997, 'A boy discovers he is a wizard and attends a magical school.'),
('The Book Thief', 'Markus Zusak', 'Historical Fiction', 2005, 'A girl steals books in Nazi Germany.'),
('Educated', 'Tara Westover', 'Memoir', 2018, 'A woman grows up in a strict family and seeks education.'),
('Things Fall Apart', 'Chinua Achebe', 'Historical Fiction', 1958, 'The story of a man in colonial Nigeria.'),
('The Alchemist', 'Paulo Coelho', 'Adventure', 1988, 'A shepherd follows his dream to find treasure.'),
('The Kite Runner', 'Khaled Hosseini', 'Fiction', 2003, 'A tale of friendship and redemption in Afghanistan.'),
('The Joy Luck Club', 'Amy Tan', 'Fiction', 1989, 'The lives of Chinese-American women and their mothers.'),
('The Silent Patient', 'Alex Michaelides', 'Psychological Thriller', 2019, 'A therapist tries to unlock the mystery of a silent patient.');

-- Add diverse users
INSERT INTO User (Username, Password, Email) VALUES
('booklover101', 'password123', 'booklover101@example.com'),
('avidreader', 'securepass', 'avidreader@example.com'),
('literaturegeek', 'litpass123', 'literaturegeek@example.com'),
('sci-fi_addict', 'spaceships', 'scifi.addict@example.com'),
('historian', 'historybuff', 'historian@example.com'),
('youngatheart', 'ya_reads', 'youngatheart@example.com'),
('thrillseeker', 'thrillsnchills', 'thrillseeker@example.com'),
('memoirhunter', 'memoirfan', 'memoirhunter@example.com'),
('fantasyworld', 'magicforever', 'fantasyworld@example.com'),
('philosophical', 'deepthoughts', 'philosophical@example.com');

-- Add diverse recommendations
INSERT INTO Recommendation (UserID, BookID, RecommendationText, DateRecommended) VALUES
(1, 3, 'A must-read for anyone curious about dystopian societies.', '2024-10-01'),
(2, 7, 'This is the definitive sci-fi classic. Highly recommended!', '2024-10-05'),
(3, 4, 'Jane Austen never fails to deliver a compelling story.', '2024-10-10'),
(4, 17, 'A magical start to an epic journey. Great for any fantasy fan.', '2024-10-15'),
(5, 19, 'Heartbreaking and inspiring memoir. Truly eye-opening.', '2024-10-20'),
(6, 11, 'An emotional rollercoaster with relatable characters.', '2024-10-25'),
(7, 10, 'Twists and turns that will keep you hooked until the end!', '2024-11-01'),
(8, 14, 'A modern memoir with a heartfelt story about family and food.', '2024-11-06'),
(9, 8, 'Beautifully written and deeply moving historical fiction.', '2024-11-10'),
(10, 22, 'A timeless story of courage and perseverance.', '2024-11-15'),
(1, 2, 'A profound and beautifully written story about morality and justice.', '2024-11-18'),
(2, 20, 'A brilliant exploration of cultural identity and community.', '2024-11-20'),
(3, 6, 'A fascinating journey through human history.', '2024-11-22'),
(4, 23, 'A story of hope, resilience, and redemption. Unforgettable.', '2024-11-23'),
(5, 13, 'Inspiring and uplifting story of a remarkable journey.', '2024-11-24'),
(6, 16, 'A haunting and poetic tale of survival and hope.', '2024-11-25'),
(7, 9, 'A classic adventure that has stood the test of time.', '2024-11-26'),
(8, 1, 'A thought-provoking novel about adolescence and identity.', '2024-11-26'),
(9, 5, 'A poignant tale of ambition and the cost of the American dream.', '2024-11-26'),
(10, 18, 'Perfect for fans of coming-of-age and magical worlds.', '2024-11-26');
