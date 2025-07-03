/*M!999999\- enable the sandbox mode */
-- MariaDB dump 10.19-11.7.2-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: fit_exercises
-- ------------------------------------------------------
-- Server version	11.4.3-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `exercises`
--

CREATE DATABASE IF NOT EXISTS fit_exercises;
USE fit_exercises;


DROP TABLE IF EXISTS `exercises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `exercises` (
  `Name of Exercise` varchar(50) DEFAULT NULL,
  `Sets` int(11) DEFAULT NULL,
  `Reps` int(11) DEFAULT NULL,
  `Benefit` varchar(50) DEFAULT NULL,
  `Burns Calories (per 30 min)` int(11) DEFAULT NULL,
  `Target Muscle Group` varchar(50) DEFAULT NULL,
  `Equipment Needed` varchar(50) DEFAULT NULL,
  `Difficulty Level` varchar(50) DEFAULT NULL,
  `id_exercise` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_exercise`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises`
--

LOCK TABLES `exercises` WRITE;
/*!40000 ALTER TABLE `exercises` DISABLE KEYS */;
INSERT INTO `exercises` VALUES
('Push-ups',3,15,'Builds upper body strength',200,'Chest, Triceps, Shoulders','None','Intermediate',1),
('Squats',4,12,'Strengthens lower body',223,'Quadriceps, Hamstrings, Glutes','None','Beginner',2),
('Lunges',3,10,'Improves balance and coordination',275,'Quadriceps, Hamstrings, Glutes','None','Beginner',3),
('Burpees',3,10,'Full body workout',355,'Full Body','None','Advanced',4),
('Mountain Climbers',3,20,'Improves cardiovascular fitness',240,'Core, Shoulders, Legs','None','Intermediate',5),
('Jumping Jacks',3,30,'Improves coordination and cardiovascular health',295,'Full Body','None','Beginner',6),
('Bicycle Crunches',3,20,'Targets abdominal muscles',210,'Core','None','Intermediate',7),
('Dips',3,12,'Strengthens triceps and chest',180,'Triceps, Chest','Parallel Bars or Chair','Intermediate',8),
('Pull-ups',3,8,'Builds upper body strength',250,'Back, Biceps','Pull-up Bar','Advanced',9),
('Russian Twists',3,20,'Improves core rotation strength',190,'Core, Obliques','None or Dumbbell','Intermediate',10),
('Leg Raises',3,15,'Strengthens lower abs',185,'Lower Abs','None','Intermediate',11),
('Deadlifts',4,8,'Strengthens back and legs',315,'Back, Hamstrings, Glutes','Barbell','Advanced',12),
('Bench Press',4,10,'Builds chest strength',280,'Chest, Triceps','Bench, Barbell','Intermediate',13),
('Rows',3,12,'Improves posture and back strength',260,'Back, Biceps','Dumbbells or Barbell','Intermediate',14),
('Shoulder Press',3,10,'Strengthens shoulders',230,'Shoulders, Triceps','Dumbbells or Barbell','Intermediate',15),
('Calf Raises',3,20,'Builds calf muscles',150,'Calves','None or Dumbbells','Beginner',16),
('Tricep Extensions',3,12,'Isolates and strengthens triceps',170,'Triceps','Dumbbells','Intermediate',17),
('Lateral Raises',3,12,'Builds shoulder width',165,'Shoulders','Dumbbells','Intermediate',18),
('Glute Bridges',3,15,'Activates and strengthens glutes',200,'Glutes, Hamstrings','None','Beginner',19),
('Superman',3,12,'Improves lower back strength',180,'Lower Back, Glutes','None','Beginner',20),
('Box Jumps',4,10,'Builds explosive power',320,'Legs, Core','Box or Platform','Advanced',21),
('Kettlebell Swings',3,15,'Improves hip power and cardiovascular fitness',335,'Glutes, Hamstrings, Core','Kettlebell','Intermediate',22),
('Step-ups',3,12,'Builds unilateral leg strength',260,'Quadriceps, Hamstrings, Glutes','Step or Box','Intermediate',23),
('Face Pulls',3,15,'Improves shoulder health and posture',145,'Rear Deltoids, Upper Back','Resistance Band or Cable Machine','Intermediate',24),
('Lat Pulldowns',3,12,'Strengthens back and improves posture',250,'Back, Biceps','Cable Machine','Intermediate',25),
('Reverse Lunges',3,10,'Improves balance and leg strength',270,'Quadriceps, Hamstrings, Glutes','None or Dumbbells','Intermediate',26),
('Plyo Squats',3,12,'Builds lower body power',315,'Quadriceps, Glutes','None','Intermediate',27),
('Scissors Kicks',3,20,'Strengthens lower abs and hip flexors',195,'Lower Abs, Hip Flexors','None','Intermediate',28),
('Tricep Dips',3,12,'Isolates triceps',180,'Triceps','Bench or Chair','Intermediate',29),
('Seated Rows',3,12,'Improves back strength and posture',240,'Back, Biceps','Cable Machine or Resistance Band','Intermediate',30),
('Flutter Kicks',3,20,'Targets lower abs',190,'Lower Abs','None','Intermediate',31),
('Inverted Rows',3,10,'Builds back strength',220,'Back, Biceps','Low Bar or TRX','Intermediate',32),
('Bulgarian Split Squats',3,10,'Improves unilateral leg strength and balance',290,'Quadriceps, Hamstrings, Glutes','Bench or Step','Advanced',33),
('Prone Cobras',3,12,'Improves posture and strengthens upper back',160,'Upper Back, Rear Deltoids','None','Beginner',34),
('Resistance Band Pull-Aparts',3,15,'Improves shoulder health and posture',140,'Upper Back, Rear Deltoids','Resistance Band','Beginner',35),
('Wall Angels',3,10,'Improves shoulder mobility and posture',130,'Shoulders, Upper Back','Wall','Beginner',36),
('Bird Dogs',3,10,'Improves core stability and balance',175,'Core, Lower Back','None','Beginner',37),
('Plyometric Push-ups',3,8,'Builds explosive upper body power',280,'Chest, Triceps, Shoulders','None','Advanced',38),
('Decline Push-ups',3,12,'Targets upper chest',220,'Upper Chest, Triceps','Bench or Step','Advanced',39),
('Incline Push-ups',3,12,'Targets lower chest',180,'Lower Chest, Triceps','Bench or Step','Beginner',40),
('Dead Bugs',3,12,'Improves core stability',165,'Core, Lower Back','None','Beginner',41),
('Pistol Squats',3,5,'Builds unilateral leg strength and balance',300,'Quadriceps, Hamstrings, Glutes','None','Advanced',42),
('Zottman Curls',3,10,'Targets biceps and forearms',155,'Biceps, Forearms','Dumbbells','Intermediate',43),
('Dragon Flags',3,8,'Advanced core exercise',250,'Full Core','Bench or Sturdy Surface','Advanced',44),
('Renegade Rows',3,10,'Improves core stability and upper body strength',280,'Back, Core, Shoulders','Dumbbells','Advanced',45),
('Frog Jumps',4,15,'Builds lower body power and endurance',310,'Quadriceps, Calves, Glutes','None','Intermediate',46),
('Turkish Get-ups',3,5,'Enhances full-body coordination and stability',240,'Full Body, Core, Shoulders','Kettlebell','Advanced',47),
('Bear Crawls',3,20,'Strengthens core and improves mobility',220,'Core, Shoulders, Hips','None','Intermediate',48),
('Windshield Wipers',3,12,'Targets obliques and improves core rotation',200,'Obliques, Core','Pull-up Bar','Advanced',49),
('Thrusters',4,10,'Combines lower body and upper body strength',330,'Legs, Shoulders, Core','Dumbbells or Barbell','Advanced',50),
('Squats',3,15,'Strengthens lower body',223,'Quadriceps, Hamstrings, Glutes','None','Beginner',52),
('Lunges',6,6,'Improves balance and coordination',275,'Quadriceps, Hamstrings, Glutes','None','Beginner',53),
('Burpees',8,4,'Full body workout',355,'Full body','None','Advanced',54),
('Jumping Jacks',5,20,'Improves coordination and cardiovascular health',295,'Full Body','None','Beginner',56),
('Dips',6,8,'Strengthens triceps and chest',180,'Triceps, Chest','Parallel Bars or Chair','Intermediate',58),
('Pull-ups',5,4,'Builds upper body strength',250,'Back, Biceps','Pull-up Bar','Advanced',59),
('Calf Raises',2,25,'Builds calf muscles',150,'Calves','None or Dumbbells','Beginner',66),
('Glute Bridges',1,30,'Activates and strengthens glutes',200,'Glutes, Hamstrings','None','Beginner',69),
('Superman',2,22,'Improves lower back strength',180,'Lower Back, Glutes','None','Beginner',70),
('Box Jumps',5,12,'Builds explosive power',320,'Legs, Core','Box or Platform','Advanced',71),
('Prone Cobras',2,16,'Improves posture and strengthens upper back',160,'Upper Back, Rear Deltoids','None','Beginner',84),
('Resistance Band Pull-Aparts',5,12,'Improves shoulder health and posture',140,'Upper Back, Rear Deltoids','Resistance Band','Beginner',85),
('Wall Angels',1,14,'Improves shoulder mobility and posture',130,'Shoulders, Upper Back','Wall','Beginner',86),
('Bird Dogs',2,22,'Improves core stability and balance',175,'Core, Lower Back','None','Beginner',87),
('Plyometric Push-ups',3,23,'Builds explosive upper body power',280,'Chest, Triceps, Shoulders','None','Advanced',88),
('Decline Push-ups',3,30,'Targets upper chest',220,'Upper Chest, Triceps','Bench or Step','Advanced',89),
('Incline Push-ups',2,16,'Targets lower chest',180,'Lower Chest, Triceps','Bench or Step','Beginner',90),
('Dead Bugs',5,10,'Improves core stability',165,'Core, Lower Back','None','Beginner',91),
('Pistol Squats',4,2,'Builds unilateral leg strength and balance',300,'Quadriceps, Hamstrings, Glutes','None','Advanced',92),
('Dragon Flags',7,2,'Advanced core exercise',250,'Full Core','Bench or Sturdy Surface','Advanced',94),
('Renegade Rows',5,12,'Improves core stability and upper body strength',280,'Back, Core, Shoulders','Dumbbells','Advanced',95),
('Turkish Get-ups',3,12,'Enhances full-body coordination and stability',240,'Full Body, Core, Shoulders','Kettlebell','Advanced',97),
('Thrusters',5,6,'Combines lower body and upper body strength',330,'Legs, Shoulders, Core','Dumbbells or Barbell','Advanced',100);
/*!40000 ALTER TABLE `exercises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'fit_exercises'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;


