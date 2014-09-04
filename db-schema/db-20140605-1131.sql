-- MySQL dump 10.13  Distrib 5.6.14, for osx10.7 (x86_64)
--
-- Host: localhost    Database: calendarizacionmixta
-- ------------------------------------------------------
-- Server version	5.6.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `carrera`
--

DROP TABLE IF EXISTS `carrera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrera`
--

LOCK TABLES `carrera` WRITE;
/*!40000 ALTER TABLE `carrera` DISABLE KEYS */;
/*!40000 ALTER TABLE `carrera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discapacidad`
--

DROP TABLE IF EXISTS `discapacidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discapacidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `imagen_id` int(11) NOT NULL DEFAULT '0' COMMENT 'Id de la imagen',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `imagen_id` (`imagen_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discapacidad`
--

LOCK TABLES `discapacidad` WRITE;
/*!40000 ALTER TABLE `discapacidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `discapacidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `espacio`
--

DROP TABLE IF EXISTS `espacio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `espacio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `codigo` varchar(20) NOT NULL,
  `capacidad` int(11) NOT NULL DEFAULT '0',
  `tipoespacio_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `tipoespacio_id` (`tipoespacio_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `espacio`
--

LOCK TABLES `espacio` WRITE;
/*!40000 ALTER TABLE `espacio` DISABLE KEYS */;
/*!40000 ALTER TABLE `espacio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `espaciodiscapacidad`
--

DROP TABLE IF EXISTS `espaciodiscapacidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `espaciodiscapacidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `espacio_id` int(11) NOT NULL,
  `discapacidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `espaciodiscapacidad`
--

LOCK TABLES `espaciodiscapacidad` WRITE;
/*!40000 ALTER TABLE `espaciodiscapacidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `espaciodiscapacidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `espaciorecurso`
--

DROP TABLE IF EXISTS `espaciorecurso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `espaciorecurso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `espacio_id` int(11) NOT NULL,
  `recurso_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1' COMMENT 'Cantidad de recursos que hay en dicho espacio.',
  PRIMARY KEY (`id`),
  KEY `espacio_id` (`espacio_id`,`recurso_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `espaciorecurso`
--

LOCK TABLES `espaciorecurso` WRITE;
/*!40000 ALTER TABLE `espaciorecurso` DISABLE KEYS */;
/*!40000 ALTER TABLE `espaciorecurso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `esquema`
--

DROP TABLE IF EXISTS `esquema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `esquema` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `entidad` varchar(100) NOT NULL,
  `esquema` text NOT NULL,
  `version` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `entidad` (`entidad`,`version`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `esquema`
--

LOCK TABLES `esquema` WRITE;
/*!40000 ALTER TABLE `esquema` DISABLE KEYS */;
/*!40000 ALTER TABLE `esquema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupo`
--

DROP TABLE IF EXISTS `grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) NOT NULL,
  `tamanio` int(11) NOT NULL DEFAULT '0' COMMENT 'Cantidad del grupo',
  `carrera_id` int(11) NOT NULL DEFAULT '0' COMMENT 'Carrera a la que pertenece',
  `semestre` int(11) NOT NULL DEFAULT '0' COMMENT 'Semestre en el que esta.',
  PRIMARY KEY (`id`),
  KEY `codigo` (`codigo`,`carrera_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupo`
--

LOCK TABLES `grupo` WRITE;
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupodiscapacidad`
--

DROP TABLE IF EXISTS `grupodiscapacidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grupodiscapacidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grupo_id` int(11) NOT NULL,
  `discapacidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `grupo_id` (`grupo_id`,`discapacidad_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupodiscapacidad`
--

LOCK TABLES `grupodiscapacidad` WRITE;
/*!40000 ALTER TABLE `grupodiscapacidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupodiscapacidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horariolaboral`
--

DROP TABLE IF EXISTS `horariolaboral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `horariolaboral` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` int(11) NOT NULL,
  `horas` varchar(255) NOT NULL DEFAULT '[]' COMMENT 'Horas laborables (valores entre 0 y 24) en arreglo JSON',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horariolaboral`
--

LOCK TABLES `horariolaboral` WRITE;
/*!40000 ALTER TABLE `horariolaboral` DISABLE KEYS */;
/*!40000 ALTER TABLE `horariolaboral` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imagen`
--

DROP TABLE IF EXISTS `imagen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagen`
--

LOCK TABLES `imagen` WRITE;
/*!40000 ALTER TABLE `imagen` DISABLE KEYS */;
/*!40000 ALTER TABLE `imagen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `instituto`
--

DROP TABLE IF EXISTS `instituto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `instituto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `color` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instituto`
--

LOCK TABLES `instituto` WRITE;
/*!40000 ALTER TABLE `instituto` DISABLE KEYS */;
INSERT INTO `instituto` VALUES (4,'Instituto de Computacion','FF0000#');
/*!40000 ALTER TABLE `instituto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materia`
--

DROP TABLE IF EXISTS `materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materia`
--

LOCK TABLES `materia` WRITE;
/*!40000 ALTER TABLE `materia` DISABLE KEYS */;
/*!40000 ALTER TABLE `materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materiarecurso`
--

DROP TABLE IF EXISTS `materiarecurso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `materiarecurso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `materia_id` int(11) NOT NULL,
  `recurso_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `materia_id` (`materia_id`,`recurso_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materiarecurso`
--

LOCK TABLES `materiarecurso` WRITE;
/*!40000 ALTER TABLE `materiarecurso` DISABLE KEYS */;
/*!40000 ALTER TABLE `materiarecurso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesor`
--

DROP TABLE IF EXISTS `profesor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  PRIMARY KEY (`id`),
  KEY `nombre` (`nombre`,`apellidos`,`codigo`,`instituto_id`,`correo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesor`
--

LOCK TABLES `profesor` WRITE;
/*!40000 ALTER TABLE `profesor` DISABLE KEYS */;
/*!40000 ALTER TABLE `profesor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesordiscapacidad`
--

DROP TABLE IF EXISTS `profesordiscapacidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profesordiscapacidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profesor_id` int(11) NOT NULL,
  `discapacidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `profesor_id` (`profesor_id`,`discapacidad_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesordiscapacidad`
--

LOCK TABLES `profesordiscapacidad` WRITE;
/*!40000 ALTER TABLE `profesordiscapacidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `profesordiscapacidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recurso`
--

DROP TABLE IF EXISTS `recurso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recurso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `tipo` int(11) NOT NULL DEFAULT '1' COMMENT '1 individual, 2 compartido, 3 grupal',
  `capacidad` int(11) NOT NULL DEFAULT '1' COMMENT 'Capacidad de alumnos del recurso: mesa para 5 personas, restirador para 2, etc.',
  `imagen_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recurso`
--

LOCK TABLES `recurso` WRITE;
/*!40000 ALTER TABLE `recurso` DISABLE KEYS */;
/*!40000 ALTER TABLE `recurso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipoespacio`
--

DROP TABLE IF EXISTS `tipoespacio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipoespacio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `imagen_id` int(11) NOT NULL DEFAULT '0',
  `color` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `imagen_id` (`imagen_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipoespacio`
--

LOCK TABLES `tipoespacio` WRITE;
/*!40000 ALTER TABLE `tipoespacio` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipoespacio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-06-05 10:10:22
