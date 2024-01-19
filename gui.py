from modules import functions
import PySimpleGUI as sg

label = sg.Text("Write task")
input_box = sg.InputText(tooltip="Type activity")
add_button = sg.Button("Add")

window = sg.Window('Time organizer', layout=[[label], [input_box, add_button]])
window.read()
window.close()
