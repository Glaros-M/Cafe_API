--
-- PostgreSQL database dump
--

-- Dumped from database version 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1)

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
-- Name: Cafes; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."Cafes" (
    "Id" integer NOT NULL,
    "Name" character varying NOT NULL
);


ALTER TABLE public."Cafes" OWNER TO admin;

--
-- Name: Cafes_Id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."Cafes_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Cafes_Id_seq" OWNER TO admin;

--
-- Name: Cafes_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."Cafes_Id_seq" OWNED BY public."Cafes"."Id";


--
-- Name: Employees; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."Employees" (
    "Id" integer NOT NULL,
    "CafeId" integer NOT NULL,
    "Login" character varying NOT NULL,
    "HashedPassword" character varying NOT NULL,
    "Name" character varying NOT NULL,
    "Surname" character varying NOT NULL,
    "Patronymic" character varying NOT NULL,
    "Birthday" character varying NOT NULL,
    "Post" character varying NOT NULL
);


ALTER TABLE public."Employees" OWNER TO admin;

--
-- Name: Employees_Id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."Employees_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Employees_Id_seq" OWNER TO admin;

--
-- Name: Employees_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."Employees_Id_seq" OWNED BY public."Employees"."Id";


--
-- Name: Feedbacks; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."Feedbacks" (
    "Id" integer NOT NULL,
    "UserId" integer NOT NULL,
    "Description" character varying,
    "Grade" integer
);


ALTER TABLE public."Feedbacks" OWNER TO admin;

--
-- Name: Feedbacks_Id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."Feedbacks_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Feedbacks_Id_seq" OWNER TO admin;

--
-- Name: Feedbacks_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."Feedbacks_Id_seq" OWNED BY public."Feedbacks"."Id";


--
-- Name: FoodProducts; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."FoodProducts" (
    "Id" integer NOT NULL,
    "Name" character varying NOT NULL
);


ALTER TABLE public."FoodProducts" OWNER TO admin;

--
-- Name: FoodProducts_Id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."FoodProducts_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."FoodProducts_Id_seq" OWNER TO admin;

--
-- Name: FoodProducts_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."FoodProducts_Id_seq" OWNED BY public."FoodProducts"."Id";


--
-- Name: OrderItems; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."OrderItems" (
    "Id" integer NOT NULL,
    "OrderId" integer NOT NULL,
    "RecipeId" integer NOT NULL
);


ALTER TABLE public."OrderItems" OWNER TO admin;

--
-- Name: OrderItems_Id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."OrderItems_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."OrderItems_Id_seq" OWNER TO admin;

--
-- Name: OrderItems_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."OrderItems_Id_seq" OWNED BY public."OrderItems"."Id";


--
-- Name: Orders; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."Orders" (
    "Id" integer NOT NULL,
    "CafeId" integer NOT NULL,
    "UserId" integer NOT NULL,
    "Description" character varying
);


ALTER TABLE public."Orders" OWNER TO admin;

--
-- Name: Orders_Id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."Orders_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Orders_Id_seq" OWNER TO admin;

--
-- Name: Orders_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."Orders_Id_seq" OWNED BY public."Orders"."Id";


--
-- Name: RecipeIngredients; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."RecipeIngredients" (
    "Id" integer NOT NULL,
    "RecipeId" integer NOT NULL,
    "FoodProductId" integer NOT NULL,
    "Number" integer NOT NULL
);


ALTER TABLE public."RecipeIngredients" OWNER TO admin;

--
-- Name: RecipeIngredients_Id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."RecipeIngredients_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."RecipeIngredients_Id_seq" OWNER TO admin;

--
-- Name: RecipeIngredients_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."RecipeIngredients_Id_seq" OWNED BY public."RecipeIngredients"."Id";


--
-- Name: Recipes; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."Recipes" (
    "Id" integer NOT NULL,
    "Name" character varying NOT NULL,
    "Description" character varying
);


ALTER TABLE public."Recipes" OWNER TO admin;

--
-- Name: Recipes_Id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."Recipes_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Recipes_Id_seq" OWNER TO admin;

--
-- Name: Recipes_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."Recipes_Id_seq" OWNED BY public."Recipes"."Id";


