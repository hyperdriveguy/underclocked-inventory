import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


builder = Gtk.Builder()
builder.add_from_file("main.glade")

window = builder.get_object("main_window")
computer_list_store = builder.get_object("product_list_model")
print(computer_list_store)
for i in computer_list_store:
    print(i[:])
product_view = builder.get_object("computer_product_view")
print(product_view.get_model())


class Handler:
    def on_destroy(self, *args):
        Gtk.main_quit()

    # def onButtonPressed(self, button):
    #     print("Hello World!")

    def on_bool_toggle(self, received, tree_path):
        print(received)
        print(tree_path)
        received.set_radio(not received.get_radio())


builder.connect_signals(Handler())
# computer_list_store.append(['fake product ID', 'fake brand', 'fake model', 'fake form factor', 'fake processor', 'fake memory type', 8000000000, 'fake graphics', 'fake storage', 'fake OS type', 'fake version', 'fake connections', 'fake ports', 'fake display', 'fake other features', 420.69, '1969-04-01', 20.00, 800.21, True, False, None])
window.show_all()

Gtk.main()
