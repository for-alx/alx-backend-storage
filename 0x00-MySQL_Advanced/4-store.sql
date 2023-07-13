-- Triger that decreases the quantity of
-- item for each new insert opration
CREATE TRIGGER decrease_quant
AFTER  INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
