CREATE DATABASE basetotal;

\c basetotal;

-- Models
CREATE TABLE demons_cont (
	"DATA"              CHAR(10),
	"REG_ANS"           CHAR(7),
	"CD_CONTA_CONTABIL" VARCHAR(15),
	"DESCRICAO"         VARCHAR(255),
	"VL_SALDO_INICIAL"  VARCHAR(20),
	"VL_SALDO_FINAL"    VARCHAR(20)
);


CREATE TABLE operadoras (
	"Registro_ANS"              CHAR(6),
	"CNPJ"                      CHAR(14),
	"Razao_Social"              VARCHAR(255),
	"Nome_Fantasia"             VARCHAR(128),
	"Modalidade"                VARCHAR(128),
	"Logradouro"                VARCHAR(128),
	"Numero"                    VARCHAR(64),
	"Complemento"               VARCHAR(128),
	"Bairro"                    VARCHAR(128),
	"Cidade"                    VARCHAR(128),
	"UF"                        CHAR(2),
	"CEP"                       CHAR(8),
	"DDD"                       CHAR(2),
	"Telefone"                  VARCHAR(20),
	"Fax"                       VARCHAR(20),
	"Endereco_eletronico"       VARCHAR(128),
	"Representante"             VARCHAR(255),
	"Cargo_Representante"       VARCHAR(255),
	"Regiao_de_Comercializacao" VARCHAR(255),
	"Data_Registro_ANS"         DATE
);


-- Copying all files to tables
COPY demons_cont FROM '/data/2022/1T2022.csv' QUOTE '"' DELIMITER ';' ENCODING 'latin1' CSV HEADER;
COPY demons_cont FROM '/data/2022/2T2022.csv' QUOTE '"' DELIMITER ';' ENCODING 'latin1' CSV HEADER;
COPY demons_cont FROM '/data/2022/3T2022.csv' QUOTE '"' DELIMITER ';' ENCODING 'latin1' CSV HEADER;
COPY demons_cont FROM '/data/2022/4T2022.csv' QUOTE '"' DELIMITER ';' ENCODING 'latin1' CSV HEADER;

COPY demons_cont FROM '/data/2023/1T2023.csv' QUOTE '"' DELIMITER ';' ENCODING 'latin1' CSV HEADER;
COPY demons_cont FROM '/data/2023/2T2023.csv' QUOTE '"' DELIMITER ';' ENCODING 'latin1' CSV HEADER;
COPY demons_cont FROM '/data/2023/3T2023.csv' QUOTE '"' DELIMITER ';' ENCODING 'latin1' CSV HEADER;

COPY operadoras FROM '/data/relatorio.csv' QUOTE '"' DELIMITER ';' ENCODING 'latin1' CSV HEADER;


-- Formating float values read as string
UPDATE demons_cont SET VL_SALDO_INICIAL = REPLACE(VL_SALDO_INICIAL, ',','.');
UPDATE demons_cont SET VL_SALDO_FINAL   = REPLACE(VL_SALDO_FINAL  , ',','.');
