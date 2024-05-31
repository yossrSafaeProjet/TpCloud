import sqlite3
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# Définir le chemin de la base de données
db_path = os.path.join(os.path.dirname(__file__), 'ma_base_de_donnees.db')

# Configuration de l'URL de la base de données SQLite
DATABASE_URL = f"sqlite:///{db_path}"

# Création de la base de données et connexion
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()
# Création de la base de données
try:
    db = sqlite3.connect(db_path)
    print("Base de données créée avec succès")
    # Création d'un curseur
    cursor = db.cursor()
    # Création de la table categorie
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        )
    ''')
    print("Table 'categories' créée avec succès")
    # Création de la table produit
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (id)    
        )
    ''')
    print("Table 'produit' créée avec succès")
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_name ON produit (name)
    ''')
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_description ON produit (description)
    ''')

    # Validation des changements
    db.commit()
except sqlite3.Error as e:
    print(f"Erreur lors de la création de la base de données: {e}")
finally:
    # Fermeture de la base de données
    if db:
        db.close()
        print("Base de données fermée avec succès")
