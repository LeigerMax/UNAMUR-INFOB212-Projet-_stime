
mysql -h localhost -P 3306 -u root -p'supersecretpassword123' -D dbstime --protocol=tcp < %~dp0\database\populate.sql