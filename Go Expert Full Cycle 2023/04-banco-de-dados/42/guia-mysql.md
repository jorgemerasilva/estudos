
docker compose up -d
docker compose ps


docker exec -it mysql bash


mysql -uroot -p goexpert


create table products (id varchar(255), name varchar(255), price decimal(10,2), primary key(id));