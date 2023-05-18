#!/bin/bash

mysql -h localhost -P 3306 -u root -p'supersecretpassword123' -D dbstime --protocol=tcp < ./database/insert_dml.sql

if [ $? -eq 0 ]; then
    echo "Stime database successfully populated !"
else
    echo "Something when wrong while populating Stime database :/"
fi