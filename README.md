README.md

Description about the project:
The purpose of this project is to model data using postgres. The name of the project is Sparkify which is a start that collects data based on songs and user activity. The analytical direction of the start up is to understand why songs the users are listening to. Thus the project will enable to collect and process data to enable answering the business questions. The data is currently stored in a json file which cannot be translated in the hands of the analytics team. Those role here is to create a database that allows to understand and translate the file into a readable format.

Details about the schema, for example, the tables used, fields used:
The design will be based on the star schema approach where I will be using Fact and Dimensions. The benefit of using this is that it will help translate the data into business needs fairly quickly with simple joins and aggregations. It also allows ease of scalability i.e. adding new dimensions and allow managing the data marts without much issue(such as updating & inserts). The fact table(song_plays) will consists of keys that will allow easy joins with the dimension tables(users, songs, artists, time). Below is an text illustration of the tables and fields names along with the data-types(dtype):

    Fact Table & Fields:
    ---Table---
    song_plays  
    ---fields & dtype---
    songplay_id serial primary key, start_time varchar NOT NULL, user_id varchar NOT NULL,   level
    varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar


    Dimension Table:
    ---Table---
    users
    ---fields & dtype---
    user_id varchar primary key not null, first_name varchar, last_name varchar, gender varchar,
    level varchar
    ---Table---
    songs
    ---fields & dtype---
    song_id varchar primary key not null, title varchar, artist_id varchar, year int, duration numeric
    ---Table---
    artists
    ---fields & dtype---
    artist_id varchar primary key not null, name varchar, location varchar, lattitude numeric, longitude numeric
    ---Table---
    time
    ---fields & dtype---
    start_time varchar primary key not null, hour int, day int, week int, month int, year int, weekday int

Any special cases like how you are handling the duplicate scenarios:
'ON CONFLICT' and using primary keys will allow to keep the data integrety without comprising the risk of duplicate data for example on the insert statement for users, if a 'free user' has upgraded to a 'paid user' the ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level will run the insert for level as it has been excluded, which will allow to change the level from 'free' to 'paid' without inserting an entirely new records with the same data but with one column difference.

How to run the script on Jupyter:

Run create_tables.py to establish the connection to the database as this the most crucial step before running the etl:

Step 1:

%run create_tables.py

Step 2:
%run etl.py
