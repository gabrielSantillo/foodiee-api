-- MariaDB dump 10.19  Distrib 10.6.9-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: foodiee
-- ------------------------------------------------------
-- Server version	10.6.9-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) COLLATE utf8mb4_bin NOT NULL,
  `last_name` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(1000) COLLATE utf8mb4_bin NOT NULL,
  `salt` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_un` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'Gabriel','Santillo','gabriel@testing.com','*A4D7878C14F33DF85C14DBAACAC137B8D5052C5E','5d0be712be0441f58f9ea293b522903d','gasantillo','2022-12-19 11:28:53');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_restaurant_order`
--

DROP TABLE IF EXISTS `client_restaurant_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_restaurant_order` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `client_id` int(10) unsigned NOT NULL,
  `restaurant_id` int(10) unsigned NOT NULL,
  `is_confirmed` tinyint(1) NOT NULL DEFAULT 0,
  `is_complete` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `client_restaurant_order_FK` (`client_id`),
  KEY `client_restaurant_order_FK_1` (`restaurant_id`),
  CONSTRAINT `client_restaurant_order_FK` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `client_restaurant_order_FK_1` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_restaurant_order`
--

LOCK TABLES `client_restaurant_order` WRITE;
/*!40000 ALTER TABLE `client_restaurant_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `client_restaurant_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_session`
--

DROP TABLE IF EXISTS `client_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_session` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `client_id` int(10) unsigned NOT NULL,
  `token` varchar(1000) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_session_un` (`token`) USING HASH,
  KEY `client_session_FK` (`client_id`),
  CONSTRAINT `client_session_FK` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_session`
--

LOCK TABLES `client_session` WRITE;
/*!40000 ALTER TABLE `client_session` DISABLE KEYS */;
INSERT INTO `client_session` VALUES (1,1,'8c37e0b02a4864a679fa46c58d85a342926718e90799e4707653f47ab5a25973','2022-12-19 11:28:53');
/*!40000 ALTER TABLE `client_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_item`
--

DROP TABLE IF EXISTS `menu_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu_item` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `restaurant_id` int(10) unsigned NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `description` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `price` float NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `menu_item_FK` (`restaurant_id`),
  CONSTRAINT `menu_item_FK` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_item`
--

LOCK TABLES `menu_item` WRITE;
/*!40000 ALTER TABLE `menu_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_item_images`
--

DROP TABLE IF EXISTS `menu_item_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu_item_images` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `menu_item_id` int(10) unsigned NOT NULL,
  `file_name` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `description` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `menu_item_images_FK` (`menu_item_id`),
  CONSTRAINT `menu_item_images_FK` FOREIGN KEY (`menu_item_id`) REFERENCES `menu_item` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_item_images`
--

LOCK TABLES `menu_item_images` WRITE;
/*!40000 ALTER TABLE `menu_item_images` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu_item_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_item_order`
--

DROP TABLE IF EXISTS `menu_item_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu_item_order` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int(10) unsigned NOT NULL,
  `menu_item_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `menu_item_order_FK` (`order_id`),
  KEY `menu_item_order_FK_1` (`menu_item_id`),
  CONSTRAINT `menu_item_order_FK` FOREIGN KEY (`order_id`) REFERENCES `client_restaurant_order` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `menu_item_order_FK_1` FOREIGN KEY (`menu_item_id`) REFERENCES `menu_item` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_item_order`
--

LOCK TABLES `menu_item_order` WRITE;
/*!40000 ALTER TABLE `menu_item_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu_item_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant`
--

DROP TABLE IF EXISTS `restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restaurant` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `phone_number` varchar(11) COLLATE utf8mb4_bin NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(1000) COLLATE utf8mb4_bin NOT NULL,
  `salt` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `bio` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `city` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `restaurant_un` (`email`),
  UNIQUE KEY `restaurant_un_phone_number` (`phone_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant`
--

LOCK TABLES `restaurant` WRITE;
/*!40000 ALTER TABLE `restaurant` DISABLE KEYS */;
/*!40000 ALTER TABLE `restaurant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_images`
--

DROP TABLE IF EXISTS `restaurant_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restaurant_images` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `restaurant_id` int(10) unsigned NOT NULL,
  `file_name` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `description` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `restaurant_images_FK` (`restaurant_id`),
  CONSTRAINT `restaurant_images_FK` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_images`
--

LOCK TABLES `restaurant_images` WRITE;
/*!40000 ALTER TABLE `restaurant_images` DISABLE KEYS */;
/*!40000 ALTER TABLE `restaurant_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurant_session`
--

DROP TABLE IF EXISTS `restaurant_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restaurant_session` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `restaurant_id` int(10) unsigned NOT NULL,
  `token` varchar(1000) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `restaurant_session_un` (`token`) USING HASH,
  KEY `restaurant_session_FK` (`restaurant_id`),
  CONSTRAINT `restaurant_session_FK` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurant` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_session`
--

LOCK TABLES `restaurant_session` WRITE;
/*!40000 ALTER TABLE `restaurant_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `restaurant_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'foodiee'
--
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_client` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_client`(
email_input varchar(100),
first_name_input varchar(30),
last_name_input varchar(30),
username_input varchar(50),
password_input varchar(1000),
salt_input varchar(100),
token_input varchar(1000)
)
    MODIFIES SQL DATA
begin
	insert into client(email, first_name, last_name, username, password, salt)
	values (email_input, first_name_input, last_name_input, username_input, PASSWORD(CONCAT(password_input, salt_input)), salt_input);

	insert into client_session (client_id, token)
	values (last_insert_id(), token_input);

	select cs.client_id as client_id, convert(cs.token using utf8) as token 
	from client_session cs 
	where cs.id = last_insert_id() ;
	commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_client` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_client`(
password_input varchar(1000),
token_input varchar(100)
)
    MODIFIES SQL DATA
begin
	delete c from client c
	inner join client_session cs on cs.client_id = c.id
	where cs.token = token_input and password = password(concat(password_input ,(select salt where cs.token = token_input)));

	select row_count() as row_updated;
	commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_client_token` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_client_token`(token_input varchar(100))
    MODIFIES SQL DATA
begin
	delete cs from client_session cs
	where cs.token = token_input;

	select row_count() as row_updated;
	commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `edit_client` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `edit_client`(
first_name_input varchar(30),
last_name_input varchar(30),
email_input varchar(100),
password_input varchar(1000),
username_input varchar(50),
token_input varchar(1000)
)
    MODIFIES SQL DATA
begin
	update client c
	inner join client_session cs on cs.client_id = c.id
	set c.first_name = first_name_input, c.last_name = last_name_input, c.email = email_input,
	c.password = password_input, c.username = username_input
	where cs.token = token_input;

	select row_count() as row_updated;
	
	commit;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_client` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_client`(id_input int unsigned)
begin
	select c.id as client_id, convert(c.email using utf8) as email, convert(c.first_name using utf8) as first_name,
	convert(c.last_name using utf8) as last_name, convert(c.username using utf8) as username, convert(c.email using utf8) as email,
	convert(c.created_at using utf8) as created_at 
	from client c
	where c.id = id_input;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_client_by_token` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_client_by_token`(token_input varchar(1000))
begin
	select convert(c.first_name using utf8) as first_name, convert(c.last_name using utf8) as last_name,
	convert(c.email using utf8) as email, convert(c.password using utf8) as password, convert(c.username using utf8) as username,
	convert(c.created_at using utf8) as created_at
	from client c
	inner join client_session cs on cs.client_id = c.id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-19 15:15:04
