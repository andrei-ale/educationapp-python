from Curs import Curs


class CursProgramare(Curs):

    niveluri_curs_programare = ["Associate", "Professional", "Expert"]
    tipuri_examen = ["teoretic", "practic", "proiect"]

    def __init__(self, nume, instructor, data_incepere, nivel, tip_examen):
        super().__init__(nume, instructor, data_incepere)
        self.id = Curs.id
        self.set_nivel(nivel)
        self.set_tip_examen(tip_examen)

    def __str__(self):
        return f"ID: {self.id} - Nume: {self.nume} - Instructor: {self.instructor} - Data incepere: {self.data_incepere}" \
               f" - Nivel: {self.nivel} - Tip examen: {self.tip_examen}"

    def get_nivel(self):
        return self.nivel

    def set_nivel(self, nivel):
        if nivel in self.niveluri_curs_programare:
            self.nivel = nivel
        else:
            raise ValueError("Nivelul cursului nu exista !")

    def get_tip_examen(self):
        return self.tip_examen

    def set_tip_examen(self,tip_examen):
        if tip_examen in self.tipuri_examen:
            self.tip_examen = tip_examen
        else:
            raise ValueError("Tipul examenului nu exista !")

