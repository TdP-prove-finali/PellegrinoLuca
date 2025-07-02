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
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
('Push-ups',5,8,'Builds upper body strength',200,'Chest, Triceps, Shoulders','None','Intermediate',51),
('Squats',3,15,'Strengthens lower body',223,'Quadriceps, Hamstrings, Glutes','None','Beginner',52),
('Lunges',6,6,'Improves balance and coordination',275,'Quadriceps, Hamstrings, Glutes','None','Beginner',53),
('Burpees',3,5,'Full body workout',355,'Full body','None','Advanced',54),
('Mountain Climbers',5,10,'Improves cardiovascular fitness',240,'Core, Shoulders, Legs','None','Intermediate',55),
('Jumping Jacks',5,20,'Improves coordination and cardiovascular health',295,'Full Body','None','Beginner',56),
('Bicycle Crunches',2,30,'Targets abdominal muscles',210,'Core','None','Intermediate',57),
('Dips',6,8,'Strengthens triceps and chest',180,'Triceps, Chest','Parallel Bars or Chair','Intermediate',58),
('Pull-ups',3,4,'Builds upper body strength',250,'Back, Biceps','Pull-up Bar','Advanced',59),
('Russian Twists',2,30,'Improves core rotation strength',190,'Core, Obliques','None or Dumbbell','Intermediate',60),
('Leg Raises',4,13,'Strengthens back and legs',315,'Back, Hamstrings, Glutes','Barbell','Intermediate',61),
('Deadlifts',5,5,'Strengthens back and legs',315,'Back, Hamstrings, Glutes','Barbell','Advanced',62),
('Bench Press',2,3,'Builds chest strength',280,'Chest, Triceps','Bench, Barbell','Intermediate',63),
('Rows',4,9,'Improves posture and back strength',260,'Back, Biceps','Dumbbells or Barbell','Intermediate',64),
('Shoulder Press',5,6,'Strengthens shoulders',230,'Shoulders, Triceps','Dumbbells or Barbell','Intermediate',65),
('Calf Raises',2,25,'Builds calf muscles',150,'Calves','None or Dumbbells','Beginner',66),
('Tricep extensions',5,15,'Isolates and strengthens triceps',170,'Triceps','Dumbbells','Intermediate',67),
('Lateral Raises',2,14,'Builds shoulder width',165,'Shoulders','Dumbbells','Intermediate',68),
('Glute Bridges',1,30,'Activates and strengthens glutes',200,'Glutes, Hamstrings','None','Beginner',69),
('Superman',2,22,'Improves lower back strength',180,'Lower Back, Glutes','None','Beginner',70),
('Box Jumps',2,12,'Builds explosive power',320,'Legs, Core','Box or Platform','Advanced',71),
('Kettlebell Swings',3,18,'Improves hip power and cardiovascular fitness',335,'Glutes, Hamstrings, Core','Kettlebell','Intermediate',72),
('Step-ups',8,4,'Builds unilateral leg strength',260,'Quadriceps, Hamstrings, Glutes','Step or Box','Intermediate',73),
('Face Pulls',1,17,'Improves shoulder health and posture',145,'Rear Deltoids, Upper Back','Resistance Band or Cable Machine','Intermediate',74),
('Lat Pulldowns',3,20,'Strengthens back and improves posture',250,'Back, Biceps','Cable Machine','Intermediate',75),
('Reverse Lunges',8,4,'Improves balance and leg strength',270,'Quadriceps, Hamstrings, Glutes','None or Dumbbells','Intermediate',76),
('Plyo Squats',2,4,'Builds lower body power',315,'Quadriceps, Glutes','None','Intermediate',77),
('Scissors Kicks',2,35,'Strengthens lower abs and hip flexors',195,'Lower Abs, Hip Flexors','None','Intermediate',78),
('Tricep Dips',1,25,'Isolates triceps',180,'Triceps','Bench or Chair','Intermediate',79),
('Seated Rows',2,14,'Improves back strength and posture',240,'Back, Biceps','Cable Machine or Resistance Band','Intermediate',80),
('Flutter Kicks',8,8,'Targets lower abs',190,'Lower Abs','None','Intermediate',81),
('Inverted Rows',7,5,'Builds back strength',220,'Back, Biceps','Low Bar or TRX','Intermediate',82),
('Bulgarian Split Squats',10,3,'Improves unilateral leg strength and balance',290,'Quadriceps, Hamstrings, Glutes','Bench or Step','Advanced',83),
('Prone Cobras',2,16,'Improves posture and strengthens upper back',160,'Upper Back, Rear Deltoids','None','Beginner',84),
('Resistance Band Pull-Aparts',5,12,'Improves shoulder health and posture',140,'Upper Back, Rear Deltoids','Resistance Band','Beginner',85),
('Wall Angels',1,14,'Improves shoulder mobility and posture',130,'Shoulders, Upper Back','Wall','Beginner',86),
('Bird Dogs',2,22,'Improves core stability and balance',175,'Core, Lower Back','None','Beginner',87),
('Plyometric Push-ups',1,23,'Builds explosive upper body power',280,'Chest, Triceps, Shoulders','None','Advanced',88),
('Decline Push-ups',1,30,'Targets upper chest',220,'Upper Chest, Triceps','Bench or Step','Advanced',89),
('Incline Push-ups',2,16,'Targets lower chest',180,'Lower Chest, Triceps','Bench or Step','Beginner',90),
('Dead Bugs',5,10,'Improves core stability',165,'Core, Lower Back','None','Beginner',91),
('Pistol Squats',2,2,'Builds unilateral leg strength and balance',300,'Quadriceps, Hamstrings, Glutes','None','Advanced',92),
('Zottman Curls',2,6,'Targets biceps and forearms',155,'Biceps, Forearms','Dumbbells','Intermediate',93),
('Dragon Flags',6,2,'Advanced core exercise',250,'Full Core','Bench or Sturdy Surface','Advanced',94),
('Renegade Rows',5,12,'Improves core stability and upper body strength',280,'Back, Core, Shoulders','Dumbbells','Advanced',95),
('Frog Jumps',7,7,'Builds lower body power and endurance',310,'Quadriceps, Calves, Glutes','None','Intermediate',96),
('Turkish Get-ups',2,12,'Enhances full-body coordination and stability',240,'Full Body, Core, Shoulders','Kettlebell','Advanced',97),
('Bear Crawls',2,35,'Strengthens core and improves mobility',220,'Core, Shoulders, Hips','None','Intermediate',98),
('Windshield Wipers',8,5,'Targets obliques and improves core rotation',200,'Obliques, Core','Pull-up Bar','Advanced',99),
('Thrusters',7,6,'Combines lower body and upper body strength',330,'Legs, Shoulders, Core','Dumbbells or Barbell','Advanced',100),
('Push-ups',7,3,'Builds upper body strength',200,'Chest, Triceps, Shoulders','None','Intermediate',101),
('Squats',7,5,'Strengthens lower body',223,'Quadriceps, Hamstrings, Glutes','None','Beginner',102),
('Lunges',1,30,'Improves balance and coordination',275,'Quadriceps, Hamstrings, Glutes','None','Beginner',103),
('Burpees',5,16,'Full body workout',355,'Full body','None','Advanced',104),
('Mountain Climbers',2,30,'Improves cardiovascular fitness',240,'Core, Shoulders, Legs','None','Intermediate',105),
('Jumping Jacks',2,40,'Improves coordination and cardiovascular health',295,'Full Body','None','Beginner',106),
('Bicycle Crunches',5,7,'Targets abdominal muscles',210,'Core','None','Intermediate',107),
('Dips',3,20,'Strengthens triceps and chest',180,'Triceps, Chest','Parallel Bars or Chair','Intermediate',108),
('Pull-ups',2,14,'Builds upper body strength',250,'Back, Biceps','Pull-up Bar','Advanced',109),
('Russian Twists',5,10,'Improves core rotation strength',190,'Core, Obliques','None or Dumbbell','Intermediate',110),
('Leg Raises',6,7,'Strengthens back and legs',315,'Back, Hamstrings, Glutes','Barbell','Intermediate',111),
('Deadlifts',1,18,'Strengthens back and legs',315,'Back, Hamstrings, Glutes','Barbell','Advanced',112),
('Bench Press',3,1,'Builds chest strength',280,'Chest, Triceps','Bench, Barbell','Intermediate',113),
('Rows',2,18,'Improves posture and back strength',260,'Back, Biceps','Dumbbells or Barbell','Intermediate',114),
('Shoulder Press',1,15,'Strengthens shoulders',230,'Shoulders, Triceps','Dumbbells or Barbell','Intermediate',115),
('Calf Raises',6,8,'Builds calf muscles',150,'Calves','None or Dumbbells','Beginner',116),
('Tricep extensions',2,22,'Isolates and strengthens triceps',170,'Triceps','Dumbbells','Intermediate',117),
('Lateral Raises',8,8,'Builds shoulder width',165,'Shoulders','Dumbbells','Intermediate',118),
('Glute Bridges',6,8,'Activates and strengthens glutes',200,'Glutes, Hamstrings','None','Beginner',119),
('Superman',6,10,'Improves lower back strength',180,'Lower Back, Glutes','None','Beginner',120),
('Box Jumps',8,5,'Builds explosive power',320,'Legs, Core','Box or Platform','Advanced',121),
('Kettlebell Swings',6,6,'Improves hip power and cardiovascular fitness',335,'Glutes, Hamstrings, Core','Kettlebell','Intermediate',122),
('Step-ups',2,25,'Builds unilateral leg strength',260,'Quadriceps, Hamstrings, Glutes','Step or Box','Intermediate',123),
('Face Pulls',5,9,'Improves shoulder health and posture',145,'Rear Deltoids, Upper Back','Resistance Band or Cable Machine','Intermediate',124),
('Lat Pulldowns',10,4,'Strengthens back and improves posture',250,'Back, Biceps','Cable Machine','Intermediate',125),
('Reverse Lunges',3,3,'Improves balance and leg strength',270,'Quadriceps, Hamstrings, Glutes','None or Dumbbells','Intermediate',126),
('Plyo Squats',2,16,'Builds lower body power',315,'Quadriceps, Glutes','None','Intermediate',127),
('Scissors Kicks',6,8,'Strengthens lower abs and hip flexors',195,'Lower Abs, Hip Flexors','None','Intermediate',128),
('Tricep Dips',8,6,'Isolates triceps',180,'Triceps','Bench or Chair','Intermediate',129),
('Seated Rows',5,5,'Improves back strength and posture',240,'Back, Biceps','Cable Machine or Resistance Band','Intermediate',130),
('Flutter Kicks',1,35,'Targets lower abs',190,'Lower Abs','None','Intermediate',131),
('Inverted Rows',5,4,'Builds back strength',220,'Back, Biceps','Low Bar or TRX','Intermediate',132),
('Bulgarian Split Squats',4,4,'Improves unilateral leg strength and balance',290,'Quadriceps, Hamstrings, Glutes','Bench or Step','Advanced',133),
('Prone Cobras',6,4,'Improves posture and strengthens upper back',160,'Upper Back, Rear Deltoids','None','Beginner',134),
('Resistance Band Pull-Aparts',8,3,'Improves shoulder health and posture',140,'Upper Back, Rear Deltoids','Resistance Band','Beginner',135),
('Wall Angels',5,5,'Improves shoulder mobility and posture',130,'Shoulders, Upper Back','Wall','Beginner',136),
('Bird Dogs',6,5,'Improves core stability and balance',175,'Core, Lower Back','None','Beginner',137),
('Plyometric Push-ups',4,4,'Builds explosive upper body power',280,'Chest, Triceps, Shoulders','None','Advanced',138),
('Decline Push-ups',5,6,'Targets upper chest',220,'Upper Chest, Triceps','Bench or Step','Advanced',139),
('Incline Push-ups',2,20,'Targets lower chest',180,'Lower Chest, Triceps','Bench or Step','Beginner',140),
('Dead Bugs',4,4,'Improves core stability',165,'Core, Lower Back','None','Beginner',141),
('Pistol Squats',1,10,'Builds unilateral leg strength and balance',300,'Quadriceps, Hamstrings, Glutes','None','Advanced',142),
('Zottman Curls',5,3,'Targets biceps and forearms',155,'Biceps, Forearms','Dumbbells','Intermediate',143),
('Dragon Flags',1,12,'Advanced core exercise',250,'Full Core','Bench or Sturdy Surface','Advanced',144),
('Renegade Rows',4,8,'Improves core stability and upper body strength',280,'Back, Core, Shoulders','Dumbbells','Advanced',145),
('Frog Jumps',1,30,'Builds lower body power and endurance',310,'Quadriceps, Calves, Glutes','None','Intermediate',146),
('Turkish Get-ups',4,6,'Enhances full-body coordination and stability',240,'Full Body, Core, Shoulders','Kettlebell','Advanced',147),
('Bear Crawls',5,12,'Strengthens core and improves mobility',220,'Core, Shoulders, Hips','None','Intermediate',148),
('Windshield Wipers',1,22,'Targets obliques and improves core rotation',200,'Obliques, Core','Pull-up Bar','Advanced',149),
('Thrusters',2,4,'Combines lower body and upper body strength',330,'Legs, Shoulders, Core','Dumbbells or Barbell','Advanced',150);
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


