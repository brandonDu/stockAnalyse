import psycopg2
# 注册字符串缺省类型为unicode
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import psycopg2.pool

def test_insert():
         no = 'sz000623'
         name='吉林敖东'
         return {'no':no,'name':name}

unit = test_insert()

dsn = "host=localhost dbname=stock user=postgres password=postgres"
pool = psycopg2.pool.ThreadedConnectionPool( minconn=2,maxconn=10, dsn=dsn)
conn = pool.getconn()
try:
         with conn.cursor() as cur:                
                  sql = "insert into stock_inf (no,name) values (%(no)s,%(name)s);"
                  cur.execute(sql,unit)
                  conn.commit()
                  
finally:
         pool.putconn(conn)
##cur.execute('''
##INSERT INTO test_tbl1 (sn, name) VALUES (%(sn)s, %(name)s)
##''', {'sn':sn, 'name':name} )


