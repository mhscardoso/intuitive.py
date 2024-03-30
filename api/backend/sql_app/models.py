from sqlalchemy import Boolean, Column, String, Integer, Table

from .database import Base

class Operador(Base):
    __tablename__ = "operadoras"

    Registro_ANS              = Column(String, primary_key=True)
    CNPJ                      = Column(String, unique=True)
    Razao_Social              = Column(String)
    Nome_Fantasia             = Column(String)
    Modalidade                = Column(String)
    Logradouro                = Column(String)
    Numero                    = Column(String)
    Complemento               = Column(String)
    Bairro                    = Column(String)
    Cidade                    = Column(String)
    UF                        = Column(String)
    CEP                       = Column(String)
    DDD                       = Column(String)
    Telefone                  = Column(String)
    Fax                       = Column(String)
    Endereco_eletronico       = Column(String)
    Representante             = Column(String)
    Cargo_Representante       = Column(String)
    Regiao_de_Comercializacao = Column(String)
    Data_Registro_ANS         = Column(String)
