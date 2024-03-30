from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas

from fastapi_pagination.ext.sqlalchemy import paginate


def get_op_by_ans_number(db: Session, ans_number: str):
    return db.query(models.Operador).filter(models.Operador.Registro_ANS == ans_number).first()


def get_op_by_CNPJ(db: Session, CNPJ: str):
    return db.query(models.Operador).filter(models.Operador.CNPJ == CNPJ).first()


def get_ops_by_UF(db: Session, UF: str, limit: int = 20):
    return db.query(models.Operador).filter(models.Operador.UF == UF).limit(limit).all()


def get_ops_by_NF(db: Session, Nome_Fantasia: str, limit: int = 20):
    return db.query(models.Operador).filter(models.Operador.Nome_Fantasia.like("%{}%".format(Nome_Fantasia))).limit(limit).all()


def get_ops_all(db: Session, RS: str):
    if RS == None:
        return paginate(db, select(models.Operador))

    return paginate(db, select(models.Operador).where(models.Operador.Razao_Social.ilike(f"%{RS}%")))
