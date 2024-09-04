-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: restaurant
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bills2`
--

DROP TABLE IF EXISTS `bills2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bills2` (
  `INVOICE_NO` varchar(30) DEFAULT NULL,
  `ITEM_NAME` varchar(30) DEFAULT NULL,
  `QTY` int DEFAULT NULL,
  `RATE` int DEFAULT NULL,
  `SUB_TOTAL` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bills2`
--

LOCK TABLES `bills2` WRITE;
/*!40000 ALTER TABLE `bills2` DISABLE KEYS */;
INSERT INTO `bills2` VALUES ('01DA20241','PICKLE',1,5,5),('01DA20241','CURD RICE',1,60,60),('01DA20241','SAMBHAR',1,32,32),('01DA20241','TOMATO SOUP',1,60,60),('01DA20241','PICKLE',1,5,5),('01DA20241','CURD RICE',1,60,60),('01DA20241','SAMBHAR',1,32,32),('01DA202410','PICKLE',1,5,5),('01DA202410','CURD RICE',1,60,60),('01DA202410','SAMBHAR',4,32,128),('01DA202411','SAMBHAR RICE',1,50,50),('01DA202411','MEALS',1,90,90),('10DA202412','YOGHURT',1,20,20),('10DA202412','BIRYANI',1,90,90),('01DA202413','MILK',1,10,10),('01DA202413','TEA',1,15,15),('01DA202414','PICKLE',1,5,5),('01DA202414','CURD RICE',1,60,60),('01DA202414','SAMBHAR',1,32,32),('01DA202414','SAMBHAR RICE',1,50,50),('01DA202414','MEALS',1,90,90),('01DA202414','FRIED RICE',1,100,100),('01DA202414','CHAPATHIS',1,20,20),('01DA202414','NAAN',1,30,30),('01DA202414','BUTTER NAAN',1,35,35),('01DA202414','ICE CREAM',1,55,55),('01DA202414','TEA',1,15,15),('01DA202414','COFFEE',1,15,15),('01DA202414','YOGHURT',1,20,20),('01DA202414','TOMATO SOUP',1,60,60),('01DA202414','PANI PURI',1,55,55),('01DA202414','BHEL PURI',6,60,360),('01DA202414','PAV BHAJI',1,68,68),('01DA202414','BREAD',1,10,10),('01DA202414','POORI',1,30,30),('01DA202414','PEANUT',1,15,15),('01DA202414','BIRYANI',1,90,90),('01DA202414','CURD',1,20,20),('01DA202414','FOOD',1,80,80),('01DA202414','PASTA',1,120,120),('07DA202415','BUTTER NAAN',3,35,105),('07DA202415','ICE CREAM',1,55,55),('01DA202416','BUTTER NAAN',1,35,35),('01DA202416','ICE CREAM',1,55,55);
/*!40000 ALTER TABLE `bills2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-04 13:12:14