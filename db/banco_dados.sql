CREATE DATABASE IF NOT EXISTS db_eventos;

USE db_eventos;

-- tabela do usuario
CREATE TABLE IF NOT EXISTS tb_usuario(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(150) NOT NULL,
    user_email VARCHAR(90) NOT NULL,
    user_password VARCHAR(90) NOT NULL,
    user_cpf VARCHAR(90) NOT NULL,
    user_uf VARCHAR(2),
    user_image BLOB,
    user_type BOOLEAN
);

-- tabela do fornecedor
CREATE TABLE IF NOT EXISTS tb_fornecerdor(
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    user_supplier_id INT NOT NULL,
    phone_number VARCHAR(90),
    contact_email VARCHAR(90),
    FOREIGN KEY (user_supplier_id) REFERENCES tb_usuario(user_id)
);

-- tabela do endereço do evento
CREATE TABLE IF NOT EXISTS tb_local(
local_id INT PRIMARY KEY AUTO_INCREMENT,
    owner_supplier_id INT NOT NULL,
    address VARCHAR(150) NOT NULL,
    address_lat DECIMAL,
    address_long DECIMAL,
    FOREIGN KEY (owner_supplier_id) REFERENCES tb_fornecerdor(supplier_id)
);

-- tabela das categorias do evento
CREATE TABLE IF NOT EXISTS tb_categoria_eventos (
category_id INT PRIMARY KEY AUTO_INCREMENT,
    tipo_categoria VARCHAR(90) NOT NULL UNIQUE
);

-- tabela do evento
CREATE TABLE IF NOT EXISTS tb_eventos(
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    owner_event INT NOT NULL,
    location_event INT NOT NULL,
    event_name VARCHAR(90) NOT NULL,
    event_category INT NOT NULL,
    event_description LONGTEXT,
    FOREIGN KEY (owner_event) REFERENCES tb_fornecerdor(supplier_id),
    FOREIGN KEY (location_event) REFERENCES tb_local(local_id),
    FOREIGN KEY (event_category) REFERENCES tb_categoria_eventos(category_id)
);

-- tabela da imagens dos eventos
CREATE TABLE IF NOT EXISTS tb_imagem_evento (
image_id INT PRIMARY KEY AUTO_INCREMENT,
    image_event_id INT NOT NULL,
    event_images BLOB,
    FOREIGN KEY (image_event_id) REFERENCES tb_eventos(event_id)
);

-- tabela dos reviews
CREATE TABLE IF NOT EXISTS tb_review(
review_id INT PRIMARY KEY AUTO_INCREMENT,
    user_review_id INT NOT NULL,
    event_review_id INT NOT NULL,
    rating DECIMAL NOT NULL,
    comments TEXT NOT NULL,
    review_time TIMESTAMP NOT NULL,
    FOREIGN KEY (user_review_id) REFERENCES tb_usuario(user_id),
    FOREIGN KEY (event_review_id) REFERENCES tb_eventos(event_id)
);

-- tabela das mensagens entre fornecedor e cliente
-- CREATE TABLE IF NOT EXISTS tb_message(
-- message_id INT PRIMARY KEY AUTO_INCREMENT,
--     user_message_id INT NOT NULL,
--     recipient_id INT NOT NULL,
--     message TEXT NOT NULL,
--     message_time TIMESTAMP NOT NULL,
--     FOREIGN KEY (user_message_id) REFERENCES tb_usuario(user_id),
--     FOREIGN KEY (recipient_id) REFERENCES tb_fornecerdor(user_supplier_id)
-- );