--
-- Name: Storage; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."Storage" (
    "Id" integer NOT NULL,
    "CafeId" integer NOT NULL,
    "FoodProductId" integer NOT NULL,
    "Measure" character varying NOT NULL,
    "Number" double precision NOT NULL
);


ALTER TABLE public."Storage" OWNER TO admin;

--
-- Name: Storage_Id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."Storage_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Storage_Id_seq" OWNER TO admin;

--
-- Name: Storage_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."Storage_Id_seq" OWNED BY public."Storage"."Id";


--
-- Name: Users; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."Users" (
    "Id" integer NOT NULL,
    "Login" character varying NOT NULL,
    "HashedPassword" character varying NOT NULL,
    "Name" character varying NOT NULL,
    "Surname" character varying NOT NULL,
    "Patronymic" character varying NOT NULL,
    "Birthday" character varying NOT NULL,
    "Type" character varying NOT NULL
);


ALTER TABLE public."Users" OWNER TO admin;

--
-- Name: Users_Id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public."Users_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Users_Id_seq" OWNER TO admin;

--
-- Name: Users_Id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public."Users_Id_seq" OWNED BY public."Users"."Id";


--
-- Name: Cafes Id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Cafes" ALTER COLUMN "Id" SET DEFAULT nextval('public."Cafes_Id_seq"'::regclass);


--
-- Name: Employees Id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Employees" ALTER COLUMN "Id" SET DEFAULT nextval('public."Employees_Id_seq"'::regclass);


--
-- Name: Feedbacks Id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Feedbacks" ALTER COLUMN "Id" SET DEFAULT nextval('public."Feedbacks_Id_seq"'::regclass);


--
-- Name: FoodProducts Id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."FoodProducts" ALTER COLUMN "Id" SET DEFAULT nextval('public."FoodProducts_Id_seq"'::regclass);


--
-- Name: OrderItems Id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."OrderItems" ALTER COLUMN "Id" SET DEFAULT nextval('public."OrderItems_Id_seq"'::regclass);


--
-- Name: Orders Id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Orders" ALTER COLUMN "Id" SET DEFAULT nextval('public."Orders_Id_seq"'::regclass);


--
-- Name: RecipeIngredients Id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."RecipeIngredients" ALTER COLUMN "Id" SET DEFAULT nextval('public."RecipeIngredients_Id_seq"'::regclass);


--
-- Name: Recipes Id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Recipes" ALTER COLUMN "Id" SET DEFAULT nextval('public."Recipes_Id_seq"'::regclass);


--
-- Name: Storage Id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Storage" ALTER COLUMN "Id" SET DEFAULT nextval('public."Storage_Id_seq"'::regclass);


--
-- Name: Users Id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Users" ALTER COLUMN "Id" SET DEFAULT nextval('public."Users_Id_seq"'::regclass);


--
-- Data for Name: Cafes; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."Cafes" ("Id", "Name") FROM stdin;
2	cafe2
4	431
5	CafePostman
3	string
\.


--
-- Data for Name: Employees; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."Employees" ("Id", "CafeId", "Login", "HashedPassword", "Name", "Surname", "Patronymic", "Birthday", "Post") FROM stdin;
1	2	string	321	string	string	string	string	string
2	2	string	321	string	string	string	string	string
3	2	string	321	string	string	string	string	string
4	2	string	321	string	string	string	string	string
5	2	string	321	string	string	string	string	string
6	2	string	321	string	string	string	string	string
\.


--
-- Data for Name: Feedbacks; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."Feedbacks" ("Id", "UserId", "Description", "Grade") FROM stdin;
\.


--
-- Data for Name: FoodProducts; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."FoodProducts" ("Id", "Name") FROM stdin;
1	ananas
2	banana
3	Картошка
4	Масло растительное
\.


--
-- Data for Name: OrderItems; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."OrderItems" ("Id", "OrderId", "RecipeId") FROM stdin;
1	1	2
2	1	1
3	1	1
4	2	3
5	4	3
6	4	3
7	4	3
\.


