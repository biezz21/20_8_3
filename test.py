import time
from w1thermsensor import W1ThermSensor
import pymysql


sensor = W1ThermSensor()

conn = pymysql.connect(host='203.255.24.98', port=3306, user='root', passwd='7890uiop', db='rasp_db', charset='utf8')

try:
    with conn.cursor () as cur:
        sql = 'insert into temp_tb (time, temperature) values(%s, %s)'

        while True:

            temperature = sensor.get_temperature()
            cur.execute(sql, (time.strftime("%Y-%m-%d %H:%m:%S", time.localtime()), temperature))
            conn.commit()
            print('%s' % temperature)
            time.sleep(1800)
except KeyboardInterrupt:
    pass
