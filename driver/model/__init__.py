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
        query = "SELECT id, sensor_mac, plug_mac, plug_ip, preset_temp, location_name FROM node"
        return self.dict_fetch_all(query)

    def add_temperature(self, mac, temp, humidity, battery, sent_at):
        with self.conn.cursor() as cursor:
            query = "INSERT INTO temperature (mac, temp, humidity, battery, sent_at) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (mac, temp, humidity, battery, sent_at))

    def set_plug_ip(self, plug_mac, plug_ip):
        with self.conn.cursor() as cursor:
            query = "UPDATE node SET plug_ip = %s WHERE plug_mac = %s"
            cursor.execute(query, (plug_ip, plug_mac))

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