--
-- Data for Name: Orders; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."Orders" ("Id", "CafeId", "UserId", "Description") FROM stdin;
1	2	3	text
2	2	3	Test
4	2	3	string
\.


--
-- Data for Name: RecipeIngredients; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."RecipeIngredients" ("Id", "RecipeId", "FoodProductId", "Number") FROM stdin;
2	1	1	2
3	1	2	3
4	3	3	100
5	3	4	20
\.


--
-- Data for Name: Recipes; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."Recipes" ("Id", "Name", "Description") FROM stdin;
1	string	string
2	booo	string
3	Картошка фри	Картошка, обжаренная во фритюре
\.


--
-- Data for Name: Storage; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."Storage" ("Id", "CafeId", "FoodProductId", "Measure", "Number") FROM stdin;
1	2	1	шт.	100500
2	5	4	мл.	2000
3	5	3	г	3000
4	2	3	г.	19600
5	2	4	г.	19920
\.


--
-- Data for Name: Users; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."Users" ("Id", "Login", "HashedPassword", "Name", "Surname", "Patronymic", "Birthday", "Type") FROM stdin;
3	123	321	413	string	string	string	string
4	admin	SoMeStR0ngPa$$word	Name	Surname	FatherName	22.02.2001	NotReallyAdmin
5	admin	SoMeStR0ngPa$$word	Name	Surname	FatherName	22.02.2001	NotReallyAdmin
6	testSequr	$2b$12$3sp4paMQKhey0KWVaVSdEO1Vi0mPKwhXKX2tUVunud/omiJJCEIVW	string	string	string	string	string
7	admin	$2b$12$qwRvj3l5Rdj7mHOk3OVkw.HkYN9iZH7b7W1UoEo8lK/PHjimtGxna	string	string	string	string	string
8	admin2	$2b$12$3hdrHjlSKfNWhXAJsteqGOaHmFmSNQTnElCb5CsY9aLv1JdgbcjTe	string	string	string	string	string
9	admin2	$2b$12$G9d7E0K3BDHTtfNQNc1ImO59zj.tcvhBO3HEXHZvBl1Bu0eG87wFC	string	string	string	string	string
10	admin3	$2b$12$KTfLXMPZDq8eXAn8zxuleOuQnNiQVVB8pdXKqMSRe9.L2YS7Y.UwS	string	string	string	string	string
\.


--
-- Name: Cafes_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."Cafes_Id_seq"', 5, true);


--
-- Name: Employees_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."Employees_Id_seq"', 6, true);


--
-- Name: Feedbacks_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."Feedbacks_Id_seq"', 2, true);


--
-- Name: FoodProducts_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."FoodProducts_Id_seq"', 5, true);


--
-- Name: OrderItems_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."OrderItems_Id_seq"', 7, true);


--
-- Name: Orders_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."Orders_Id_seq"', 4, true);


--
-- Name: RecipeIngredients_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."RecipeIngredients_Id_seq"', 5, true);


--
-- Name: Recipes_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."Recipes_Id_seq"', 3, true);


--
-- Name: Storage_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."Storage_Id_seq"', 5, true);


--
-- Name: Users_Id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public."Users_Id_seq"', 10, true);


--
-- Name: Cafes Cafes_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Cafes"
    ADD CONSTRAINT "Cafes_pkey" PRIMARY KEY ("Id");


--
-- Name: Employees Employees_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Employees"
    ADD CONSTRAINT "Employees_pkey" PRIMARY KEY ("Id");


--
-- Name: Feedbacks Feedbacks_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Feedbacks"
    ADD CONSTRAINT "Feedbacks_pkey" PRIMARY KEY ("Id");


--
-- Name: FoodProducts FoodProducts_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."FoodProducts"
    ADD CONSTRAINT "FoodProducts_pkey" PRIMARY KEY ("Id");


--
-- Name: OrderItems OrderItems_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."OrderItems"
    ADD CONSTRAINT "OrderItems_pkey" PRIMARY KEY ("Id");


--
-- Name: Orders Orders_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Orders"
    ADD CONSTRAINT "Orders_pkey" PRIMARY KEY ("Id");


--
-- Name: RecipeIngredients RecipeIngredients_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."RecipeIngredients"
    ADD CONSTRAINT "RecipeIngredients_pkey" PRIMARY KEY ("Id");


