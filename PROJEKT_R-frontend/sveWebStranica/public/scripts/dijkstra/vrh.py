class Vrh:
    def __init__(self, naziv, vr, prethodnik):
        self.naziv = naziv
        self.vr = vr
        self.prethodnik = prethodnik
    def __str__(self):
        return f"({self.naziv}, {self.vr}, {self.prethodnik})"
    def __eq__(self, other):
        if isinstance(other, Vrh):
            return self.naziv == other.naziv and self.vr == other.vr
        return False