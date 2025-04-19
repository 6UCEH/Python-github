CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = value OR phone_number = value;
END;
$$;
