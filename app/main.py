from fastapi import FastAPI

app = FastAPI()

@app.get("/year")
def get_year(year: int):
    return {"mensaje": f"Estás en el año {year} de tu carrera"}
