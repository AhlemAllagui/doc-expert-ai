
import os

from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg

# Créer l'application Flask
app = Flask(__name__)

# Autoriser Vue.js à communiquer avec Flask
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:5173",
            "http://localhost:5174"
        ]
    }
})

# Charger les variables du fichier .env
load_dotenv(
    os.path.join(os.path.dirname(__file__), ".env")
)


# Connexion à PostgreSQL
def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


# Vérifier que Flask fonctionne
@app.route("/api/home", methods=["GET"])
def bonjour():
    return jsonify({
        "message": "Bonjour, les amis !",
        "status": "success"
    })


# Récupérer les documents depuis PostgreSQL
@app.route("/api/documents", methods=["GET"])
def get_documents():
    conn = get_db_connection()

    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, filename, created_at
                FROM documents
                ORDER BY id DESC
            """)

            rows = cur.fetchall()

        documents = [
            {
                "id": row[0],
                "filename": row[1],
                "created_at": (
                    row[2].isoformat() if row[2] else None
                )
            }
            for row in rows
        ]

        return jsonify(documents)

    except psycopg.Error:
        app.logger.exception(
            "Erreur lors de la récupération des documents"
        )
        return jsonify({
            "error": "Impossible de récupérer les documents."
        }), 500

    finally:
        conn.close()


# Démarrer le serveur Flask
if __name__ == "__main__":
    app.run(debug=True, port=5000)
