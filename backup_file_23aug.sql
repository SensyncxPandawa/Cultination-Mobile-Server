--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: alembic
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO alembic;

--
-- Name: community_cache; Type: TABLE; Schema: public; Owner: alembic
--

CREATE TABLE public.community_cache (
    community_id integer NOT NULL,
    community_province character varying(255),
    community_city character varying(255),
    community_month character varying(255),
    community_fish_type character varying(255),
    community_production_total integer,
    community_user_total integer
);


ALTER TABLE public.community_cache OWNER TO alembic;

--
-- Name: overview_community_cache_community_id_seq; Type: SEQUENCE; Schema: public; Owner: alembic
--

CREATE SEQUENCE public.overview_community_cache_community_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.overview_community_cache_community_id_seq OWNER TO alembic;

--
-- Name: overview_community_cache_community_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: alembic
--

ALTER SEQUENCE public.overview_community_cache_community_id_seq OWNED BY public.community_cache.community_id;


--
-- Name: users_2fa; Type: TABLE; Schema: public; Owner: alembic
--

CREATE TABLE public.users_2fa (
    user_id integer NOT NULL,
    ota_codes character varying(6)
);


ALTER TABLE public.users_2fa OWNER TO alembic;

--
-- Name: users_auth; Type: TABLE; Schema: public; Owner: alembic
--

CREATE TABLE public.users_auth (
    user_id integer NOT NULL,
    user_fullname character varying(255),
    user_birthdate date,
    user_phonenumber character varying(25),
    user_email character varying(255),
    user_password character varying(255)
);


ALTER TABLE public.users_auth OWNER TO alembic;

--
-- Name: users_auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: alembic
--

CREATE SEQUENCE public.users_auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_auth_user_id_seq OWNER TO alembic;

--
-- Name: users_auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: alembic
--

ALTER SEQUENCE public.users_auth_user_id_seq OWNED BY public.users_auth.user_id;


--
-- Name: users_class; Type: TABLE; Schema: public; Owner: alembic
--

CREATE TABLE public.users_class (
    user_id integer NOT NULL,
    user_age integer,
    user_proficiency_level character varying(50),
    user_pond_total integer,
    user_pond_size_range character varying(50),
    user_fish_type character varying(50),
    user_fish_size_preference character varying(50)
);


ALTER TABLE public.users_class OWNER TO alembic;

--
-- Name: users_harvest_plan; Type: TABLE; Schema: public; Owner: alembic
--

CREATE TABLE public.users_harvest_plan (
    harvest_plan_id integer NOT NULL,
    user_id integer,
    user_province character varying(255),
    user_city character varying(255),
    harvest_plan_start character varying(255),
    harvest_plan_end character varying(255),
    harvest_plan_dayofcultivation integer,
    harvest_plan_readyonmonth integer,
    harvest_plan_pond_total integer,
    harvest_plan_pond_size integer,
    harvest_plan_fish_type character varying(255),
    harvest_plan_target_capacity character varying(255),
    harvest_plan_target_size character varying(255),
    harvest_plan_total_fish character varying(255)
);


ALTER TABLE public.users_harvest_plan OWNER TO alembic;

--
-- Name: users_harvest_plan_harvest_plan_id_seq; Type: SEQUENCE; Schema: public; Owner: alembic
--

CREATE SEQUENCE public.users_harvest_plan_harvest_plan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_harvest_plan_harvest_plan_id_seq OWNER TO alembic;

--
-- Name: users_harvest_plan_harvest_plan_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: alembic
--

ALTER SEQUENCE public.users_harvest_plan_harvest_plan_id_seq OWNED BY public.users_harvest_plan.harvest_plan_id;


--
-- Name: users_market; Type: TABLE; Schema: public; Owner: alembic
--

CREATE TABLE public.users_market (
    user_id integer NOT NULL,
    user_production_capacity_n integer,
    user_production_capacity_unit character varying(25),
    user_production_capacity_cycle character varying(25),
    user_market_capacity_n integer,
    user_market_capacity_unit character varying(25),
    user_market_capacity_cycle character varying(25),
    user_market_preference character varying(255)
);


ALTER TABLE public.users_market OWNER TO alembic;

--
-- Name: users_market_user_id_seq; Type: SEQUENCE; Schema: public; Owner: alembic
--

CREATE SEQUENCE public.users_market_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_market_user_id_seq OWNER TO alembic;

--
-- Name: users_market_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: alembic
--

ALTER SEQUENCE public.users_market_user_id_seq OWNED BY public.users_market.user_id;


--
-- Name: users_ponds_address; Type: TABLE; Schema: public; Owner: alembic
--

