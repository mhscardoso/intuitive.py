from pydantic import BaseModel
from datetime import date

class OperadorSchema(BaseModel):
	Registro_ANS:              str
	CNPJ:                      str | None
	Razao_Social:              str | None
	Nome_Fantasia:             str | None
	Modalidade:                str | None
	Logradouro:                str | None
	Numero:                    str | None
	Complemento:               str | None
	Bairro:                    str | None
	Cidade:                    str | None
	UF:                        str | None
	CEP:                       str | None
	DDD:                       str | None
	Telefone:                  str | None
	Fax:                       str | None
	Endereco_eletronico:       str | None
	Representante:             str | None
	Cargo_Representante:       str | None
	Regiao_de_Comercializacao: str | None
	Data_Registro_ANS:         date | None
