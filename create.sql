CREATE TABLE public.country (
	id serial,
	"name" varchar(60) NOT NULL,
	CONSTRAINT country_pk PRIMARY KEY (id),
	CONSTRAINT country_un UNIQUE ("name")
);
CREATE TABLE public.hemispheres (
	id serial,
	"name" varchar(60) NOT NULL,
	CONSTRAINT hemisphere_pk PRIMARY KEY (id),
	CONSTRAINT eastwest_un UNIQUE ("name")
);
CREATE TABLE public.eastwest (
	id serial NOT NULL,
	"name" varchar(60) NOT NULL,
	CONSTRAINT eastwest_pk PRIMARY KEY (id),
	CONSTRAINT hemispheres_un UNIQUE ("name")
);

CREATE TABLE public.city (
	id serial,
	"name" varchar(60) NOT NULL,
	latitude float NOT NULL,
	longitude float NOT NULL,
	id_country int NOT NULL,
	id_hemisphere int NOT NULL,
	id_eastwest int NOT NULL,
	CONSTRAINT city_pk PRIMARY KEY (id),
	CONSTRAINT country_fk FOREIGN KEY (id_country) REFERENCES public.country(id),
	CONSTRAINT hemisphere_fk FOREIGN KEY (id_hemisphere) REFERENCES public.hemispheres(id),
	CONSTRAINT eastwest_fk FOREIGN KEY (id_eastwest) REFERENCES public.eastwest(id)
);

CREATE TABLE public.records (
	id serial,
	"year" int NOT NULL,
	temperature float NOT NULL,
	id_city int NOT NULL,
	CONSTRAINT record_pk PRIMARY KEY (id),
	CONSTRAINT city_fk FOREIGN KEY (id_city) REFERENCES public.city(id)
);
