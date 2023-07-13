-- Trigger that resets the vlid_email attribute
-- if email is changed(update)

DELIMITER $$
CREATE TRIGGER validate
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
	SET NEW.valid_email = 0;
	END IF;
END$$
DELIMITER ;$$
