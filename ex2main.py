# con framework fastapi, con el modulo uvicorn para el servidor
# pip install fastapi uvicorn

from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

app = FastAPI()

# para ejecutar en frontend @component
""" @component
def App():
  # return html.h1("hola")
  return html.header(
    html.h1("hola a mi app"),
    html.button('click')
  )
configure(app, App) """

@component
def GoodComponent():
  return (
    html.p("hola a mi good componente"),
    
  )

@component
def BadComponent():
  msg = 'este es err'
  raise RuntimeError(msg)

@component
def TasKlist():
  tasks = [
    {
      'id': 0,
      'text': 'desayunar',
      'priority': 1
    },
    {
      'id': 1,
      'text': 'almorzar',
      'priority': 2
    },
    {
      'id': 2,
      'text': 'cenar',
      'priority': 3
    },
    {
      'id': 3,
      'text': 'postre😏',
      'priority': 4
    },
  ]

  lis = [html.li(task['text']) for task in tasks]
  return html.ul(
    lis
  )

@component
def App():
  return html.section(
    html.h1('lista'),
    html.ul(
      html.li('reactPy'),
      html.li('FastAPI'),
      html.li('algo')
    ),
    html.img({
      'src': 'http://picsum.photos/id/237/500/300',
      'style': {
        'width': '50%'
      },
      'alt': 'imagen'
    })
    # GoodComponent(),
    # BadComponent()
  )
configure(app, App)

# ejecutar en modo desarrollo 
#  uvicorn main:app --reload

# modo (debug) en powershell
# $env:REACTPY_DEBUG_MODE = "1"
"""
uvicorn main:app --reload



"""
