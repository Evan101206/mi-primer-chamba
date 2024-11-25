alumno = {
    "nombre": "alexandra",
    "matricula": "a171206",
    "ead": 17,
    "semestre": "quinto",
    "calificaciones": {
        "matematicas": 5,
        "fisica": 5,
        "programacion": 9,
        "quimica": 7,
},
"direccion": {
    "calle": "montaña rusa",
    "ciudad": "calera",
    "codigo_postal": "205",
},
"telefono": "478-124-1351",
"email": "murilloarleth21@gmail.com"
}
print(alumno["nombre"])
print(alumno["calificaciones"])

print("la calificacion del alumno es: ")
print(alumno["calificaciones"]["programacion"])