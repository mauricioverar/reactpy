# backend
from fastapi import FastAPI
from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure

app = FastAPI()

# estilos
@component
def Estilos(task):
  counter, set_counter = hooks.use_state(0) # estado

  def handle_click(event):
    set_counter(counter + 1)
    print('click')

  if task['priority'] > 1:
    return html.li(
      {
        'key': task['id'],
        'style': 
        {
          'background': 'yellow',
          'padding': '1rem',
          'border': '1px solid black',
          'margin': '1rem'
        }
      },
      task['text']
    )
  else:
    return html.li(
      {
        'key': task['id'],
        'style': 
          {
            'background': 'skyblue',
            'padding': '1rem',
            'border': '1px solid black',
            'margin': '1rem'
          }
      },
      html.div(
        {
          'style': 
            {
              'display': 'flex',
              'justify-content': 'space-between'
            }
        },
        f"⚠️ {task['text']} - {task['priority']} - {counter}",
        html.button(
          {
            'on_click': handle_click
          },
          'Borrar'
        )
      )
    )

# listado
@component
def TasKlist():

  # datos
  tasks = [
    {
      'id': 0,
      'text': 'desayunar',
      'priority': 1
    },
    {
      'id': 0,
      'text': 'algo',
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
      'priority': 2
    },
    {
      'id': 3,
      'text': 'postre😏',
      'priority': 3
    },
  ]

  # for
  lis = [ Estilos(task) for task in tasks ]

  return html.ul( lis )

# render
@component
def App():  
  return html.main(
    html.h1('mis tareas'),
    html.div(TasKlist())
  )

configure(app, App)

"""
ejecutar

uvicorn main:app --reload



"""
