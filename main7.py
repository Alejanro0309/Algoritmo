estudiante=[
    {
        "nombre":"Juan",
        "nota":17
    },
    {
        "nombre":"Jose",
        "nota":19
    },
     {
        "nombre":"Pedro",
        "nota":10
     }
]

estudiante_mayor={"nombre":"nadie","nota":0}
for i in estudiante:
    if i["nota"]> estudiante_mayor["nota"]:
        estudiante_mayor=i
print("el estudiantes con la nota mayor es", estudiante_mayor["nombre"],"con",estudiante_mayor["nota"],"pts")

