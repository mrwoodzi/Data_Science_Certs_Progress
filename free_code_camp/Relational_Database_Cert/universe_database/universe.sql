--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE universe;
--
-- Name: universe; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE universe WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE universe OWNER TO freecodecamp;

\connect universe

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: galaxy; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galaxy (
    galaxy_id integer NOT NULL,
    galaxy_type character varying(40) NOT NULL,
    star_types text NOT NULL,
    planet_types character varying(40) NOT NULL,
    life boolean,
    name character varying(40) NOT NULL
);


ALTER TABLE public.galaxy OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.galaxy_galaxy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galaxy_galaxy_id_seq OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.galaxy_galaxy_id_seq OWNED BY public.galaxy.galaxy_id;


--
-- Name: moon; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.moon (
    moon_id integer NOT NULL,
    name character varying(40) NOT NULL,
    planet_id integer NOT NULL,
    life boolean,
    size character varying(10),
    moon_code character varying(10)
);


ALTER TABLE public.moon OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.moon_moon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moon_moon_id_seq OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.moon_moon_id_seq OWNED BY public.moon.moon_id;


--
-- Name: planet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet (
    planet_id integer NOT NULL,
    name character varying(40) NOT NULL,
    star_id integer NOT NULL,
    planet_type character varying(40),
    number_moons numeric,
    life boolean,
    planet_code character varying(10)
);


ALTER TABLE public.planet OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.planet_planet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planet_planet_id_seq OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.planet_planet_id_seq OWNED BY public.planet.planet_id;


--
-- Name: ships; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.ships (
    ships_id integer NOT NULL,
    name character varying(40) NOT NULL,
    space_station_id integer NOT NULL,
    ship_code character varying(10)
);


ALTER TABLE public.ships OWNER TO freecodecamp;

--
-- Name: ships_ships_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.ships_ships_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ships_ships_id_seq OWNER TO freecodecamp;

--
-- Name: ships_ships_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.ships_ships_id_seq OWNED BY public.ships.ships_id;


--
-- Name: space_station; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.space_station (
    space_station_id integer NOT NULL,
    name character varying(40) NOT NULL,
    galaxy_id integer NOT NULL,
    star_id integer NOT NULL,
    space_station_type character varying(40),
    number_ships integer,
    space_station_code character varying(10)
);


ALTER TABLE public.space_station OWNER TO freecodecamp;

--
-- Name: space_station_space_station_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.space_station_space_station_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.space_station_space_station_id_seq OWNER TO freecodecamp;

--
-- Name: space_station_space_station_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.space_station_space_station_id_seq OWNED BY public.space_station.space_station_id;


--
-- Name: star; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star (
    star_id integer NOT NULL,
    name character varying(40) NOT NULL,
    galaxy_id integer NOT NULL,
    star_type character varying(40),
    number_planets integer
);


ALTER TABLE public.star OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.star_star_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.star_star_id_seq OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.star_star_id_seq OWNED BY public.star.star_id;


--
-- Name: galaxy galaxy_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy ALTER COLUMN galaxy_id SET DEFAULT nextval('public.galaxy_galaxy_id_seq'::regclass);


--
-- Name: moon moon_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon ALTER COLUMN moon_id SET DEFAULT nextval('public.moon_moon_id_seq'::regclass);


--
-- Name: planet planet_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet ALTER COLUMN planet_id SET DEFAULT nextval('public.planet_planet_id_seq'::regclass);


--
-- Name: ships ships_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.ships ALTER COLUMN ships_id SET DEFAULT nextval('public.ships_ships_id_seq'::regclass);


--
-- Name: space_station space_station_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.space_station ALTER COLUMN space_station_id SET DEFAULT nextval('public.space_station_space_station_id_seq'::regclass);


--
-- Name: star star_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star ALTER COLUMN star_id SET DEFAULT nextval('public.star_star_id_seq'::regclass);


--
-- Data for Name: galaxy; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galaxy VALUES (3, 'Seyfert Galaxy', '34 Types', '654', true, 'Alpha Quadrant Galaxy');
INSERT INTO public.galaxy VALUES (4, 'Blazar Galaxy', '783 Types', '8394', true, 'Outer Rim Galaxy');
INSERT INTO public.galaxy VALUES (5, 'Spiral Galaxy', '2376 Types', '983', true, 'Milky Way Galaxy');
INSERT INTO public.galaxy VALUES (6, 'Spiral Galaxy', 'Type A, Type B, Type C', '1200', true, 'Andromeda Galaxy');
INSERT INTO public.galaxy VALUES (7, 'Spiral Galaxy', 'Type D, Type E', '550', false, 'Whirlpool Galaxy');
INSERT INTO public.galaxy VALUES (8, 'Spiral Galaxy', 'Type F, Type G', '380', true, 'Triangulum Galaxy');


