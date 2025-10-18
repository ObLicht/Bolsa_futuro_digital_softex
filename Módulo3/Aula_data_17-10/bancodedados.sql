CREATE DATABASE loja;

USE loja;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2),
    estoque INT
);

INSERT INTO produtos (nome, preco, estoque)
VALUES('Camiseta', 59.90, 30),
('Calça Jeans', 120.00, 15),
('Tênis', 250.00, 10);

SELECT * FROM produtos; -- mostrar tudo

SELECT nome, preco FROM produtos; -- mostrar só nome e preço

SELECT nome FROM produtos WHERE preco > 100;

UPDATE produtos SET estoque = estoque + 5 WHERE nome = 'Camiseta';

DELETE FROM produtos WHERE id = 3;

SELECT * FROM produtos; 



