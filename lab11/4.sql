CREATE OR REPLACE FUNCTION get_phonebook_page(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, first_name TEXT, phone_number TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        phonebook.id, 
        phonebook.first_name::TEXT, 
        phonebook.phone_number::TEXT
    FROM phonebook
    ORDER BY id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;
