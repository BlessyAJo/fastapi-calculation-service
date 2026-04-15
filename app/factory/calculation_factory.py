from app.models.calculation import Addition, Subtraction, Multiplication, Division


class CalculationFactory:

    @staticmethod
    def create(a: float, b: float, op_type: str):

        mapping = {
            "addition": Addition,
            "subtraction": Subtraction,
            "multiplication": Multiplication,
            "division": Division
        }

        cls = mapping.get(op_type.lower())

        if not cls:
            raise ValueError(
                "Invalid operation type. Must be addition, subtraction, multiplication, or division."
            )

        return cls(a=a, b=b)