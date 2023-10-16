# usando el framework starlette
# pip install "reactpy[starlette]"

from reactpy import component, html, run

# para ejecutar en frontend @component
@component
def App():
  # return html.h1("hola")
  return html.header(
    html.h1("hola"),
    html.button('click')
  )
run(App)
# python main.py

# con framework fastapi, con el modulo uvicorn para el servidor