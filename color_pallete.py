import sublime, sublime_plugin
import json
import os

class ColorPallete(sublime_plugin.TextCommand):
  def run(self, edit):
    print(sublime.active_window().extract_variables())
    variables = sublime.active_window().extract_variables()
    pallete_path = os.path.join(variables['folder'], "color_pallete.json")
    with open(pallete_path) as data_file:    
      pallete_file = json.load(data_file)
    print(pallete_file)
    pallete = pallete_file["pallete"]
    out = "<style>a {font-size:30px}</style>"
    for index, color  in enumerate(pallete):
      
      out += '<a style="color: %s" href="%s">■</a>&nbsp;' %(color, color)
      if ((index + 1) % 5) == 0 : out +='<br>' 
    self.view.show_popup(out, on_navigate=self.onClick, max_width = 320, max_height = 240)

  def onClick(self, color):
    self.view.run_command("insert_color_data", {"args":{'color':color}})
    self.view.hide_popup()

class InsertColorData(sublime_plugin.TextCommand):
  def run(self, edit, args):
    self.view.insert(edit, self.view.sel()[0].begin(), args['color'])