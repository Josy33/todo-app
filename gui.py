import function
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo" , key = "todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout = [[label], [input_box], [add_button]],
                   font=('Helvetica', 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = function.get_todos()
            new_todo = value['todo'] + "/n"
            todos.append(new_todo)
            function.write_todos('FILEPATH', 'todos')
        case sg.WIN_CLOSED:
            break


window.close()
