import ast
import inspect


class DynamicPythonCodeGenerator:
    def __init__(self, template):

        self.template = template

    def complete_template(self, **kwargs):

        try:
            self.completed_code = self.template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Brakujący klucz w danych wejściowych: {e}")

    def validate_code(self):

        try:
            ast.parse(self.completed_code)
        except SyntaxError as e:
            raise SyntaxError(f"Błąd w składni kodu: {e}")

    def execute_code(self, globals_dict=None, locals_dict=None):

        globals_dict = globals_dict if globals_dict is not None else {}
        locals_dict = locals_dict if locals_dict is not None else {}

        exec(self.completed_code, globals_dict, locals_dict)
        return locals_dict



if __name__ == "__main__":

    szablon = """
def {function_name}(x):
    return x + {value}

result = {function_name}({argument})
"""

    generator = DynamicPythonCodeGenerator(szablon)

    try:
        generator.complete_template(function_name="dodaj", value=10, argument=5)

        generator.validate_code()

        locals_ = generator.execute_code()

        print("Wynik:", locals_["result"])

    except (ValueError, SyntaxError) as e:
        print("Błąd:", e)