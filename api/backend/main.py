from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

from fastapi_pagination import Page, add_pagination, paginate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/operadoras/")
def read_operadoras(Razao_Social: str = None, db: Session = Depends(get_db)) -> Page[schemas.OperadorSchema]:
    operadoras = crud.get_ops_all(db, Razao_Social)
    return operadoras


@app.get("/operadoras/{ans_number}", response_model=schemas.OperadorSchema)
def read_op_by_ans_number(ans_number: str, db: Session = Depends(get_db)):
    db_operadora = crud.get_op_by_ans_number(db, ans_number=ans_number)
    if db_operadora is None:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")
    return db_operadora


@app.get("/operadoras/{CNPJ}", response_model=schemas.OperadorSchema)
def read_op_by_ans_number(CNPJ: str, db: Session = Depends(get_db)):
    db_operadora = crud.get_op_by_CNPJ(db, CNPJ=CNPJ)
    if db_operadora is None:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")
    return db_operadora


add_pagination(app)
