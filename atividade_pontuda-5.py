import os
import csv
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Livros:
    titulo_do_livro : str
    autor_do_livro : str
    data_do_lancamento : int
    genero : str
