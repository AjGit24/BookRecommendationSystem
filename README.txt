README
STUDENT NAME:
Ajaan Nalliah
STUDENT NUMBER:
101325463
PROJECT NAME:
Book Recommendation System
DESCRIPTION:
This is a Book Recommendation System that allows users to:
    1. Register and log in.
    2. View and search books in the database.
    3. Create and manage personalized reading lists.
The system is built with Python and SQLite3. Users can explore, rate, and organize books
through command-line interface (CLI).
DATABASE INFORMATION:
Database Filename - books_recommendation_system.db 
Location - The database file is located in the root directory of the project folder.
Accessing the Database - To manually examine the database using the SQLite3 command line tool:
    1. Open your terminal or command prompt.
    2. Run the following command:
        sqlite3 books_recommendation_system.db 
    3. User SQLite3 commands to explore the database. For example:
        * List tables:
        .tables
        * View schema:
        .schema
        * Query a table:
        SELECT * FROM Book LIMIT 10;
HOW TO RUN THE APPLICATION:
    1. Ensure Python3 and SQLite3 are installed on your system.
    2. Open a terminal or command prompt. 
    3. Navigate to the project directory.
    4. Run the application with the following command:
        python3 book_recommendation_system.py
IMPORTANT NOTES:
* The database file book_recommendation_system.db contains the prepopulated data used by the application.
* If you need to reset the database or initialize a new one, the schema and data SQL scripts
(schema.sql and data.sql) are included in the project.
