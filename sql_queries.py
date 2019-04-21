# DROP TABLES

songplay_table_drop = "drop table if exists song_plays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS song_plays (songplay_id serial primary key, start_time varchar NOT NULL, user_id varchar NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id varchar primary key not null, first_name varchar, last_name varchar, gender varchar, level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar primary key not null, title varchar, artist_id varchar, year int, duration numeric)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar primary key not null, name varchar, location varchar, lattitude numeric, longitude numeric)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time varchar primary key not null, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO song_plays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO UPDATE
SET level = EXCLUDED.level
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, lattitude, longitude) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id)
DO NOTHING
""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time)
DO NOTHING
""")


# FIND SONGS

song_select = ("""select s.song_id, a.artist_id from songs as s
join artists as a
on a.artist_id = s.artist_id
where title = (%s) and name = (%s) and duration=(%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
