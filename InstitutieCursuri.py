from CursProgramare import CursProgramare
from CursLimbaStraina import CursLimbaStraina


class InstitutieCursuri:

    def __init__(self, nume, locatie):
        self.nume = nume
        self.locatie = locatie
        self.lista_cursuri = []

    def afiseaza_cursuri(self):
        cursuri = []
        for curs in self.lista_cursuri:
            curs_curent = curs.__str__()
            cursuri.append(curs_curent)
        return cursuri

    def afiseaza_curs(self, id_curs):
        signal = False
        for curs in self.lista_cursuri:
            if curs.id == id_curs:
                curs_curent = curs.__str__()
                signal = True
                return curs_curent
        if signal == False:
            return "Not Found!"


    def adauga_curs(self, curs_nou):
        self.lista_cursuri.append(curs_nou)

    def sterge_curs(self, id_curs):
        signal = False
        for curs in self.lista_cursuri:
            if curs.id == id_curs:
                self.lista_cursuri.remove(curs)
                signal = True
        if signal == False:
            return "Not found!"

    def salveaza_in_fisier(self, nume_fisier):
        with open(f"{nume_fisier}.txt", mode="wt") as file:
            file.write("Institutia noastra va pune la dispozitie urmatoarele cursuri:\n\n")
            nr_crt = 1
            for curs in self.lista_cursuri:
                if isinstance(curs, CursProgramare):
                    file.write(f"{nr_crt}. {curs.nume} - Instructor: {curs.instructor}"
                               f" - Data incepere: {curs.data_incepere} - Nivel: {curs.nivel}"
                               f" - Tip examen: {curs.tip_examen}\n")
                elif isinstance(curs, CursLimbaStraina):
                    file.write(f"{nr_crt}. {curs.nume} - Instructor: {curs.instructor} "
                               f"- Data incepere: {curs.data_incepere} - Nivel: {curs.nivel}\n")
                nr_crt += 1