CREATE TABLE public.users_ponds_address (
    pond_address_id integer NOT NULL,
    user_id integer,
    user_address_full character varying(255),
    user_address_province character varying(255),
    user_address_city character varying(255),
    user_address_subdistrict character varying(255),
    user_address_zipcode character varying(20),
    user_address_coordinates character varying(100)
);


ALTER TABLE public.users_ponds_address OWNER TO alembic;

--
-- Name: users_ponds_address_pond_address_id_seq; Type: SEQUENCE; Schema: public; Owner: alembic
--

CREATE SEQUENCE public.users_ponds_address_pond_address_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_ponds_address_pond_address_id_seq OWNER TO alembic;

--
-- Name: users_ponds_address_pond_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: alembic
--

ALTER SEQUENCE public.users_ponds_address_pond_address_id_seq OWNED BY public.users_ponds_address.pond_address_id;


--
-- Name: users_primary_address; Type: TABLE; Schema: public; Owner: alembic
--

CREATE TABLE public.users_primary_address (
    user_id integer NOT NULL,
    pond_address_id integer
);


ALTER TABLE public.users_primary_address OWNER TO alembic;

--
-- Name: community_cache community_id; Type: DEFAULT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.community_cache ALTER COLUMN community_id SET DEFAULT nextval('public.overview_community_cache_community_id_seq'::regclass);


--
-- Name: users_auth user_id; Type: DEFAULT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_auth ALTER COLUMN user_id SET DEFAULT nextval('public.users_auth_user_id_seq'::regclass);


--
-- Name: users_harvest_plan harvest_plan_id; Type: DEFAULT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_harvest_plan ALTER COLUMN harvest_plan_id SET DEFAULT nextval('public.users_harvest_plan_harvest_plan_id_seq'::regclass);


--
-- Name: users_market user_id; Type: DEFAULT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_market ALTER COLUMN user_id SET DEFAULT nextval('public.users_market_user_id_seq'::regclass);


