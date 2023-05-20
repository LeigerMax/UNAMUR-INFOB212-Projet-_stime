DELIMITER //

CREATE TRIGGER note_trop_petite_trop_grande
BEFORE INSERT ON AVIS
FOR EACH ROW
BEGIN
     IF NEW.Note < 0 THEN
          signal sqlstate '45000' set message_text = "Plus petit que 0";
     END IF;
     IF NEW.Note > 10 THEN
          signal sqlstate '45000' set message_text = "Plus grand que 10";
     END IF;
END //

CREATE TRIGGER portefeuille_vide_ou_trop_rempli
BEFORE INSERT ON UTILISATEUR
FOR EACH ROW
BEGIN
     IF (NEW.Portefeuille < 0) THEN
          signal sqlstate '45000' set message_text = "Plus petit que 0";
     END IF;
     IF (NEW.Portefeuille > 2000) THEN
          signal sqlstate '45000' set message_text = "Plus grand que 2000";
     END IF;
END //

CREATE TRIGGER nouveau_proprietaire
BEFORE UPDATE ON TRANSACTION
FOR EACH ROW
BEGIN
     IF (OLD.Acheteur != NEW.Acheteur) THEN
          UPDATE OBJET_INSTANCE
          SET Possesseur = New.Acheteur
          WHERE Id = OLD.Objet;
     END IF;
END //

CREATE TRIGGER on_peut_pas_racheter_ce_quon_vend
BEFORE UPDATE ON TRANSACTION
FOR EACH ROW
BEGIN
     IF (OLD.Revendeur = NEW.Acheteur) THEN
          signal sqlstate '45000' set message_text = "On ne peut racheter ce que l'on vend";
     END IF;
END //

CREATE TRIGGER pas_acheter_dlc_sans_avoir_jeu
AFTER UPDATE ON UTILISATEUR_JEU
FOR EACH ROW
BEGIN
   DECLARE isNotDLC BOOLEAN;
   DECLARE jeuDeBase INT;
   DECLARE jeuDeBaseAchete INT;

   SET isNotDLC = (SELECT ISNULL(DLC) FROM JEU WHERE GameId = NEW.Jeu);

   IF (NOT isNotDLC) THEN
      SET jeuDeBase = (SELECT DLC FROM JEU WHERE GameId = NEW.Jeu);
      SET jeuDeBaseAchete = (SELECT Count(Jeu) FROM UTILISATEUR_JEU WHERE Utilisateur = NEW.Utilisateur AND Jeu = jeuDeBase);
      IF (jeuDeBaseAchete = 0) THEN
          signal sqlstate '45000' set message_text = "On ne peut pas acheter un DLC sans avoir achetÃ© le jeu de base";
      END IF;
   END IF;
END //

DELIMITER ;