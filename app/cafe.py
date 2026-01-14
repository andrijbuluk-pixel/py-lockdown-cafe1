from app.error import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError
from datetime import datetime

class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        exp = visitor["vaccine"]["expiration_date"]

        if not visitor["vaccine"]:
            raise NotVaccinatedError

        elif exp < datetime.today().day:
            raise OutdatedVaccineError

        elif not visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError

        else:
            print(f"Welcome to {self.name}")