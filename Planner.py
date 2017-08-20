import tkinter

_DEFAULT_FONT = ('Helvetica', 14)

day_to_abbrev = {'Monday': 'mon', 'Tuesday': 'tues', 'Wednesday': 'wed', 'Thursday': 'thurs', 'Friday': 'fri', 'Saturday': 'sat', 'Sunday': 'sun'}
days_in_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class MenuDialog:
    def __init__(self, current_plan):
        self._dialog_window = tkinter.Toplevel()
        
        label = tkinter.Label(master = self._dialog_window, text = 'Enter plan:', font = _DEFAULT_FONT)
        label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        
        self.plan_entry = tkinter.Entry(master = self._dialog_window, width = 20, font = _DEFAULT_FONT)
        self.plan_entry.insert(0, current_plan)
        self.plan_entry.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self.plan = ''
        
        
        button_frame = tkinter.Frame(master = self._dialog_window)
        button_frame.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10,
                          sticky = tkinter.W + tkinter.E + tkinter.S)
        
        ok_button = tkinter.Button(
        master = button_frame, text = 'OK', font = _DEFAULT_FONT,
            command = self._ok_pressed)
        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = _DEFAULT_FONT,
            command = self._cancel_pressed)
        
        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)
        self.cancelled = False
    def show(self):
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()
        
    def _ok_pressed(self):
        self.plan = self.plan_entry.get()
        self._dialog_window.destroy()

    def _cancel_pressed(self):
        self._dialog_window.destroy()
        self.cancelled = True
    def get_plan(self):
        return self.plan
    def get_cancelled(self):
        return self.cancelled
    
