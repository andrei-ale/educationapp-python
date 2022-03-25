from flask import Flask, jsonify, request, Response
from InstitutieCursuri import InstitutieCursuri
from CursProgramare import CursProgramare
from CursLimbaStraina import CursLimbaStraina

app = Flask(__name__)

institutie1 = InstitutieCursuri("Telecom Academy", "Bucuresti")

@app.route("/cursuri")
def get_cursuri():
    if len(institutie1.lista_cursuri) == 0:
        return "Eroare ! Nu exista nici un curs.", 404
    return jsonify(institutie1.afiseaza_cursuri()), 200

@app.route("/cursuri/<int:id_curs>")
def get_curs(id_curs):
    if type(institutie1.afiseaza_curs(id_curs)) == str:
        return jsonify(institutie1.afiseaza_curs(id_curs)), 200
    else:
        return jsonify(f"Cursul cu ID-ul: {id_curs} nu exista !"), 404

@app.route("/cursuri", methods = ["POST"])
def adauga_curs():
    if len(institutie1.lista_cursuri) == 15:
        return jsonify("Institutia a atins limita maxima de cursuri ! Nu mai pot fi adaugate alte cursuri !"), 403
    curs_nou = request.get_json()
    if curs_nou["tip_curs"] == "Programare":
        try:
            cursul_meu = CursProgramare(curs_nou["nume"], curs_nou["instructor"], curs_nou["data_incepere"],
                    curs_nou["nivel"], curs_nou["tip_examen"])
        except ValueError as e:
            return jsonify(str(e)), 400
    elif curs_nou["tip_curs"] == "Limba straina":
        try:
            cursul_meu = CursLimbaStraina(curs_nou["nume"], curs_nou["instructor"], curs_nou["data_incepere"],
                    curs_nou["nivel"])
        except ValueError as e:
            return jsonify(str(e)), 400
    institutie1.adauga_curs(cursul_meu)
    return jsonify(curs_nou), 200

@app.route("/cursuri/<int:id_curs>", methods = ["PUT"])
def actualizeaza_curs(id_curs):
    signal = False
    for curs in institutie1.lista_cursuri:
        if curs.id == id_curs:
            cursul_meu = curs
            signal= True
    if signal == False:
        return jsonify(f"Cursul cu ID-ul: {id_curs} nu exista !"), 404

    cursul_meu.nume = request.json.get("nume", cursul_meu.nume)
    cursul_meu.instructor = request.json.get("instructor", cursul_meu.instructor)
    cursul_meu.data_incepere = request.json.get("data_incepere", cursul_meu.data_incepere)
    if isinstance(cursul_meu, CursProgramare):
        if request.json.get("nivel"):
            if request.json.get("nivel") not in CursProgramare.niveluri_curs_programare:
                return jsonify("Nivelul cursului nu exista!"), 400
        if request.json.get("tip_examen"):
            if request.json.get("tip_examen") not in CursProgramare.tipuri_examen:
                return jsonify("Tipul examenului nu exista!"), 400
        cursul_meu.nivel = request.json.get("nivel", cursul_meu.nivel)
        cursul_meu.tip_examen = request.json.get("tip_examen", cursul_meu.tip_examen)

    if isinstance(cursul_meu, CursLimbaStraina):
        if request.json.get("nivel"):
            if request.json.get("nivel") not in CursLimbaStraina.niveluri_curs_limba_straina:
                return jsonify("Nivelul cursului nu exista!"), 400
        cursul_meu.nivel = request.json.get("nivel", cursul_meu.nivel)
    return jsonify(cursul_meu.__str__()), 201


@app.route("/cursuri/<int:id_curs>", methods = ["DELETE"])
def sterge_curs(id_curs):
    if len(institutie1.lista_cursuri) == 0:
        return jsonify("Eroare ! Nu exista nici un curs."), 404
    if institutie1.sterge_curs(id_curs) == "Not found!":
        return jsonify(f"Cursul cu ID-ul: {id_curs} nu exista !"), 404
    else:
        return Response(status = 204)


if __name__ == "__main__":
    app.run(debug=True)
