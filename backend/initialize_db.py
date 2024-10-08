import logging
import database

# Configure logging
logging.basicConfig(
    filename='app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_database_tables():
    try:
        # This function creates the necessary tables
        database.create_user_table()
        logging.info("Database tables were successfully created.")
    except Exception as e:
        logging.error(f"An error occurred while creating database tables: {e}")

# Run the function to create tables
create_database_tables()
