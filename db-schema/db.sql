-- MySQL dump 10.13  Distrib 5.6.14, for osx10.7 (x86_64)
--
-- Host: localhost    Database: calendarizacionmixta
-- ------------------------------------------------------
-- Server version	5.6.14
--
-- Table structure for table `carrera`
--

DROP TABLE IF EXISTS `carrera`;

CREATE TABLE `carrera` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` int(11) NOT NULL DEFAULT '0' COMMENT 'Tipo de carrera: 0 lic, 1 ing, 2 maestria',
  `nombre` varchar(100) NOT NULL,
  `instituto_id` int(11) NOT NULL DEFAULT '0' COMMENT 'Instituto al que pertenece.',
  `color` varchar(10) NOT NULL,
  `imagen_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `instituto_id` (`instituto_id`),
  KEY `imagen_id` (`imagen_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `carrera`
--

LOCK TABLES `carrera` WRITE;

UNLOCK TABLES;

--
-- Table structure for table `discapacidad`
--

DROP TABLE IF EXISTS `discapacidad`;


CREATE TABLE `discapacidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `imagen_id` int(11) NOT NULL DEFAULT '0' COMMENT 'Id de la imagen',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `imagen_id` (`imagen_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `discapacidad`
--

LOCK TABLES `discapacidad` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `espacio`
--

DROP TABLE IF EXISTS `espacio`;


CREATE TABLE `espacio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `codigo` varchar(20) NOT NULL,
  `capacidad` int(11) NOT NULL DEFAULT '0',
  `tipoespacio_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `tipoespacio_id` (`tipoespacio_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `espacio`
--

LOCK TABLES `espacio` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `espaciodiscapacidad`
--

DROP TABLE IF EXISTS `espaciodiscapacidad`;


CREATE TABLE `espaciodiscapacidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `espacio_id` int(11) NOT NULL,
  `discapacidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `espaciodiscapacidad`
--

LOCK TABLES `espaciodiscapacidad` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `espaciorecurso`
--

DROP TABLE IF EXISTS `espaciorecurso`;


CREATE TABLE `espaciorecurso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `espacio_id` int(11) NOT NULL,
  `recurso_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1' COMMENT 'Cantidad de recursos que hay en dicho espacio.',
  PRIMARY KEY (`id`),
  KEY `espacio_id` (`espacio_id`,`recurso_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `espaciorecurso`
--

LOCK TABLES `espaciorecurso` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `grupo`
--

DROP TABLE IF EXISTS `grupo`;


CREATE TABLE `grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) NOT NULL,
  `periodo` varchar(10) NOT NULL COMMENT 'Periodo de clases: 2014A, etc.',
  `tamanio` int(11) NOT NULL DEFAULT '0' COMMENT 'Cantidad de alumnos en el grupo',
  `carrera_id` int(11) NOT NULL DEFAULT '0' COMMENT 'Carrera a la que pertenece',
  `semestre` int(11) NOT NULL DEFAULT '0' COMMENT 'Semestre en el que esta.',
  PRIMARY KEY (`id`),
  KEY `codigo` (`codigo`,`carrera_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `grupo`
--

LOCK TABLES `grupo` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `grupodiscapacidad`
--

DROP TABLE IF EXISTS `grupodiscapacidad`;


CREATE TABLE `grupodiscapacidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grupo_id` int(11) NOT NULL,
  `discapacidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `grupo_id` (`grupo_id`,`discapacidad_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `grupodiscapacidad`
--

LOCK TABLES `grupodiscapacidad` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `horariolaboral`
--

DROP TABLE IF EXISTS `horariolaboral`;


CREATE TABLE `horariolaboral` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` int(11) NOT NULL,
  `horas` varchar(255) NOT NULL DEFAULT '[]' COMMENT 'Horas laborables (valores entre 0 y 24) en arreglo JSON',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `horariolaboral`
--

LOCK TABLES `horariolaboral` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `imagen`
--

DROP TABLE IF EXISTS `imagen`;


CREATE TABLE `imagen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `archivo` varchar(255) NOT NULL COMMENT 'Nombre del archivo de la imagen.',
  `mime` varchar(255) NOT NULL COMMENT 'Tipo mime.',
  `ancho` varchar(10) NOT NULL COMMENT '10px, 1cm, etc.',
  `alto` varchar(10) NOT NULL,
  `alt` text NOT NULL COMMENT 'Mensaje alterno.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `imagen`
--

LOCK TABLES `imagen` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `instituto`
--

DROP TABLE IF EXISTS `instituto`;


CREATE TABLE `instituto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `color` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;


--
-- Dumping data for table `instituto`
--

LOCK TABLES `instituto` WRITE;

INSERT INTO `instituto` VALUES (4,'Instituto de Computacion','FF0000#');

UNLOCK TABLES;

--
-- Table structure for table `materia`
--

DROP TABLE IF EXISTS `materia`;


CREATE TABLE `materia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(20) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `carrera_id` int(11) NOT NULL DEFAULT '0',
  `color` varchar(10) NOT NULL,
  `imagen_id` int(11) NOT NULL DEFAULT '0',
  `horaspref` varchar(255) NOT NULL DEFAULT '[]' COMMENT 'Hoas preferentes en arreglo JSON',
  PRIMARY KEY (`id`),
  KEY `codigo` (`codigo`,`nombre`,`imagen_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `materia`
--

LOCK TABLES `materia` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `materiarecurso`
--

DROP TABLE IF EXISTS `materiarecurso`;


CREATE TABLE `materiarecurso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `materia_id` int(11) NOT NULL,
  `recurso_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `materia_id` (`materia_id`,`recurso_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `materiarecurso`
--

LOCK TABLES `materiarecurso` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `profesor`
--

DROP TABLE IF EXISTS `profesor`;


CREATE TABLE `profesor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `codigo` varchar(20) NOT NULL,
  `instituto_id` int(11) NOT NULL DEFAULT '0',
  `correo` varchar(255) NOT NULL,
  `imagen_id` int(11) NOT NULL DEFAULT '0',
  `activo`   int(11) NOT NULL DEFAULT '1',
  `horaspref` varchar(255) NOT NULL DEFAULT '[]' COMMENT 'Horas preferentes (valores entre 0 y 24) en JSON',
  `observaciones` text NOT NULL COMMENT 'observaciones',
  PRIMARY KEY (`id`),
  KEY `nombre` (`nombre`,`apellidos`,`codigo`,`instituto_id`,`correo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `profesor`
--

LOCK TABLES `profesor` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `profesormateria`
--

DROP TABLE IF EXISTS `profesormateria`;


CREATE TABLE `profesormateria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profesor_id` int(11) NOT NULL,
  `materia_id` int(11) NOT NULL,
  `preferente` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `materia_id` (`materia_id`),
  KEY `profesor_id` (`profesor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `materiarecurso`
--

LOCK TABLES `profesormateria` WRITE;


UNLOCK TABLES;


--
-- Table structure for table `profesordiscapacidad`
--

DROP TABLE IF EXISTS `profesordiscapacidad`;


CREATE TABLE `profesordiscapacidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profesor_id` int(11) NOT NULL,
  `discapacidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `profesor_id` (`profesor_id`,`discapacidad_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `profesordiscapacidad`
--

LOCK TABLES `profesordiscapacidad` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `recurso`
--

DROP TABLE IF EXISTS `recurso`;


CREATE TABLE `recurso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `tipo` int(11) NOT NULL DEFAULT '1' COMMENT '1 individual, 2 compartido, 3 grupal',
  `capacidad` int(11) NOT NULL DEFAULT '1' COMMENT 'Capacidad de alumnos del recurso: mesa para 5 personas, restirador para 2, etc.',
  `imagen_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `recurso`
--

LOCK TABLES `recurso` WRITE;


UNLOCK TABLES;

--
-- Table structure for table `tipoespacio`
--

DROP TABLE IF EXISTS `tipoespacio`;


CREATE TABLE `tipoespacio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `imagen_id` int(11) NOT NULL DEFAULT '0',
  `color` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `imagen_id` (`imagen_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Dumping data for table `tipoespacio`
--

LOCK TABLES `tipoespacio` WRITE;


UNLOCK TABLES;










-- Dump completed on 2014-06-05 10:10:22
