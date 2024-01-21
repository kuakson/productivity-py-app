from modules import functions
import PySimpleGUI as sg


label = sg.Text("Write task")
input_box = sg.InputText(tooltip="Type activity",
                         key="task")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")

list_box = sg.Listbox(values=functions.get_chore_list(), key="tasks",
                      enable_events=True, size=[45, 10])
window = sg.Window('Time organizer',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            tasks = functions.get_chore_list()
            new_task = values['task'] + "\n"
            tasks.append(new_task)
            functions.write_chore_list(tasks)
            window['tasks'].update(values=tasks)
        case "Edit":
            task_to_edit = values['tasks'][0]
            new_task = values['task']

            tasks = functions.get_chore_list()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            functions.write_chore_list(tasks)
            window['tasks'].update(values=tasks)
        case 'tasks':
            window['task'].update(value=values['tasks'][0])
        case sg.WIN_CLOSED:
            break
window.close()
