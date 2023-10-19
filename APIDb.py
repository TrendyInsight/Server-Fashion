from flask import Flask, jsonify
import sqlite3

def connect_to_database():
    conn = sqlite3.connect("fashion.db")
    return conn

@app.route("/")
def index():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jenis_baju")
    jenis_baju = cursor.fetchall()
    cursor.execute("SELECT * FROM outfit")
    outfit = cursor.fetchall()
    cursor.execute("SELECT * FROM rekomendasi")
    rekomendasi = cursor.fetchall()
    return jsonify({
        "jenis_baju": jenis_baju,
        "outfit": outfit,
        "rekomendasi": rekomendasi
    })

if __name__ == "__main__":
    app.run()