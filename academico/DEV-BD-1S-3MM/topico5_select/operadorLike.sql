CREATE TABLE veiculo (
    id_veiculo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    ano_fabricacao INT NOT NULL,
    preco DECIMAL(9, 2) NOT NULL,
    cor VARCHAR(30),
    data_registro DATE
);

-- DECIMAL (9,2) 9 999 999.99 

INSERT INTO veiculo (marca, modelo, ano_fabricacao, preco, cor, data_registro) VALUES
('Chevrolet', 'Onix Plus', 2024, 85990.00, 'Preto', '2024-05-15');

INSERT INTO veiculo (marca, modelo, ano_fabricacao, preco, cor, data_registro) VALUES
('Hyundai', 'HB20 Vision', 2023, 72500.00, 'Branco', '2024-05-15');

INSERT INTO veiculo (marca, modelo, ano_fabricacao, preco, cor, data_registro) VALUES
('Volkswagen', 'T-Cross Comfortline', 2024, 135000.00, 'Cinza', '2024-05-16');

INSERT INTO veiculo (marca, modelo, ano_fabricacao, preco, cor, data_registro) VALUES
('Ford', 'Ranger XLT', 2023, 230500.00, 'Vermelho', '2024-05-16');

INSERT INTO veiculo (marca, modelo, ano_fabricacao, preco, cor, data_registro) VALUES
('Jeep', 'Renegade Longitude', 2022, 115000.00, 'Verde', '2024-05-17');

INSERT INTO veiculo (marca, modelo, ano_fabricacao, preco, cor, data_registro) VALUES
('Fiat', 'Strada Freedom', 2024, 105990.00, 'Prata', '2024-05-17');

INSERT INTO veiculo (marca, modelo, ano_fabricacao, preco, cor, data_registro) VALUES
('Renault', 'Kwid Zen', 2024, 68000.00, 'Azul', '2024-05-18');

INSERT INTO veiculo (marca, modelo, ano_fabricacao, preco, cor, data_registro) VALUES
('Honda', 'HR-V EXL', 2023, 155900.00, 'Branco', '2024-05-18');

INSERT INTO veiculo (marca, modelo, ano_fabricacao, preco, cor, data_registro) VALUES
('Toyota', 'Corolla Altis Premium', 2024, 175000.00, 'Preto', '2024-05-19');

INSERT INTO veiculo (marca, modelo, ano_fabricacao, preco, cor, data_registro) VALUES
('Nissan', 'Kicks Advance', 2023, 110500.00, 'Cinza', '2024-05-19');

select * from veiculo;

 -- selecione os campos modelo, com apelido (alias) Carro,
 -- marca, preco com apelido valor
 -- da tabela veciulo ordenado pelo modelo
 
 
 select 
 marca as Fabricante, modelo as Carro, preco as Valor 
 from veiculo 
 order by modelo;
 
 -- selecione apenas o campo cor e mostre os valores 
 -- sem repetição ordenado pela cor
 
 select distinct cor
 from veiculo
 order by cor;
 
 -- selecione o campo modelo, com apelido carro,
 -- preco com apelido valor, preco com 10% de desconnto
 -- com apelido desconto 10%, da tabela veiculo
 -- ordenado pelo preco de forma decrescente
 
 select
  modelo as Carro, preco as Valor, preco*0.9 as "Desconto 10%"
 from 
  veiculo
 order by 
  preco desc;
  
  
select 2025 % 2 as "resto divisão por 2";


-- selecione a cor e o ano de fabricação
-- da tabela veiculo para todos os carros
-- que tenha a cor azul  ou que seja do
-- ano de fabricação 2024


select
  cor as Cor, ano_fabricacao as "Ano de fabricação"
from 
  veiculo
where cor="azul" or ano_fabricacao=2024;


select modelo,cor
from veiculo
where cor in ('Preto' , 'Branco');

select modelo,cor
from veiculo
where cor not in ('Preto' , 'Branco');

select * from veiculo;

select * from veiculo --  começa por R
where modelo like 'R%';

select * from veiculo  --  termina por e
where modelo like '%e';


select * from veiculo -- ro no meio
where modelo like '%ro%';

/*
selecione as marcas que tenham 4 letras e 
a primeira letra seja F
*/

select * from veiculo
where marca like '____';

-- selecione todas as marcas onde a
-- penultima letra seja a


-- select marca
-- from veiculo
-- where marca like '%a_';

select marca,modelo,cor, ano_fabricacao,preco
from veiculo
where cor = "preto";
