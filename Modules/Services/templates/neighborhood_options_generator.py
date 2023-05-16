# with open("opciones.js", "w") as archivo_js:
#     with open("../choices.py", "r") as archivo_py:
#         archivo_js.write("function getOptions() {\n")
#         archivo_js.write("  return [")
#         for linea in archivo_py:
#             linea = linea.strip()
#             if linea.startswith("[") and linea.endswith("]"):
#                 opciones = linea[1:-1].split(",")
#                 opciones = [opcion.strip() for opcion in opciones]
#                 opciones_js = "[" + ", ".join(opciones) + "]"
#                 archivo_js.write(opciones_js)
#         archivo_js.write("];\n}\n")


