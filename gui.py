from modules import functions
import PySimpleGUI as sg


label = sg.Text("Write task")
input_box = sg.InputText(tooltip="Type activity",
                         key="task")
add_button = sg.Button("Add")

window = sg.Window('Time organizer',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            tasks = functions.get_chore_list()
            new_task = values['task'] + "\n"
            tasks.append(new_task)
            functions.write_chore_list(tasks)
        case sg.WIN_CLOSED:
            break
window.close()
