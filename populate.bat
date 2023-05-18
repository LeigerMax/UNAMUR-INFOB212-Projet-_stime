@echo off

mysql -h localhost --user=root --password=supersecretpassword123 --database=dbstime < %~dp0\database\insert_dml.sql

if %ERRORLEVEL% neq 0 (
    echo "Something went wrong while populating the Stime database :/"
) else (
    echo "Stime database successfully populated!"
)