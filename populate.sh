#!/bin/bash

mysql -h localhost -P 3306 -u'op01' -p'pa55w0rd' -D dbstime --protocol=tcp < ./database/stime_dml.sql

if [ $? -eq 0 ]; then
    echo "Stime database successfully populated !"
else
    echo "Something went wrong while populating Stime database :/"
fi