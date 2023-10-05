-- Buat database
CREATE DATABASE IF NOT EXISTS fashion;
USE fashion;

-- Tabel jenis_baju
CREATE TABLE IF NOT EXISTS jenis_baju (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
	atasan VARCHAR(20),
    bawahan VARCHAR(20),
	kerudung VARCHAR(20),
	gamis VARCHAR(20)
);

-- Tabel outfit
CREATE TABLE IF NOT EXISTS outfit (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
	foto BLOB,
	tanggal CURRENT_TIMESTAMP,
    id_jenis INTEGER,
    FOREIGN KEY (id_jenis) REFERENCES jenis_baju (id),
);

-- Tabel rekomendasi
CREATE TABLE IF NOT EXISTS rekomendasi (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
	rating VARCHAR(20),
    warna VARCHAR(20),
	foto_rek VARCHAR(20)
);