--
-- Name: Recipes Recipes_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Recipes"
    ADD CONSTRAINT "Recipes_pkey" PRIMARY KEY ("Id");


--
-- Name: Storage Storage_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Storage"
    ADD CONSTRAINT "Storage_pkey" PRIMARY KEY ("Id");


--
-- Name: Users Users_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Users"
    ADD CONSTRAINT "Users_pkey" PRIMARY KEY ("Id");


--
-- Name: ix_Cafes_Id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "ix_Cafes_Id" ON public."Cafes" USING btree ("Id");


--
-- Name: ix_Employees_Id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "ix_Employees_Id" ON public."Employees" USING btree ("Id");


--
-- Name: ix_Feedbacks_Id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "ix_Feedbacks_Id" ON public."Feedbacks" USING btree ("Id");


--
-- Name: ix_FoodProducts_Id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "ix_FoodProducts_Id" ON public."FoodProducts" USING btree ("Id");


--
-- Name: ix_OrderItems_Id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "ix_OrderItems_Id" ON public."OrderItems" USING btree ("Id");


--
-- Name: ix_Orders_Id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "ix_Orders_Id" ON public."Orders" USING btree ("Id");


--
-- Name: ix_RecipeIngredients_Id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "ix_RecipeIngredients_Id" ON public."RecipeIngredients" USING btree ("Id");


--
-- Name: ix_Recipes_Id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "ix_Recipes_Id" ON public."Recipes" USING btree ("Id");


--
-- Name: ix_Storage_Id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "ix_Storage_Id" ON public."Storage" USING btree ("Id");


--
-- Name: ix_Users_Id; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX "ix_Users_Id" ON public."Users" USING btree ("Id");


--
-- Name: Employees Employees_CafeId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Employees"
    ADD CONSTRAINT "Employees_CafeId_fkey" FOREIGN KEY ("CafeId") REFERENCES public."Cafes"("Id");


--
-- Name: Feedbacks Feedbacks_UserId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Feedbacks"
    ADD CONSTRAINT "Feedbacks_UserId_fkey" FOREIGN KEY ("UserId") REFERENCES public."Users"("Id");


--
-- Name: OrderItems OrderItems_OrderId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."OrderItems"
    ADD CONSTRAINT "OrderItems_OrderId_fkey" FOREIGN KEY ("OrderId") REFERENCES public."Orders"("Id");


--
-- Name: OrderItems OrderItems_RecipeId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."OrderItems"
    ADD CONSTRAINT "OrderItems_RecipeId_fkey" FOREIGN KEY ("RecipeId") REFERENCES public."Recipes"("Id");


--
-- Name: Orders Orders_CafeId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Orders"
    ADD CONSTRAINT "Orders_CafeId_fkey" FOREIGN KEY ("CafeId") REFERENCES public."Cafes"("Id");


--
-- Name: Orders Orders_UserId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Orders"
    ADD CONSTRAINT "Orders_UserId_fkey" FOREIGN KEY ("UserId") REFERENCES public."Users"("Id");


--
-- Name: RecipeIngredients RecipeIngredients_FoodProductId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."RecipeIngredients"
    ADD CONSTRAINT "RecipeIngredients_FoodProductId_fkey" FOREIGN KEY ("FoodProductId") REFERENCES public."FoodProducts"("Id");


--
-- Name: RecipeIngredients RecipeIngredients_RecipeId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."RecipeIngredients"
    ADD CONSTRAINT "RecipeIngredients_RecipeId_fkey" FOREIGN KEY ("RecipeId") REFERENCES public."Recipes"("Id");


--
-- Name: Storage Storage_CafeId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Storage"
    ADD CONSTRAINT "Storage_CafeId_fkey" FOREIGN KEY ("CafeId") REFERENCES public."Cafes"("Id");


--
-- Name: Storage Storage_FoodProductId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."Storage"
    ADD CONSTRAINT "Storage_FoodProductId_fkey" FOREIGN KEY ("FoodProductId") REFERENCES public."FoodProducts"("Id");


--
-- PostgreSQL database dump complete
--

