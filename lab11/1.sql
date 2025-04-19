CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, first_name TEXT, phone_number TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        phonebook.id, 
        phonebook.first_name::TEXT, 
        phonebook.phone_number::TEXT
    FROM phonebook
    WHERE phonebook.first_name ILIKE '%' || pattern || '%'
       OR phonebook.phone_number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
