/* ----------------Creacion de la table client */
CREATE TABLE client (
    id number PRIMARY KEY,
    name varchar(4000),
    email VARCHAR2(20),
    age NUMBER
)

/* Metodo GET */
select * from CLIENT;

/* Metodo POST */
BEGIN
    insert into client (id, name, email, age)
    values (:id, :name, :email, :age);
    :status_code:=201;
    EXCEPTION WHEN OTHERS THEN
    :status_code:=204;
END;

/* Metodo PUT */
BEGIN
    UPDATE client set name = :name, email = :email, age = :age
    WHERE id = :id;
    :status_code:=201;
    EXCEPTION WHEN OTHERS THEN
    :status_code:=204;
END;

/* Metodo DELETE */
BEGIN
    DELETE FROM clien WHERE id = :id;
    :status_code:=201;
    EXCEPTION WHEN OTHERS THEN
    :status_code:=201;
END;

/* Metodo GET basado en un id */
SELECT * FROM client WHERE id = :id





/* ----------------Creacion de la table message */
CREATE TABLE message (
    id NUMBER PRIMARY KEY,
    messagetext VARCHAR2(4000)
)

/* Metodo GET */
select * from MESSAGE;

/* Metodo POST */
BEGIN
    INSERT INTO message (id, messagetext)
    values (:id, :messagetext);
    :status_code:=201;
    EXCEPTION WHEN OTHERS THEN
    :status_code:=204;
END;

/* Metodo PUT */
BEGIN
    UPDATE MESSAGE set (messagetext = :messagetext)
    WHERE id = :id;
    :status_code:=201;
    EXCEPTION WHEN OTHERS THEN
    :status_code:=204;
END;

/* Metodo DELETE */
BEGIN
    DELETE FROM message WHERE id = :id;
    :status_code:=201;
    EXCEPTION WHEN OTHERS THEN
    :status_code:=204;
END;

/* Metodo GET basado en un id */
SELECT * FROM message WHERE id = :id