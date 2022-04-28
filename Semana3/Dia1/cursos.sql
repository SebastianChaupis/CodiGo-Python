-- MySQL dump 10.13  Distrib 5.7.33, for Win64 (x86_64)
--
-- Host: localhost    Database: cursos
-- ------------------------------------------------------
-- Server version	5.7.33

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
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alumno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pais` varchar(60) DEFAULT 'Perú',
  `apellido` varchar(100) DEFAULT NULL,
  `nota` double(3,1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno`
--

LOCK TABLES `alumno` WRITE;
/*!40000 ALTER TABLE `alumno` DISABLE KEYS */;
INSERT INTO `alumno` VALUES (1,'Bidget','bblamey0@usgs.gov','Colombia','Blamey',14.0),(2,'Jakob','japril1@domainmarket.com','Brazil','April',16.0),(3,'Hilly','hcummungs2@reverbnation.com','Bolivia','Cummungs',15.0),(4,'Shara','splumptre3@theatlantic.com','Peru','Plumptre',18.0),(5,'Aubrey','aavraham4@japanpost.jp','Brazil','Avraham',14.0),(6,'Ursula','uproudley5@hubpages.com','Colombia','Proudley',17.0),(7,'Jaime','jmaymand6@wired.com','Brazil','Maymand',14.0),(8,'Renae','rkarpfen7@cargocollective.com','Brazil','Karpfen',13.0),(9,'Merrill','mtrosdall8@kickstarter.com','Argentina','Trosdall',10.0),(10,'Elise','ebattram9@hhs.gov','Ecuador','Battram',13.0),(11,'Dionisio','dbonnella@example.com','Chile','Bonnell',14.0),(12,'Zonnya','zroakesb@soup.io','Colombia','Roakes',14.0),(13,'Katine','khilandc@cnn.com','Peru','Hiland',18.0),(14,'Ethel','eroysed@nbcnews.com','Argentina','Royse',14.0),(15,'Leigh','llangere@sciencedirect.com','Brazil','Langer',10.0),(16,'Rica','rlightningf@ycombinator.com','Argentina','Lightning',19.0),(17,'Sasha','strahearng@ibm.com','Peru','Trahearn',20.0),(18,'Ansell','adobneyh@unesco.org','Brazil','Dobney',19.0),(19,'Yard','ylickessi@microsoft.com','Brazil','Lickess',10.0),(20,'Myca','mbleddonj@ucla.edu','Brazil','Bleddon',18.0),(21,'Amye','amewhak@taobao.com','Peru','Mewha',18.0),(22,'Aloin','apowleyl@gnu.org','Argentina','Powley',16.0),(23,'Lloyd','lohalleghanem@stumbleupon.com','Brazil','O\'Halleghane',19.0),(24,'Darrin','dwontern@dot.gov','Brazil','Wonter',18.0),(25,'Thaddus','ttournero@hostgator.com','Colombia','Tourner',19.0),(26,'Lawrence','lunthankp@mit.edu','Brazil','Unthank',17.0),(27,'Leoline','lmarcamq@cisco.com','Argentina','Marcam',14.0),(28,'Di','dgiannottir@macromedia.com','Brazil','Giannotti',11.0),(29,'Rosabelle','rrowatts@digg.com','Argentina','Rowatt',18.0),(30,'Cassi','cdidellot@parallels.com','Peru','Di Dello',11.0),(31,'Dmitri','dskingleu@woothemes.com','Peru','Skingle',10.0),(32,'Karalee','kemertonv@redcross.org','Argentina','Emerton',14.0),(33,'Jerrie','jeytelw@domainmarket.com','Brazil','Eytel',17.0),(34,'Rodrick','rsecretx@gnu.org','Argentina','Secret',13.0),(35,'Trev','tbaffy@mac.com','Colombia','Baff',16.0),(36,'Garry','gfoisterz@cocolog-nifty.com','Peru','Foister',20.0),(37,'Auguste','abelcher10@youtu.be','Argentina','Belcher',16.0),(38,'Maribel','mmcpaik11@nifty.com','Brazil','McPaik',18.0),(39,'Malva','mgoodier12@vk.com','Argentina','Goodier',16.0),(40,'Lorelle','lsiddele13@ebay.co.uk','Brazil','Siddele',18.0),(41,'Casey','cwinchcombe14@usa.gov','Brazil','Winchcombe',18.0),(42,'Raimondo','rarckoll15@whitehouse.gov','Brazil','Arckoll',16.0),(43,'Allayne','aemmanuel16@liveinternet.ru','Colombia','Emmanuel',19.0),(44,'Ezequiel','erichards17@qq.com','Peru','Richards',12.0),(45,'Mercie','mjessopp18@ovh.net','Argentina','Jessopp',19.0),(46,'Blinny','btoop19@who.int','Argentina','Toop',11.0),(47,'Emmott','edumbrall1a@fema.gov','Peru','Dumbrall',13.0),(48,'Lonnard','llindenboim1b@cafepress.com','Brazil','Lindenboim',18.0),(49,'Doyle','dbentham1c@oaic.gov.au','Brazil','Bentham',12.0),(50,'Nertie','njanos1d@ucsd.edu','Ecuador','Janos',11.0),(51,'Rois','rrizzillo1e@bing.com','Peru','Rizzillo',18.0),(52,'Phillipe','pbonhome1f@ftc.gov','Brazil','Bonhome',10.0),(53,'Zolly','zfortey1g@plala.or.jp','Brazil','Fortey',20.0),(54,'Roldan','rcluley1h@seattletimes.com','Brazil','Cluley',20.0),(55,'Jon','jamerici1i@bbb.org','Argentina','Americi',13.0),(56,'Stephannie','sferrer1j@booking.com','Argentina','Ferrer',14.0),(57,'Maddie','mteese1k@skyrock.com','Argentina','Teese',11.0),(58,'Devondra','dgerriets1l@guardian.co.uk','Argentina','Gerriets',13.0),(59,'Omar','ocarlile1m@hostgator.com','Brazil','Carlile',11.0),(60,'Eberto','ecartwight1n@scientificamerican.com','Peru','Cartwight',19.0),(61,'Kathye','ktanby1o@virginia.edu','Ecuador','Tanby',11.0),(62,'Itch','ithieme1p@miitbeian.gov.cn','Brazil','Thieme',19.0),(63,'Jesse','jlivzey1q@omniture.com','Ecuador','Livzey',19.0),(64,'Henrik','hlumby1r@hao123.com','Brazil','Lumby',11.0),(65,'Cari','ccrimin1s@admin.ch','Peru','Crimin',11.0),(66,'Desiree','dsworn1t@businessweek.com','Chile','Sworn',17.0),(67,'Jacquie','jagott1u@reference.com','Brazil','Agott',14.0),(68,'Sutton','statum1v@illinois.edu','Brazil','Tatum',11.0),(69,'Adair','aandress1w@discuz.net','Colombia','Andress',16.0),(70,'Eduardo','ecamerello1x@hao123.com','Brazil','Camerello',12.0),(71,'Lucretia','lgoldsbrough1y@livejournal.com','Peru','Goldsbrough',10.0),(72,'Burgess','babbotts1z@prweb.com','Brazil','Abbotts',12.0),(73,'Enrica','emitchley20@blogs.com','Brazil','Mitchley',15.0),(74,'Tedi','tsorley21@meetup.com','Peru','Sorley',13.0),(75,'Marje','mfalconertaylor22@arizona.edu','Ecuador','Falconer-Taylor',11.0),(76,'Vivia','vgallo23@toplist.cz','Brazil','Gallo',13.0),(77,'Lisle','laudiss24@ocn.ne.jp','Brazil','Audiss',17.0),(78,'Delmore','dmaling25@tiny.cc','Brazil','Maling',11.0),(79,'Sybila','szettler26@gnu.org','Argentina','Zettler',14.0),(80,'Sayre','sgrealy27@bbb.org','Brazil','Grealy',18.0),(81,'Selena','scuxon28@pen.io','Peru','Cuxon',14.0),(82,'Derron','dadshede29@chicagotribune.com','Brazil','Adshede',18.0),(83,'Cathrin','civanuschka2a@booking.com','Brazil','Ivanuschka',13.0),(84,'Harry','hcoltart2b@omniture.com','Brazil','Coltart',11.0),(85,'Quintus','qfidelus2c@yelp.com','Peru','Fidelus',14.0),(86,'Rosene','rbeachamp2d@arstechnica.com','Brazil','Beachamp',20.0),(87,'Tyne','tkale2e@cpanel.net','Brazil','Kale',12.0),(88,'Zora','zmullett2f@google.cn','Peru','Mullett',12.0),(89,'Bertrando','bpercifer2g@exblog.jp','Argentina','Percifer',12.0),(90,'Kip','khamper2h@aol.com','Brazil','Hamper',13.0),(91,'Alfonso','ahylands2i@oracle.com','Peru','Hylands',19.0),(92,'Katlin','ksiman2j@shinystat.com','Brazil','Siman',19.0),(93,'Lutero','lellif2k@xinhuanet.com','Brazil','Ellif',17.0),(94,'Bessie','bmaulkin2l@merriam-webster.com','Peru','Maulkin',10.0),(95,'Sig','sunworth2m@omniture.com','Argentina','Unworth',15.0),(96,'Ekaterina','elau2n@icio.us','Brazil','Lau',16.0),(97,'Filippo','fdumbrall2o@cam.ac.uk','Brazil','Dumbrall',10.0),(98,'Saunderson','sgreguoli2p@diigo.com','Brazil','Greguoli',18.0),(99,'Rossie','rmacilhench2q@nih.gov','Chile','Macilhench',20.0),(100,'Niles','nrussell2r@altervista.org','Brazil','Russell',11.0);
/*!40000 ALTER TABLE `alumno` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-28 12:41:52
