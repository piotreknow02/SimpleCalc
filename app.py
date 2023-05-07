import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

btn_padding = 3

class Calculator(Gtk.Window):
    def __init__(self, app):
        super().__init__(application=app, title="SimpleCalc")

        # Create the grid
        grid = Gtk.Grid()
        grid.set_hexpand(True)
        grid.set_vexpand(True)
        grid.set_column_spacing(btn_padding)
        grid.set_row_spacing(btn_padding)
        self.set_child(grid)

        # Create the entry field
        self.entry = Gtk.Entry()
        self.entry.set_hexpand(True)
        grid.attach(self.entry, 0, 0, 4, 1)

        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        x = 0
        y = 1
        for button_label in buttons:
            button = Gtk.Button(label=button_label)
            button.connect('clicked', self.button_clicked)
            grid.attach(button, x, y, 1, 1)
            x += 1
            if x > 3:
                x = 0
                y += 1

    def button_clicked(self, button):
        # Get the current text from the entry field
        expression = self.entry.get_text()

        # Get the label text of the button clicked
        label = button.get_label()

        # Handle different button actions
        if label == '=':
            try:
                result = eval(expression)
                self.entry.set_text(str(result))
            except Exception as e:
                self.entry.set_text("Error")
        else:
            self.entry.set_text(expression + label)


scalc = Gtk.Application(application_id='com.piotreknow02.SimpleCalc')
def activate(app):
    win = Calculator(app)
    win.present()

# Run the app
scalc.connect('activate', activate)
scalc.run(sys.argv)
