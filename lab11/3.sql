CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
    invalid_data TEXT := '';
BEGIN
    WHILE i <= array_length(names, 1) LOOP
        IF phones[i] IS NULL OR length(phones[i]) < 5 THEN
            invalid_data := invalid_data || 'Invalid: ' || names[i] || ', ';
        ELSE
            CALL insert_or_update_user(names[i], phones[i]);
        END IF;
        i := i + 1;
    END LOOP;

    RAISE NOTICE 'Некорректные данные: %', invalid_data;
END;
$$;
