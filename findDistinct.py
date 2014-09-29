import sublime, sublime_plugin

class findDistinctCommand(sublime_plugin.TextCommand):
    def formatForOutput(self, expr):
        #adding quotes for each expression (optional)
        return '\'{0}\''.format(expr)

    def onDone(self, regexp):
        lines = self.view.find_all(regexp)
        if len(lines) > 0:
            hashTable = {}
            for line in lines:
                hashTable[self.formatForOutput(self.view.substr(line))] = True

            #outputs
            print('Found {0} distinct expresions:'.format(len(hashTable)))
            print(', '.join(hashTable.keys()))
        else:
            print('Nothing found')
        # opens console
        sublime.active_window().run_command("show_panel", {"panel": "console", "toggle": True})

    def run(self, edit):
        # opens dialog
        self.view.window().show_input_panel('Find distinct', '', lambda s: self.onDone(s), None, None)