--
-- Data for Name: moon; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.moon VALUES (1, 'Moon 1', 1, true, '3400 km', 'ABC123');
INSERT INTO public.moon VALUES (2, 'Moon 2', 1, false, '2900 km', 'DEF456');
INSERT INTO public.moon VALUES (3, 'Moon 3', 1, false, '2200 km', 'GHI789');
INSERT INTO public.moon VALUES (4, 'Moon 4', 2, true, '1800 km', 'JKL012');
INSERT INTO public.moon VALUES (5, 'Moon 5', 2, true, '2100 km', 'MNO345');
INSERT INTO public.moon VALUES (6, 'Moon 6', 2, false, '2500 km', 'PQR678');
INSERT INTO public.moon VALUES (7, 'Moon 7', 3, false, '1500 km', 'STU901');
INSERT INTO public.moon VALUES (8, 'Moon 8', 3, true, '100 km', 'VWX234');
INSERT INTO public.moon VALUES (9, 'Moon 9', 3, true, '500 km', 'YZA567');
INSERT INTO public.moon VALUES (10, 'Moon 10', 4, false, '4000 km', 'BCD890');
INSERT INTO public.moon VALUES (11, 'Moon 11', 4, false, '10 km', 'EFG123');
INSERT INTO public.moon VALUES (12, 'Moon 12', 4, false, '8000 km', 'HIJ456');
INSERT INTO public.moon VALUES (13, 'Moon 13', 5, true, '600 km', 'KLM789');
INSERT INTO public.moon VALUES (14, 'Moon 14', 5, true, '50 km', 'NOP012');
INSERT INTO public.moon VALUES (15, 'Moon 15', 5, false, '4500 km', 'QRS345');
INSERT INTO public.moon VALUES (16, 'Moon 16', 6, false, '700 km', 'TUV678');
INSERT INTO public.moon VALUES (17, 'Moon 17', 6, false, '30000 km', 'WXY901');
INSERT INTO public.moon VALUES (18, 'Moon 18', 6, true, '30 km', 'ZAB234');
INSERT INTO public.moon VALUES (19, 'Moon 19', 6, true, '5000 km', 'CDE567');
INSERT INTO public.moon VALUES (20, 'Moon 20', 6, false, '5 km', 'FGH890');


--
-- Data for Name: planet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet VALUES (1, 'Planet 1', 1, 'Type X', 2, true, 'ABC123');
INSERT INTO public.planet VALUES (2, 'Planet 2', 2, 'Type Y', 0, false, 'DEF456');
INSERT INTO public.planet VALUES (3, 'Planet 3', 3, 'Type Z', 4, true, 'GHI789');
INSERT INTO public.planet VALUES (4, 'Planet 4', 4, 'Type X', 1, false, 'JKL012');
INSERT INTO public.planet VALUES (5, 'Planet 5', 5, 'Type Y', 3, true, 'MNO345');
INSERT INTO public.planet VALUES (6, 'Planet 6', 6, 'Type Z', 0, false, 'PQR678');
INSERT INTO public.planet VALUES (7, 'Planet 7', 1, 'Type X', 5, true, 'STU901');
INSERT INTO public.planet VALUES (8, 'Planet 8', 2, 'Type Y', 2, false, 'VWX234');
INSERT INTO public.planet VALUES (9, 'Planet 9', 3, 'Type Z', 1, true, 'YZA567');
INSERT INTO public.planet VALUES (10, 'Planet 10', 4, 'Type X', 0, false, 'BCD890');
INSERT INTO public.planet VALUES (11, 'Planet 11', 5, 'Type Y', 3, true, 'EFG123');
INSERT INTO public.planet VALUES (12, 'Planet 12', 6, 'Type Z', 2, false, 'HIJ456');


--
-- Data for Name: ships; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.ships VALUES (1, 'Millennium Falcon', 1, 'ABC123');
INSERT INTO public.ships VALUES (2, 'Star Destroyer', 1, 'DEF456');
INSERT INTO public.ships VALUES (3, 'Enterprise', 2, 'GHI789');
INSERT INTO public.ships VALUES (4, 'Death Star', 2, 'JKL012');
INSERT INTO public.ships VALUES (5, 'X-wing', 3, 'MNO345');
INSERT INTO public.ships VALUES (6, 'USS Voyager', 3, 'PQR678');
INSERT INTO public.ships VALUES (7, 'TIE Fighter', 4, 'STU901');
INSERT INTO public.ships VALUES (8, 'Klingon Bird of Prey', 4, 'VWX234');
INSERT INTO public.ships VALUES (9, 'Slave 1', 5, 'YZA567');


