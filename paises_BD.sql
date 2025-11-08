USE paises;

CREATE TABLE REGIONES (
	id_region INT AUTO_INCREMENT PRIMARY KEY,
	nombre_region VARCHAR(150)
);

CREATE TABLE SUBREGIONES (
	id_subregion INT AUTO_INCREMENT PRIMARY KEY,
	nombre_subregion VARCHAR(150)
);

CREATE TABLE IDIOMAS (
	id_idioma INT AUTO_INCREMENT PRIMARY KEY,
	nombre_idioma VARCHAR(150),
	nomenclatura_idioma VARCHAR(50)
);

CREATE TABLE MONEDAS (
	id_moneda INT AUTO_INCREMENT PRIMARY KEY,
    nomenclatura_moneda VARCHAR(50), 
    simbolo_moneda VARCHAR(50),
    nombre_moneda VARCHAR(150)
);

CREATE TABLE PAISES (
	id_pais INT AUTO_INCREMENT PRIMARY KEY,
	nombre_comun_pais VARCHAR(150),
	nombre_oficial_pais VARCHAR(150),
	capital_pais VARCHAR(150),
    id_region INT NOT NULL,
    id_subregion INT NOT NULL,
    FOREIGN KEY (id_region) REFERENCES REGIONES(id_region),
    FOREIGN KEY (id_subregion) REFERENCES SUBREGIONES(id_subregion)
);

CREATE TABLE MONEDAS_PAISES (
	id_pais INT NOT NULL,
    id_moneda INT NOT NULL,
    PRIMARY KEY (id_pais, id_moneda),  
	FOREIGN KEY(id_moneda) REFERENCES MONEDAS(id_moneda),
    FOREIGN KEY(id_pais) REFERENCES PAISES(id_pais)
);

CREATE TABLE PAISES_IDIOMAS (
    id_idioma INT NOT NULL,
    id_pais INT NOT NULL,
    PRIMARY KEY (id_pais, id_idioma),  
	FOREIGN KEY(id_idioma) REFERENCES IDIOMAS(id_idioma),
    FOREIGN KEY(id_pais) REFERENCES PAISES(id_pais)
);




