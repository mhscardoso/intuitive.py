-- Models
CREATE TABLE operadoras (
	"Registro_ANS"              CHAR(6)      PRIMARY KEY,
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
SET datestyle TO "ISO, YMD";
COPY operadoras  FROM '/data/relatorio.csv'   QUOTE '"' DELIMITER ';' ENCODING 'UTF8' CSV HEADER;
