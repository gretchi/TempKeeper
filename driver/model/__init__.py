import psycopg2
import psycopg2.extras


class Model(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            host="pgsql",
            port="5432",
            dbname="tkdb",
            user="system",
            password="system",
        )

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def dict_cursor(self):
        return self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def dict_fetch_all(self, query, values=()):
        with self.dict_cursor() as cursor:
            cursor.execute(query, values)
            results = []
            for row in cursor.fetchall():
                results.append(dict(row))
            return results

    def get_nodes(self):
        query = "SELECT id, sensor_mac, plug_mac, plug_ip, preset_temp, location_name FROM node ORDER BY id ASC"
        return self.dict_fetch_all(query)

    def get_nodes_summary(self):
        query = """SELECT
                n.id,
                n.sensor_mac,
                n.plug_mac,
                n.plug_ip,
                n.preset_temp,
                n.location_name,
                (
                    SELECT
                        p.status
                    FROM
                        plug_state AS p
                    WHERE n.plug_mac = p.mac
                    ORDER BY p.id DESC LIMIT 1
                ) AS status,
                (
                    SELECT t.temp
                    FROM temperature as t
                    WHERE t.mac = n.sensor_mac
                    ORDER BY sent_at DESC LIMIT 1
                ) as current_temp
            FROM node AS n
            ORDER BY id ASC"""
        return self.dict_fetch_all(query)

    def get_nodes_order_by_random(self):
        query = "SELECT id, sensor_mac, plug_mac, plug_ip, preset_temp, location_name FROM node ORDER BY RANDOM()"
        return self.dict_fetch_all(query)

    def add_temperature(self, mac, temp, humidity, battery, sent_at):
        with self.conn.cursor() as cursor:
            query = "INSERT INTO temperature (mac, temp, humidity, battery, sent_at) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (mac, temp, humidity, battery, sent_at))

    def set_plug_ip(self, plug_mac, plug_ip):
        with self.conn.cursor() as cursor:
            query = "UPDATE node SET plug_ip = %s WHERE plug_mac = %s"
            cursor.execute(query, (plug_ip, plug_mac))

    def set_preset_temp(self, id, preset_temp):
        with self.conn.cursor() as cursor:
            query = "UPDATE node SET preset_temp = %s WHERE id = %s"
            cursor.execute(query, (preset_temp, id))

    def set_node(self, id, sensor_mac, plug_mac, preset_temp, location_name):
        with self.conn.cursor() as cursor:
            query = "UPDATE node SET sensor_mac = %s, plug_mac = %s, preset_temp = %s, location_name = %s WHERE id = %s"
            cursor.execute(query, (sensor_mac, plug_mac,
                           preset_temp, location_name, id))

    def get_temperature_one(self, mac):
        with self.conn.cursor() as cursor:
            query = "SELECT mac, temp, humidity, battery, sent_at FROM temperature  WHERE mac = %s ORDER BY sent_at DESC LIMIT 1"
            return self.dict_fetch_all(query, (mac, ))[0]

    def add_plug_state(self, mac, status, sent_at):
        with self.conn.cursor() as cursor:
            query = (
                "INSERT INTO plug_state (mac, status, sent_at) VALUES (%s, %s, %s)"
            )
            cursor.execute(query, (mac, status, sent_at))
