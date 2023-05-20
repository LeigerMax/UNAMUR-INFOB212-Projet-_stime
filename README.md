
![Generic badge](https://img.shields.io/badge/STATUT-DEV-blue.svg)   ![Generic badge](https://img.shields.io/badge/VERSION-0.0-green.svg) ![Generic badge](https://img.shields.io/badge/SCHOOL_PROJET-UNamur-green.svg)


# UNamur - Projet Base de données - Stime

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#-build-with">Build with</a></li>
  </ol>
</details>


## About The Project

## Requirements

- Python `3.10` or higher
- Docker Engine
- Docker Compose
- Docker Desktop (optional)

## Installation

### Windows
1. `git clone https://github.com/LeigerMax/UNAMUR-INFOB212-Projet-_stime` to clone the project
2. `dir UNAMUR-INFOB212-Projet-_stime` to change current directory
3. `python3 -m venv .env` to create a Python virtual environment
4. `.env\Scripts\activate.bat` to activate the virtual environment
5. `pip install -r requirements.txt` to install Python packages

### Linux
1. `git clone https://github.com/LeigerMax/UNAMUR-INFOB212-Projet-_stime` to clone the project
2. `cd UNAMUR-INFOB212-Projet-_stime` to change current directory
3. `python3 -m venv .env` to create a Python virtual environment
4. `source .env/bin/actiate` to activate the virtual environment
5. `pip install -r requirements.txt` to install Python packages
6. `docker-compose up` to launch the database
7. `python3 app/main.py` to run the program
8. `chmod +x populate.sh` to make the script executable


## Running the project

1. activate the virtual environment (via `.env`)
2. `docker-compose up` to launch the database service (can be launched via Docker Desktop)
3. `populate.bat`(Windows) or `populate.sh`(Linux) to populate the database
4. `python main.py` to run the program

## Stopping the project

1. `docker-compose stop` to stop the database service (can be stopped via Docker Desktop)
2. `deactivate` to exit the Python virtual environment

## Adminer
1. Go to "http://localhost:8000/"
2. Enter database connection information

## Authors
- [@LeigerMax](https://github.com/LeigerMax) 
- [@BenjaminPans](https://github.com/BenjaminPans) 
- [@PastoriLucas](https://github.com/PastoriLucas) 
- [@louisc-un](https://github.com/louisc-un)
- [@simo-ath](https://github.com/simo-ath)


## 🛠 Built with
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/)
- [MySQL](https://www.mysql.com/fr/)



