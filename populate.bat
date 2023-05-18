@echo off

mysql -h localhost --user=root --password=supersecretpassword123 --database=dbstime < %~dp0\database\insert_dml.sql

if %ERRORLEVEL% neq 0
    echo "Stime database successfully populated !"
else
    echo "Something when wrong while populating Stime database :/"