class PlannerApplication():
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._root_window.configure(background='#99e6ff')
        self.all_days = {'Monday': '', 'Tuesday': '', 'Wednesday': '', 'Thursday': '', 'Friday': '',
            'Saturday': '', 'Sunday': ''}
        
        #Buttons to edit days
        self._monday_button = tkinter.Button(master = self._root_window, text = 'Monday',
                                             font = _DEFAULT_FONT, command = self._edit_monday)
        self._tuesday_button = tkinter.Button(master = self._root_window, text = 'Tuesday',
                                             font = _DEFAULT_FONT, command = self._edit_tuesday)
        self._wednesday_button = tkinter.Button(master = self._root_window, text = 'Wednesday',
                                             font = _DEFAULT_FONT, command = self._edit_wednesday)
        self._thursday_button = tkinter.Button(master = self._root_window, text = 'Thursday',
                                             font = _DEFAULT_FONT, command = self._edit_thursday)
        self._friday_button = tkinter.Button(master = self._root_window, text = 'Friday',
                                             font = _DEFAULT_FONT, command = self._edit_friday)
        self._saturday_button = tkinter.Button(master = self._root_window, text = 'Saturday',
                                             font = _DEFAULT_FONT, command = self._edit_saturday)    
        self._sunday_button = tkinter.Button(master = self._root_window, text = 'Sunday',
                                             font = _DEFAULT_FONT, command = self._edit_sunday)       
        
        self._monday_button.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.N)
        self._tuesday_button.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tkinter.N)
        self._wednesday_button.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = tkinter.N)
        self._thursday_button.grid(row = 0, column = 3, padx = 10, pady = 10, sticky = tkinter.N)
        self._friday_button.grid(row = 0, column = 4, padx = 10, pady = 10, sticky = tkinter.N)
        self._saturday_button.grid(row = 0, column = 5, padx = 10, pady = 10, sticky = tkinter.N)
        self._sunday_button.grid(row = 0, column = 6, padx = 10, pady = 10, sticky = tkinter.N)
        
        self._mon_plan = tkinter.Label(master = self._root_window, text = '', font = _DEFAULT_FONT, wraplength = 150, background = '#99e6ff')
        self._tues_plan = tkinter.Label(master = self._root_window, text = '', font = _DEFAULT_FONT, wraplength = 150, background = '#99e6ff')
        self._wed_plan = tkinter.Label(master = self._root_window, text = '', font = _DEFAULT_FONT, wraplength = 150, background = '#99e6ff')
        self._thurs_plan = tkinter.Label(master = self._root_window, text = '', font = _DEFAULT_FONT, wraplength = 150, background = '#99e6ff')
        self._fri_plan = tkinter.Label(master = self._root_window, text = '', font = _DEFAULT_FONT, wraplength = 150, background = '#99e6ff')
        self._sat_plan = tkinter.Label(master = self._root_window, text = '', font = _DEFAULT_FONT, wraplength = 150, background = '#99e6ff')
        self._sun_plan = tkinter.Label(master = self._root_window, text = '', font = _DEFAULT_FONT, wraplength = 150, background = '#99e6ff')
        
        self._mon_plan.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.N)
        self._tues_plan.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = tkinter.N)
        self._wed_plan.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = tkinter.N)
        self._thurs_plan.grid(row = 1, column = 3, padx = 10, pady = 10, sticky = tkinter.N)
        self._fri_plan.grid(row = 1, column = 4, padx = 10, pady = 10, sticky = tkinter.N)
        self._sat_plan.grid(row = 1, column = 5, padx = 10, pady = 10, sticky = tkinter.N)
        self._sun_plan.grid(row = 1, column = 6, padx = 10, pady = 10, sticky = tkinter.N)
        
        self.save_button = tkinter.Button(master = self._root_window, text = 'Save', 
                                          font = _DEFAULT_FONT, command = self.save_plans)
        
        self.save_button.grid(row = 2, column = 5, padx = 10, pady = 10, sticky = tkinter.N)
        
        self.load_button = tkinter.Button(master = self._root_window, text = 'Load',
                                          font = _DEFAULT_FONT, command = self.load_plans)
        self.load_button.grid(row = 2, column = 6, padx = 10, pady = 10, sticky = tkinter.N)
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        self._root_window.columnconfigure(2, weight = 1)
        self._root_window.columnconfigure(3, weight = 1)
        self._root_window.columnconfigure(4, weight = 1)
        self._root_window.columnconfigure(5, weight = 1)
        self._root_window.columnconfigure(6, weight = 1)
        
    def _edit_monday(self):    
        self._edit_day('Monday')
        
    def _edit_tuesday(self):    
        self._edit_day('Tuesday')
        
    def _edit_wednesday(self):    
        self._edit_day('Wednesday')
        
    def _edit_thursday(self):    
        self._edit_day('Thursday')
        
    def _edit_friday(self):    
        self._edit_day('Friday')
        
    def _edit_saturday(self):    
        self._edit_day('Saturday')
        
    def _edit_sunday(self):    
        self._edit_day('Sunday')
        
    def _edit_day(self, day):
        dialog = MenuDialog(self.all_days[day])
        dialog.show()
        if not dialog.get_cancelled():
            self.all_days[day] = dialog.get_plan()
            abbreviated = day_to_abbrev[day]
            exec("self._" + abbreviated + "_plan['text'] = dialog.get_plan()")
        
    def start(self):
        self._root_window.mainloop()
        
    def save_plans(self):
        savefile = open('save.txt', 'w')
        save_string = ''
        for day in days_in_order:
            save_string += self.all_days[day] + '\n'
        savefile.write(save_string.rstrip('\n'))
        savefile.close()
    
    def load_plans(self):
        try:
            self.all_days = {'Monday': '', 'Tuesday': '', 'Wednesday': '', 'Thursday': '', 'Friday': '',
            'Saturday': '', 'Sunday': ''}
            for plan in ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']:
                exec("self._" + plan + "_plan['text'] = ''")
            savefile = open('save.txt', 'r')
            for day, plan in zip(days_in_order, savefile):
                self.all_days[day] = plan.rstrip('\n')
                abbreviated = day_to_abbrev[day]
                exec("self._" + abbreviated + "_plan['text'] = " + "'" + plan.rstrip('\n') + "'")
            savefile.close()
        except FileNotFoundError:
            pass
        

if __name__ == '__main__':
    PlannerApplication().start()