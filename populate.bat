@echo off

mysql -h localhost --user=op01 --password=pa55w0rd --database=dbstime < %~dp0\database\stime_dml.sql

if %ERRORLEVEL% neq 0 (
    echo "Something went wrong while populating the Stime database :/"
) else (
    echo "Stime database successfully populated!"
)