import mysql.connector
from mysql.connector import Error

# Database connection configuration
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies"
}

try:
    # Create connection
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    
    # Query 1: Select all fields from studio table
    print("-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}")
        print()
    
    # Query 2: Select all fields from genre table
    print("-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}")
        print()
    
    # Query 3: Select movie names with runtime less than 2 hours (120 minutes)
    print("-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()
    for film in short_films:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}")
        print()
    
    # Query 4: Select film names and directors, grouped by director
    print("-- DISPLAYING Director RECORDS in Order --")
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director, film_name")
    director_films = cursor.fetchall()
    for film in director_films:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print()

except Error as e:
    print(f"Error: {e}")

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()