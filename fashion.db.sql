BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "jenis_baju" (
	"id_jenis"	INTEGER UNIQUE,
	"atasan"	TEXT,
	"bawahan"	TEXT,
	"kerudung"	TEXT,
	"gamis"	TEXT,
	PRIMARY KEY("id_jenis")
);
CREATE TABLE IF NOT EXISTS "rekomendasi" (
	"id_rekom"	INTEGER UNIQUE,
	"rating"	TEXT,
	"warna"	TEXT,
	"foto_rek"	TEXT,
	PRIMARY KEY("id_rekom")
);
CREATE TABLE IF NOT EXISTS "outfit" (
	"id_outfit"	INTEGER NOT NULL,
	"foto"	TEXT NOT NULL,
	"date"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id_outfit" AUTOINCREMENT)
);
INSERT INTO "outfit" VALUES (1,'','2023-09-21 01:34:12');
COMMIT;
