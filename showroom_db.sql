-- ======================================
-- Database: showroom_db
-- Tabel: cars, transaction
-- DBMS: MySQL
-- ======================================

DROP DATABASE IF EXISTS showroom_db;
CREATE DATABASE showroom_db;
USE showroom_db;

-- ======================================
-- 1. TABLE: cars
-- ======================================
DROP TABLE IF EXISTS cars;
CREATE TABLE cars (
    id_mobil INT PRIMARY KEY,
    merk VARCHAR(100) NOT NULL,
    Jenis_mobil ENUM('listrik', 'bensin') NOT NULL,
    Harga_beli DECIMAL(15,2) NOT NULL,
    Harga_jual DECIMAL(15,2) NOT NULL
);

INSERT INTO cars (id_mobil, merk, Jenis_mobil, Harga_beli, Harga_jual) VALUES
(1, 'Toyota Avanza', 'bensin', 210000000.00, 235000000.00),
(2, 'Honda Brio', 'bensin', 165000000.00, 185000000.00),
(3, 'Suzuki Ertiga', 'bensin', 225000000.00, 248000000.00),
(4, 'Mitsubishi Xpander', 'bensin', 255000000.00, 280000000.00),
(5, 'Daihatsu Xenia', 'bensin', 205000000.00, 228000000.00),
(6, 'Toyota Rush', 'bensin', 250000000.00, 275000000.00),
(7, 'Honda HR-V', 'bensin', 320000000.00, 348000000.00),
(8, 'Wuling Alvez', 'bensin', 240000000.00, 262000000.00),
(9, 'Hyundai Creta', 'bensin', 285000000.00, 310000000.00),
(10, 'Mazda CX-3', 'bensin', 355000000.00, 382000000.00),
(11, 'Toyota bZ4X', 'listrik', 1080000000.00, 1150000000.00),
(12, 'Hyundai Ioniq 5', 'listrik', 690000000.00, 735000000.00),
(13, 'Wuling Air EV', 'listrik', 185000000.00, 210000000.00),
(14, 'Nissan Leaf', 'listrik', 620000000.00, 665000000.00),
(15, 'MG 4 EV', 'listrik', 410000000.00, 445000000.00),
(16, 'BYD Dolphin', 'listrik', 360000000.00, 395000000.00),
(17, 'BYD Atto 3', 'listrik', 470000000.00, 510000000.00),
(18, 'Chery Omoda E5', 'listrik', 445000000.00, 485000000.00),
(19, 'Kia EV6', 'listrik', 1180000000.00, 1265000000.00),
(20, 'Tesla Model 3', 'listrik', 1320000000.00, 1415000000.00);

-- ======================================
-- 2. TABLE: transaction
-- Catatan: transaction adalah keyword khusus,
-- jadi dipakai dengan backtick (`transaction`)
-- ======================================
DROP TABLE IF EXISTS `transaction`;
CREATE TABLE `transaction` (
    id_dijual INT PRIMARY KEY,
    merk VARCHAR(100) NOT NULL,
    Harga_jual DECIMAL(15,2) NOT NULL,
    di_bayar DECIMAL(15,2) NOT NULL,
    pembeli VARCHAR(100) NOT NULL,
    CONSTRAINT fk_transaction_car FOREIGN KEY (id_dijual) REFERENCES cars(id_mobil)
);

INSERT INTO `transaction` (id_dijual, merk, Harga_jual, di_bayar, pembeli) VALUES
(1, 'Toyota Avanza', 235000000.00, 235000000.00, 'Andi Saputra'),
(2, 'Honda Brio', 185000000.00, 185000000.00, 'Budi Santoso'),
(3, 'Suzuki Ertiga', 248000000.00, 248000000.00, 'Citra Lestari'),
(4, 'Mitsubishi Xpander', 280000000.00, 280000000.00, 'Dewi Anggraini'),
(5, 'Daihatsu Xenia', 228000000.00, 228000000.00, 'Eko Prasetyo'),
(6, 'Toyota Rush', 275000000.00, 275000000.00, 'Fajar Nugroho'),
(7, 'Honda HR-V', 348000000.00, 348000000.00, 'Gina Maharani'),
(8, 'Wuling Alvez', 262000000.00, 262000000.00, 'Hendra Wijaya'),
(9, 'Hyundai Creta', 310000000.00, 310000000.00, 'Intan Permata'),
(10, 'Mazda CX-3', 382000000.00, 382000000.00, 'Joko Susilo'),
(11, 'Toyota bZ4X', 1150000000.00, 1150000000.00, 'Kevin Pradana'),
(12, 'Hyundai Ioniq 5', 735000000.00, 735000000.00, 'Lina Marlina'),
(13, 'Wuling Air EV', 210000000.00, 210000000.00, 'Maya Sari'),
(14, 'Nissan Leaf', 665000000.00, 665000000.00, 'Nanda Putra'),
(15, 'MG 4 EV', 445000000.00, 445000000.00, 'Oki Firmansyah'),
(16, 'BYD Dolphin', 395000000.00, 395000000.00, 'Putri Amelia'),
(17, 'BYD Atto 3', 510000000.00, 510000000.00, 'Rahmat Hidayat'),
(18, 'Chery Omoda E5', 485000000.00, 485000000.00, 'Salsa Aulia'),
(19, 'Kia EV6', 1265000000.00, 1265000000.00, 'Teguh Prakoso'),
(20, 'Tesla Model 3', 1415000000.00, 1415000000.00, 'Vina Oktavia');

-- ======================================
-- Cek data
-- ======================================
SELECT * FROM cars;
SELECT * FROM `transaction`;



