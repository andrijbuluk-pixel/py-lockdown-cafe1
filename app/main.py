from app.cafe import Cafe
from app.error import VaccineError, NotWearingMaskError


def go_to_cafe(self, friends):
    out = 0
    for cafe in friends:
        try:
            cafe.visit_cafe()
        except VaccineError as e:
            print(e, "All friends should be vaccinated")
            out += 1
        except NotWearingMaskError as e:
            print(e, f"Friends should buy {out} masks")
            out += 1

    else:
        if not out:
            print(f"Friends can go to {self.name}")


