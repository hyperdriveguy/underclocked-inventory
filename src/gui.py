import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


builder = Gtk.Builder()
builder.add_from_file("main.glade")

window = builder.get_object("main_window")
computer_list_store = builder.get_object("product_list_model")
computer_list_store.append(['fake product ID',
                            'fake brand',
                            'fake model',
                            'fake form factor',
                            'fake processor',
                            'fake memory type 8000000000 GB',
                            'fake graphics',
                            'fake storage',
                            'fake OS type fake version',
                            'fake display',
                            False])
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

    def on_col_click(self, data):
        print('Clicked Connectivity column')
        print(data)
        computer_list_store.append(['fake product ID',
                                    'fake brand',
                                    'fake model',
                                    'fake form factor',
                                    'fake processor',
                                    'fake memory type 8000000000 GB',
                                    'fake graphics',
                                    'fake storage',
                                    'fake OS type fake version',
                                    'fake display',
                                    False])

    def on_bool_toggle(self, received, tree_path):
        print('received', received)
        print('path', tree_path)
        print('model', computer_list_store[tree_path][-1])
        computer_list_store[tree_path][-1] = not computer_list_store[tree_path][-1]
    
    def on_product_select(self, tree_view, row_index, tree_view_column):
        print('Product selected:')
        print(tree_view, row, col)
        print(computer_list_store[row])
        for c in computer_list_store[row]:
            print(c)
        print('-' * 35)

builder.connect_signals(Handler())
window.show_all()

Gtk.main()
