import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

class Handler:

    def button_clicked(self, button):
        name = Gtk.Buildable.get_name(button)

        if (name in active_tags):
            active_tags.remove(name)
        else:
            active_tags.append(name)
            bounds = buffer.get_selection_bounds()
            if len(bounds) != 0:
                start, end = bounds
                buffer.apply_tag_by_name(name, start, end)

    def font(self, button):
        buffer.get_tag_table().remove(buffer.get_tag_table().lookup("font"))
        tag_font = buffer.create_tag("font", font=font_chooser.get_font())
        Handler.edit_selection(self, tag_font)

    def edit_input(buffer, iter, text, len):
        for x in active_tags:
            print(x)
        new_pos = buffer.get_insert()

        #for x in active_tags:
        buffer.apply_tag_by_name("bold", buffer.get_iter_at_mark(buffer.get_mark("old_pos")), buffer.get_iter_at_mark(new_pos))
        old_pos = new_pos





builder = Gtk.Builder()
builder.add_from_file("/home/thomas/Documents/TestNotepad2.glade")
textview = builder.get_object("textview")
buffer = textview.get_buffer()
font_chooser = builder.get_object("font_chooser")

tag_bold = buffer.create_tag("bold", weight=Pango.Weight.BOLD)
tag_underline = buffer.create_tag("underline", underline=Pango.Underline.SINGLE)
tag_italic = buffer.create_tag("italics", style=Pango.Style.ITALIC)

tag_font = buffer.create_tag("font", font=font_chooser.get_font())

active_tags = ["font"]

buffer.create_mark("old_pos", buffer.get_iter_at_mark(buffer.get_insert()), True)

builder.connect_signals(Handler())
buffer.connect("insert-text", Handler.edit_input)

window = builder.get_object("MainWindow")
window.show_all()

Gtk.main()
