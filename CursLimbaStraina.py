from Curs import Curs


class CursLimbaStraina(Curs):

    niveluri_curs_limba_straina = ["A1", "B1", "B2", "C1", "C2"]

    def __init__(self, nume, instructor, data_incepere, nivel):
        super().__init__(nume, instructor, data_incepere)
        self.id = Curs.id
        self.set_nivel(nivel)

    def __str__(self):
        return f"ID: {self.id} - Nume: {self.nume} - Instructor: {self.instructor} - Data incepere: {self.data_incepere}" \
               f"Nivel: {self.nivel}"

    def get_nivel(self):
        return self.nivel

    def set_nivel(self, nivel):
        if nivel in self.niveluri_curs_limba_straina:
            self.nivel = nivel
        else:
            raise ValueError("Nivelul cursului nu exista !")