"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    t0 = pd.read_csv("tbl0.tsv", sep='\t')
    t2 = pd.read_csv(r'C:\Universidad\Sistemas\Fundamentos de analítica\Labs\\2024-2-LAB-02-pandas-upar1234\\files\input\tbl2.tsv', sep='\t')
    t0 = t0.loc[:,['c0','c1']]
    t2 = t2.loc[:,['c0', 'c5b']]
    df = pd.merge(
        t0,
        t2,
        on='c0'
    )
    df = df.groupby('c1')['c5b'].sum()
    print(df)
    return df
    
pregunta_13()