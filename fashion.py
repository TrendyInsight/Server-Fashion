import json
import sqlite3

class FashionApp:
    def __init__(self):
        self.conn = sqlite3.connect("fashion.db")
        self.cursor = self.conn.cursor()
        self.create_tables()  # Panggil fungsi ini untuk membuat tabel jika belum ada

    def create_tables(self):
        with open('fashion.sql', 'r') as sqlfile:  # Pastikan nama file dan pathnya sesuai
            sqlscript = sqlfile.read()
        self.cursor.executescript(sqlscript)
        self.conn.commit()  # Simpan perubahan ke database


    def save_jenis_baju(self, id_jenis, atasan, bawahan, kerudung, gamis): 
        try: 
            self.cursor.execute
            ("INSERT INTO jenis_baju (id_jenis, atasan, bawahan, kerudung, gamis) VALUES (?, ?, ?, ?, ?)", 
             (id_jenis, atasan, bawahan, kerudung, gamis)
            )
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False

    def save_rekomendasi(self, id_rekom, rating, warna, foto_rek): 
        try: 
            self.cursor.execute
            ("INSERT INTO rekomendasi (id_rekom, rating, warna, foto_rek) VALUES (?, ?, ?, ?)", 
             (id_rekom, rating, warna, foto_rek)
            )
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False

    def save_outfit(self, id_outfit, foto, date): 
        try: 
            self.cursor.execute
            ("INSERT INTO outfit (id_outfit, foto, date) VALUES (?, ?, ?)", 
             (id_outfit, foto, date)
            )
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False
