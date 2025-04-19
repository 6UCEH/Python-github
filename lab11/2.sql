CREATE OR REPLACE PROCEDURE insert_or_update_user(name TEXT, phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = name) THEN
        UPDATE phonebook SET phone_number = phone WHERE first_name = name;
    ELSE
        INSERT INTO phonebook (first_name, phone_number) VALUES (name, phone);
    END IF;
END;
$$;
