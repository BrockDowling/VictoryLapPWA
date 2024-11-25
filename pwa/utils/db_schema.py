import os
from psycopg import connect
from dotenv import load_dotenv


base_dir = os.path.dirname(os.path.abspath(__file__))  # Current script's directory (e.g., pwa/utils)
project_dir = os.path.dirname(os.path.dirname(base_dir))  # Move two levels up to VictoryLapPWA

# Construct the path to the .env file
dotenv_path = os.path.join(project_dir, '.env')

# Load the .env filess
load_dotenv(dotenv_path=dotenv_path)

def list_tables():
    try:
        # Get the database URL from .env
        database_url = os.getenv("DATABASE_URL")

        if not database_url:
            raise ValueError("DATABASE_URL is not set in .env")

        # Connect to the database
        with connect(database_url) as conn:
            with conn.cursor() as cur:
                # Query to list all tables in the current database schema
                cur.execute("""
                    SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema = 'public'
                    ORDER BY table_name;
                """)
                tables = cur.fetchall()
                if not tables:
                    print("No tables found in the database.")
                    return

                print("Tables and their columns in the database:")
                for table in tables:
                    table_name = table[0]
                    print(f"\nTable: {table_name}")

                    # Query to get columns for each table
                    cur.execute("""
                        SELECT column_name, data_type
                        FROM information_schema.columns
                        WHERE table_name = %s
                        ORDER BY ordinal_position;
                    """, (table_name,))
                    columns = cur.fetchall()

                    if columns:
                        for column in columns:
                            column_name, data_type = column
                            print(f"  - {column_name} ({data_type})")
                    else:
                        print("  No columns found.")
    except Exception as e:
        print(f"Error: {e}")
# Run the function
if __name__ == "__main__":
    list_tables()
