
DROP TABLE IF EXISTS `carrera`;
CREATE TABLE IF NOT EXISTS carrera (
  id int(11) NOT NULL AUTO_INCREMENT,
  tipo int(11) NOT NULL DEFAULT '0' COMMENT 'Tipo de carrera: 0 lic, 1 ing, 2 maestria',
  nombre varchar(100) NOT NULL,
  instituto_id int(11) NOT NULL DEFAULT '0' COMMENT 'Instituto al que pertenece.',
  color varchar(10) NOT NULL,
  imagen_id int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (id),
  UNIQUE KEY nombre (nombre),
  KEY instituto_id (instituto_id),
  KEY imagen_id (imagen_id)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `discapacidad`;
CREATE TABLE IF NOT EXISTS discapacidad (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombre varchar(100) NOT NULL,
  imagen_id int(11) NOT NULL DEFAULT '0' COMMENT 'Id de la imagen',
  PRIMARY KEY (id),
  UNIQUE KEY nombre (nombre),
  KEY imagen_id (imagen_id)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `espacio`;
CREATE TABLE IF NOT EXISTS espacio (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombre varchar(255) NOT NULL,
  codigo varchar(20) NOT NULL,
  capacidad int(11) NOT NULL DEFAULT '0',
  tipoespacio_id int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (id),
  UNIQUE KEY nombre (nombre),
  KEY tipoespacio_id (tipoespacio_id)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `espaciodiscapacidad`;
CREATE TABLE IF NOT EXISTS espaciodiscapacidad (
  id int(11) NOT NULL AUTO_INCREMENT,
  espacio_id int(11) NOT NULL,
  discapacidad_id int(11) NOT NULL,
  PRIMARY KEY (id)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `espaciorecurso`;
CREATE TABLE IF NOT EXISTS espaciorecurso (
  id int(11) NOT NULL AUTO_INCREMENT,
  espacio_id int(11) NOT NULL,
  recurso_id int(11) NOT NULL,
  cantidad int(11) NOT NULL DEFAULT '1' COMMENT 'Cantidad de recursos que hay en dicho espacio.',
  PRIMARY KEY (id),
  KEY espacio_id (espacio_id,recurso_id)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `esquema`;
CREATE TABLE IF NOT EXISTS esquema (
  id int(11) NOT NULL AUTO_INCREMENT,
  entidad varchar(100) NOT NULL,
  esquema text NOT NULL,
  version int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (id),
  KEY entidad (entidad,version)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `grupo`;
CREATE TABLE IF NOT EXISTS grupo (
  id int(11) NOT NULL AUTO_INCREMENT,
  codigo varchar(50) NOT NULL,
  tamanio int(11) NOT NULL DEFAULT '0' COMMENT 'Cantidad del grupo',
  carrera_id int(11) NOT NULL DEFAULT '0' COMMENT 'Carrera a la que pertenece',
  semestre int(11) NOT NULL DEFAULT '0' COMMENT 'Semestre en el que esta.',
  PRIMARY KEY (id),
  KEY codigo (codigo,carrera_id)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `grupodiscapacidad`;
CREATE TABLE IF NOT EXISTS grupodiscapacidad (
  id int(11) NOT NULL AUTO_INCREMENT,
  grupo_id int(11) NOT NULL,
  discapacidad_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY grupo_id (grupo_id,discapacidad_id)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `horariolaboral`;
CREATE TABLE IF NOT EXISTS horariolaboral (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombre int(11) NOT NULL,
  horas varchar(255) NOT NULL DEFAULT '[]' COMMENT 'Horas laborables (valores entre 0 y 24) en arreglo JSON',
  PRIMARY KEY (id),
  UNIQUE KEY nombre (nombre)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `imagen`;
CREATE TABLE IF NOT EXISTS imagen (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombre varchar(255) NOT NULL,
  archivo varchar(255) NOT NULL COMMENT 'Nombre del archivo de la imagen.',
  mime varchar(255) NOT NULL COMMENT 'Tipo mime.',
  ancho varchar(10) NOT NULL COMMENT '10px, 1cm, etc.',
  alto varchar(10) NOT NULL,
  alt text NOT NULL COMMENT 'Mensaje alterno.',
  PRIMARY KEY (id),
  UNIQUE KEY nombre (nombre)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `instituto`;
CREATE TABLE IF NOT EXISTS instituto (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombre varchar(255) NOT NULL,
  color varchar(10) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY nombre (nombre)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `materia`;
CREATE TABLE IF NOT EXISTS materia (
  id int(11) NOT NULL AUTO_INCREMENT,
  codigo varchar(20) NOT NULL,
  nombre varchar(255) NOT NULL,
  carrera_id int(11) NOT NULL DEFAULT '0',
  color varchar(10) NOT NULL,
  imagen_id int(11) NOT NULL DEFAULT '0',
  horaspref varchar(255) NOT NULL DEFAULT '[]' COMMENT 'Hoas preferentes en arreglo JSON',
  PRIMARY KEY (id),
  KEY codigo (codigo,nombre,imagen_id)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `materiarecurso`;
CREATE TABLE IF NOT EXISTS materiarecurso (
  id int(11) NOT NULL AUTO_INCREMENT,
  materia_id int(11) NOT NULL,
  recurso_id int(11) NOT NULL,
  cantidad int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (id),
  KEY materia_id (materia_id,recurso_id)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `profesor`;
CREATE TABLE IF NOT EXISTS profesor (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombre varchar(255) NOT NULL,
  apellidos varchar(255) NOT NULL,
  codigo varchar(20) NOT NULL,
  instituto_id int(11) NOT NULL DEFAULT '0',
  correo varchar(255) NOT NULL,
  imagen_id int(11) NOT NULL DEFAULT '0',
  horaspref varchar(255) NOT NULL DEFAULT '[]' COMMENT 'Horas preferentes (valores entre 0 y 24) en JSON',
  PRIMARY KEY (id),
  KEY nombre (nombre,apellidos,codigo,instituto_id,correo)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `profesordiscapacidad`;
CREATE TABLE IF NOT EXISTS profesordiscapacidad (
  id int(11) NOT NULL AUTO_INCREMENT,
  profesor_id int(11) NOT NULL,
  discapacidad_id int(11) NOT NULL,
  PRIMARY KEY (id),
  KEY profesor_id (profesor_id,discapacidad_id)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `recurso`;
CREATE TABLE IF NOT EXISTS recurso (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombre varchar(100) NOT NULL,
  tipo int(11) NOT NULL DEFAULT '1' COMMENT '1 individual, 2 compartido, 3 grupal',
  capacidad int(11) NOT NULL DEFAULT '1' COMMENT 'Capacidad de alumnos del recurso: mesa para 5 personas, restirador para 2, etc.',
  imagen_id int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (id),
  UNIQUE KEY nombre (nombre)
) AUTO_INCREMENT=1 ;

DROP TABLE IF EXISTS `tipoespacio`;
CREATE TABLE IF NOT EXISTS tipoespacio (
  id int(11) NOT NULL AUTO_INCREMENT,
  nombre varchar(255) NOT NULL,
  imagen_id int(11) NOT NULL DEFAULT '0',
  color varchar(10) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY nombre (nombre),
  KEY imagen_id (imagen_id)
) AUTO_INCREMENT=1 ;
