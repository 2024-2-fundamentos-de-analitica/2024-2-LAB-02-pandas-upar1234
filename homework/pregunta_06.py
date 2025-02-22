"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def esta_o_no(l:list, x):
    if x in l:
        pass
    else:
        l.append(x)
    return l
def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.
    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    """
    l = []
    df = pd.read_csv("files\\input\\tbl1.tsv", sep = '\t')
    df = df['c4'].map(lambda x : x.capitalize())
    for i in range(len(df)):
        df.map(lambda x : esta_o_no(l, df[i]).sort())
    print(l)
    return l
    
    
pregunta_06()