--
-- Name: users_ponds_address pond_address_id; Type: DEFAULT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_ponds_address ALTER COLUMN pond_address_id SET DEFAULT nextval('public.users_ponds_address_pond_address_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: alembic
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: community_cache; Type: TABLE DATA; Schema: public; Owner: alembic
--

COPY public.community_cache (community_id, community_province, community_city, community_month, community_fish_type, community_production_total, community_user_total) FROM stdin;
1	California	Los Angeles	August	Tilapia	8000	100
2	New York	New York City	July	Salmon	7000	90
3	Texas	Austin	September	Catfish	9000	120
\.


--
-- Data for Name: users_2fa; Type: TABLE DATA; Schema: public; Owner: alembic
--

COPY public.users_2fa (user_id, ota_codes) FROM stdin;
1	123456
2	987654
3	111111
\.


--
-- Data for Name: users_auth; Type: TABLE DATA; Schema: public; Owner: alembic
--

COPY public.users_auth (user_id, user_fullname, user_birthdate, user_phonenumber, user_email, user_password) FROM stdin;
1	Ruly Resfiandhi	1990-05-15	tel:+62-812-1432-1083	ruly@example.com	password123
2	Ridwan Wijaya	1990-05-15	tel:+62-877-2278-1396	ridwan@example.com	secure456
3	Reza Aed Galib Bajri	1998-01-10	tel:+62-821-2552-4838	reza@example.com	mypassword
\.


--
-- Data for Name: users_class; Type: TABLE DATA; Schema: public; Owner: alembic
--

COPY public.users_class (user_id, user_age, user_proficiency_level, user_pond_total, user_pond_size_range, user_fish_type, user_fish_size_preference) FROM stdin;
2	30	Mahir	3	5-8	Tilapia	1-3,4-6
3	25	Pemula	2	1-3	Catfish	3-4
1	30	Menengahxyz	5	1-3,7-10	Tilapia	1-2,5-8
\.


--
-- Data for Name: users_harvest_plan; Type: TABLE DATA; Schema: public; Owner: alembic
--

COPY public.users_harvest_plan (harvest_plan_id, user_id, user_province, user_city, harvest_plan_start, harvest_plan_end, harvest_plan_dayofcultivation, harvest_plan_readyonmonth, harvest_plan_pond_total, harvest_plan_pond_size, harvest_plan_fish_type, harvest_plan_target_capacity, harvest_plan_target_size, harvest_plan_total_fish) FROM stdin;
1	1	California	Los Angeles	2023-08-01	2023-09-15	45	5	3	1000	Tilapia	High	Medium	30000
2	2	New York	New York City	2023-07-15	2023-08-30	50	6	2	800	Salmon	Medium	Large	28000
3	3	Texas	Austin	2023-09-01	2023-10-20	40	4	4	1200	Catfish	Medium	Small	40000
\.


--
-- Data for Name: users_market; Type: TABLE DATA; Schema: public; Owner: alembic
--

COPY public.users_market (user_id, user_production_capacity_n, user_production_capacity_unit, user_production_capacity_cycle, user_market_capacity_n, user_market_capacity_unit, user_market_capacity_cycle, user_market_preference) FROM stdin;
2	150	kg	weekly	300	kg	monthly	global
1	120	kg	monthly	240	kg	monthly	local
\.


--
-- Data for Name: users_ponds_address; Type: TABLE DATA; Schema: public; Owner: alembic
--

COPY public.users_ponds_address (pond_address_id, user_id, user_address_full, user_address_province, user_address_city, user_address_subdistrict, user_address_zipcode, user_address_coordinates) FROM stdin;
1	1	123 Main St	California	Los Angeles	Downtown	12345	34.0522ø N, 118.2437ø W
2	2	456 Elm Ave	New York	New York City	Midtown	67890	40.7128ø N, 74.0060ø W
3	3	789 Oak Rd	Texas	Austin	Eastside	54321	30.2672ø N, 97.7431ø W
\.


--
-- Data for Name: users_primary_address; Type: TABLE DATA; Schema: public; Owner: alembic
--

COPY public.users_primary_address (user_id, pond_address_id) FROM stdin;
1	1
2	2
3	3
\.


--
-- Name: overview_community_cache_community_id_seq; Type: SEQUENCE SET; Schema: public; Owner: alembic
--

SELECT pg_catalog.setval('public.overview_community_cache_community_id_seq', 3, true);


--
-- Name: users_auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: alembic
--

SELECT pg_catalog.setval('public.users_auth_user_id_seq', 4, true);


--
-- Name: users_harvest_plan_harvest_plan_id_seq; Type: SEQUENCE SET; Schema: public; Owner: alembic
--

SELECT pg_catalog.setval('public.users_harvest_plan_harvest_plan_id_seq', 3, true);


--
-- Name: users_market_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: alembic
--

SELECT pg_catalog.setval('public.users_market_user_id_seq', 1, false);


--
-- Name: users_ponds_address_pond_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: alembic
--

SELECT pg_catalog.setval('public.users_ponds_address_pond_address_id_seq', 3, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: community_cache overview_community_cache_pkey; Type: CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.community_cache
    ADD CONSTRAINT overview_community_cache_pkey PRIMARY KEY (community_id);


--
-- Name: users_2fa users_2fa_pkey; Type: CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_2fa
    ADD CONSTRAINT users_2fa_pkey PRIMARY KEY (user_id);


--
-- Name: users_auth users_auth_pkey; Type: CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_auth
    ADD CONSTRAINT users_auth_pkey PRIMARY KEY (user_id);


--
-- Name: users_class users_class_pkey; Type: CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_class
    ADD CONSTRAINT users_class_pkey PRIMARY KEY (user_id);


--
-- Name: users_harvest_plan users_harvest_plan_pkey; Type: CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_harvest_plan
    ADD CONSTRAINT users_harvest_plan_pkey PRIMARY KEY (harvest_plan_id);


--
-- Name: users_market users_market_pkey; Type: CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_market
    ADD CONSTRAINT users_market_pkey PRIMARY KEY (user_id);


--
-- Name: users_ponds_address users_ponds_address_pkey; Type: CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_ponds_address
    ADD CONSTRAINT users_ponds_address_pkey PRIMARY KEY (pond_address_id);


--
-- Name: users_primary_address users_primary_address_pkey; Type: CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_primary_address
    ADD CONSTRAINT users_primary_address_pkey PRIMARY KEY (user_id);


--
-- Name: users_2fa users_2fa_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_2fa
    ADD CONSTRAINT users_2fa_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users_auth(user_id);


--
-- Name: users_class users_class_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_class
    ADD CONSTRAINT users_class_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users_auth(user_id);


--
-- Name: users_harvest_plan users_harvest_plan_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_harvest_plan
    ADD CONSTRAINT users_harvest_plan_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users_auth(user_id);


--
-- Name: users_market users_market_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_market
    ADD CONSTRAINT users_market_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users_auth(user_id);


--
-- Name: users_ponds_address users_ponds_address_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_ponds_address
    ADD CONSTRAINT users_ponds_address_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users_auth(user_id);


--
-- Name: users_primary_address users_primary_address_pond_address_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_primary_address
    ADD CONSTRAINT users_primary_address_pond_address_id_fkey FOREIGN KEY (pond_address_id) REFERENCES public.users_ponds_address(pond_address_id);


--
-- Name: users_primary_address users_primary_address_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: alembic
--

ALTER TABLE ONLY public.users_primary_address
    ADD CONSTRAINT users_primary_address_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users_auth(user_id);


--
-- PostgreSQL database dump complete
--

