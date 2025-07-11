import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows
    

@app.get("/superheroesDC")
def get_superheroesDC():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows


@app.get("/superheroesMarvel")
def get_superheroesMV():
    rows = ["ironman", "capitan america", "thor", "hulk", "black widow", "spiderman", "antman", "doctor strange"]
    return rows

@app.get("/cursosPlatzi")
def get_cursos():
    rows = ["Docker", "Kubernetes", "Python", "FastAPI", "NodeJS", "ReactJS", "Angular", "VueJS"]
    return rows
