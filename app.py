from flask import Flask, jsonify
import sqlite3
#import pymysql

app = Flask(__name__)

def connect_to_database():
    conn = sqlite3.connect("fashion.db")
    return conn

@app.route("/")
def index():
    conn = connect_to_database()
    cursor = conn.cursor()

    # Query tabel jenis_baju
    cursor.execute("SELECT * FROM jenis_baju")
    jenis_baju = cursor.fetchall()

    # Query tabel outfit
    cursor.execute("SELECT * FROM outfit")
    outfit = cursor.fetchall()

    # Query tabel rekomendasi
    cursor.execute("SELECT * FROM rekomendasi")
    rekomendasi = cursor.fetchall()

    # Tutup koneksi database
    conn.close()

    # Koneksi ke database MariaDB
    #conn_mariadb = pymysql.connect(host='localhost', port=3306, user='root', password='', database='fashion')

    # Query di database MariaDB
    #cursor_mariadb = conn_mariadb.cursor()
    #cursor_mariadb.execute('SELECT * FROM users')
    #users = cursor_mariadb.fetchall()

    # Tutup koneksi database MariaDB
    #conn_mariadb.close()

    return jsonify({
        "jenis_baju": jenis_baju,
        "outfit": outfit,
        "rekomendasi": rekomendasi
    })

if __name__ == "__main__":
    app.debug = True
    app.run()
