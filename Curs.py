class Curs:

    id = 0

    def __init__(self, nume, instructor, data_incepere):
        self.id = Curs.id
        self.nume = nume
        self.instructor = instructor
        self.data_incepere = data_incepere
        Curs.id += 1

    def __str__(self):
        raise NotImplementedError("Metoda nu a fost inca definita.")