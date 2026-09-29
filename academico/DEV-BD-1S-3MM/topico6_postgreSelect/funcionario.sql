-- tabela utilizada com exemplo para consultas

CREATE TABLE funcionario (
    id_funcionario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    salario NUMERIC(10, 2) NOT NULL,
    departamento VARCHAR(40) NOT NULL,
    dependente INTEGER check (dependente>=0),
    dt_nascimento DATE NOT NULL
);
INSERT INTO funcionario (nome, salario, departamento, dt_nascimento, dependente) VALUES
('Astrogildo', 2000.00, 'RH', '1971-02-17', NULL),
('Irene', 2000.00, 'RH', '1978-05-27', 2),
('Perla', 2200.00, 'RH', '1978-09-01', 1),
('Manuela', 5500.00, 'TI', '1988-03-07', 1),
('Roberta', 4500.00, 'TI', '1987-09-12', 2),
('Ramon', 4200.30, 'TI', '1988-12-22', 3),
('Astolfo', 7800.55, 'DIRETORIA', '1979-03-15', 3),
('Mariana', 7800.55, 'DIRETORIA', '1975-03-15', 4),
('Anacleto', 3500.00, 'COMERCIAL', '1979-09-25', NULL),
('Mariana', 3600.00, 'COMERCIAL', '1979-07-22', 2);