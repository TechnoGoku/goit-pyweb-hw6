from faker import Faker
import random
import psycopg2

fake = Faker()

conn = psycopg2.connect(host="localhost", database="hw6", user="postgres", password="567234")
cur = conn.cursor()

for _ in range(3):
    cur.execute("INSERT INTO groups (name) VALUES (%s)", (fake.word(),))

for teacher_id in range(1, 4):
    for _ in range(2):
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (fake.word(), teacher_id))


