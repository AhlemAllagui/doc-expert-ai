
import os
from flask import Flask, jsonify
import psycopg
from dotenv import load_dotenv

app = Flask(__name__)

# Charger les variables du fichier .env
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.route('/api/home')
def bonjour():
    return 'Bonjour, les amis !'

@app.route('/api/documents', methods=['GET'])
def get_documents():
    conn = get_db_connection()

    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, filename, created_at FROM documents ORDER BY id DESC"
            )
            rows = cur.fetchall()

        documents = [
            {
                "id": row[0],
                "filename": row[1],
                "created_at": row[2].isoformat() if row[2] else None
            }
            for row in rows
        ]

        return jsonify(documents)

    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
