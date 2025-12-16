# Aplikasi Manajemen Pengguna (User Management System)

Aplikasi ini adalah sistem manajemen pengguna sederhana namun aman yang dibangun menggunakan arsitektur **Frontend-Backend separation**. Aplikasi ini memungkinkan fitur Login, Register, dan CRUD data pengguna yang terautentikasi.
## 🛠️ Tech Stack

**Frontend:**
* **Vue.js 3** (Composition API)
* **Vite** (Build tool)
* **Pinia** (State Management)
* **Axios** (HTTP Client)
* **Vue Router** (Navigasi)

**Backend:**
* **Python Flask** (Web Framework)
* **SQLAlchemy** (ORM)
* **PostgreSQL** (Database)

---

## 🗄️ Skema Database

Aplikasi ini menggunakan database **PostgreSQL**. Berikut adalah struktur tabel utama `users`:

### Tabel: `users`

| Nama Kolom | Tipe Data | Constraint / Keterangan |
| :--- | :--- | :--- |
| **id** | `BIGINT` | **Primary Key**, Auto Increment |
| **username** | `VARCHAR(50)` | Not Null, **Unique** (Tidak boleh duplikat) |
| **password** | `VARCHAR(255)` | Not Null (Disimpan sebagai Hash/Encrypted) |
| **email** | `VARCHAR(100)` | Not Null, **Unique** |
| **nama** | `VARCHAR(100)` | Not Null |
| **created_at**| `TIMESTAMP` | Default: `CURRENT_TIMESTAMP` |

---

## 🚀 Cara Menjalankan Project 

### Prasyarat
Pastikan Anda sudah menginstal:
* [Node.js](https://nodejs.org/) & npm
* [Python](https://www.python.org/) (versi 3.8 ke atas)
* [PostgreSQL](https://www.postgresql.org/)
* Git

### 1. Clone Repository
Buka terminal dan clone repository ini:

```bash
git clone https://github.com/lhanif/horus-hanif-exam
cd horus-hanif-exam
```
### 2. Setup Database
#### a. Buat Database di PostgreSQL 

### 3. Setup Backend
#### a. Masuk ke folder Backend
```
cd Backend
```
#### b. Buat Virtual Environment (agar library tidak tercampur)
```
python -m venv venv
```
* Windows : venv\Scripts\activate
#### c. Install Dependencies
```
pip install -r requirements.txt
```
#### d. Sesuaikan Environment Variables (buat file .env)
```
JWT_SECRET_KEY=jwt-secret-key
DATABASE_URL=postgresql://username:password@localhost:5432/db_name
```
#### e. Jalankan Migrasi Database
```
flask db upgrade
```
#### f. Jalankan Flask (Backend)
```
python run.py
```
### 4. Setup Frontend
#### a. Masuk ke Folder Frontend
```
cd Frontend
```

#### b. Install Dependencies
```
npm install
```

#### c. Sesuaikan Environment Variables (buat file .env)
```
VITE_API_URL=http://localhost:PORT || backend URL
```
#### d. Jalankan Frontend
```
npm run dev
```
### 5. Lainnya

#### a. DDL SQL untuk membuat tabel database (apabila migrasi tidak berhasil)
```
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    nama VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```