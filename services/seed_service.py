from config.base import session_factory
from sqlalchemy import text
from services.mission_service import get_all_targets


def create_tables():
    with session_factory() as session:
        session.execute(text("""
        create table if not exists country (
            country_id serial primary key,
            country_name varchar(100) unique not null
            );

            create table if not exists city (
            city_id serial primary key,
            city_name varchar(100) not null,
            country_id int ,
            foreign key (country_id) references country(country_id)
            );


            create table if not exists industry (
            industry_id serial primary key,
            industry_name varchar(255) unique not null
            );



            create table if not exists target_type(
            type_id serial primary key ,
            type_name varchar(100) unique not null 
            );


            create table if not exists target(
            target_id serial primary key,
            city_id int,
            industry_id int,
            type_id int,
            target_priority varchar(100),
            target_latitude NUMERIC(10, 6),                
            target_longitude NUMERIC(10, 6),   
            foreign key (city_id) references city(city_id),
            foreign key (type_id) references target_type(type_id),
            foreign key (industry_id) references industry(industry_id)
            );
        """))
        session.commit()


def insert_data():
    with session_factory() as session:
        session.execute(text("""
        insert into target_country (country_name)
            select distinct target_country
            FROM mission
            where target_country is not NULL
            on conflict (country_name) do nothing;


            insert into target_city (city_name, country_id)
            select distinct
                m.target_city,
                c.country_id
            from mission m
            join target_country c on m.target_country = c.country_name
            where m.target_city is not null;


            insert into target_industry (industry_name)
            select distinct target_industry
            from mission
            where target_industry is not null
            on conflict (industry_name) do nothing;
            
            
            insert into target_type (type_name)
            select distinct target_type
            from mission
            where mission.target_type IS NOT NULL
            on conflict (type_name) do nothing ;



            insert into target(city_id, industry_id, type_id, target_priority, target_latitude, target_longitude)
                select distinct
                c.city_id,
                i.industry_id,
                t.type_id,
                m.target_priority,
                m.target_latitude,
                m.target_longitude
                from mission m
                join target_industry i on m.target_industry = i.industry_name
                join target_city c on m.target_city = c.city_name
                join target_type t on m.target_type = t.type_name
                 """))
        session.commit()


def seed():
    create_tables()
    if not is_filled():
        insert_data()


def is_filled():
    return get_all_targets() != 0