--
-- Data for Name: space_station; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.space_station VALUES (1, 'Space Station 1', 3, 1, 'Type A', 10, 'ABC123');
INSERT INTO public.space_station VALUES (2, 'Space Station 2', 3, 2, 'Type B', 5, 'DEF456');
INSERT INTO public.space_station VALUES (3, 'Space Station 3', 4, 3, 'Type C', 8, 'GHI789');
INSERT INTO public.space_station VALUES (4, 'Space Station 4', 4, 4, 'Type A', 15, 'JKL012');
INSERT INTO public.space_station VALUES (5, 'Space Station 5', 5, 5, 'Type B', 3, 'MNO345');
INSERT INTO public.space_station VALUES (6, 'Space Station 6', 5, 6, 'Type C', 7, 'PQR678');
INSERT INTO public.space_station VALUES (8, 'Space Station 7', 3, 3, 'Type A', NULL, 'VWX234');
INSERT INTO public.space_station VALUES (9, 'Space Station 8', 4, 5, 'Type B', NULL, 'YZA567');


--
-- Data for Name: star; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star VALUES (1, 'Star 1', 3, 'Type A', 34);
INSERT INTO public.star VALUES (2, 'Star 2', 4, 'Type B', 783);
INSERT INTO public.star VALUES (3, 'Star 3', 5, 'Type C', 2376);
INSERT INTO public.star VALUES (4, 'Star 4', 3, 'Type A', 654);
INSERT INTO public.star VALUES (5, 'Star 5', 4, 'Type B', 8394);
INSERT INTO public.star VALUES (6, 'Star 6', 5, 'Type C', 983);


--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.galaxy_galaxy_id_seq', 8, true);


--
-- Name: moon_moon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.moon_moon_id_seq', 20, true);


--
-- Name: planet_planet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.planet_planet_id_seq', 12, true);


--
-- Name: ships_ships_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.ships_ships_id_seq', 10, true);


--
-- Name: space_station_space_station_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.space_station_space_station_id_seq', 9, true);


--
-- Name: star_star_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.star_star_id_seq', 6, true);


--
-- Name: galaxy galaxy_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_pkey PRIMARY KEY (galaxy_id);


--
-- Name: moon moon_moon_code_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_moon_code_key UNIQUE (moon_code);


--
-- Name: moon moon_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_pkey PRIMARY KEY (moon_id);


--
-- Name: galaxy names; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT names UNIQUE (name);


--
-- Name: planet planet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_pkey PRIMARY KEY (planet_id);


--
-- Name: planet planet_planet_code_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_planet_code_key UNIQUE (planet_code);


--
-- Name: ships ships_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.ships
    ADD CONSTRAINT ships_pkey PRIMARY KEY (ships_id);


--
-- Name: ships ships_ship_code_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.ships
    ADD CONSTRAINT ships_ship_code_key UNIQUE (ship_code);


--
-- Name: space_station space_station_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.space_station
    ADD CONSTRAINT space_station_pkey PRIMARY KEY (space_station_id);


--
-- Name: space_station space_station_space_station_code_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.space_station
    ADD CONSTRAINT space_station_space_station_code_key UNIQUE (space_station_code);


--
-- Name: star star_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_pkey PRIMARY KEY (star_id);


--
-- Name: moon unique_name; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT unique_name UNIQUE (name);


--
-- Name: star unique_number_planets; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT unique_number_planets UNIQUE (number_planets);


--
-- Name: ships unique_ships; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.ships
    ADD CONSTRAINT unique_ships UNIQUE (name);


--
-- Name: space_station unique_space_station; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.space_station
    ADD CONSTRAINT unique_space_station UNIQUE (name);


--
-- Name: unique_planet; Type: INDEX; Schema: public; Owner: freecodecamp
--

CREATE UNIQUE INDEX unique_planet ON public.planet USING btree (name);


--
-- Name: unique_star; Type: INDEX; Schema: public; Owner: freecodecamp
--

CREATE UNIQUE INDEX unique_star ON public.star USING btree (name);


--
-- Name: moon moon_planet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES public.planet(planet_id);


--
-- Name: planet planet_star_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_star_id_fkey FOREIGN KEY (star_id) REFERENCES public.star(star_id);


--
-- Name: ships ships_space_station_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.ships
    ADD CONSTRAINT ships_space_station_id_fkey FOREIGN KEY (space_station_id) REFERENCES public.space_station(space_station_id);


--
-- Name: space_station space_station_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.space_station
    ADD CONSTRAINT space_station_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- Name: space_station space_station_star_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.space_station
    ADD CONSTRAINT space_station_star_id_fkey FOREIGN KEY (star_id) REFERENCES public.star(star_id);


--
-- Name: star star_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- PostgreSQL database dump complete
--

