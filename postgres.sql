CREATE DATABASE stock
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'Chinese (Simplified)_People''s Republic of China.936'
       LC_CTYPE = 'Chinese (Simplified)_People''s Republic of China.936'
       CONNECTION LIMIT = -1;


drop table if exists stock_inf;
create table if not exists stock_inf(
	sn integer,
	no varchar(10),
	name text,
	info text,
	about text,
	primary key(sn)
);

create sequence seq_stock_inf_sn start 1 increment 1
owned by stock_inf.sn;

