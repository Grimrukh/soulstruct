from contextlib import contextmanager
from functools import wraps
import tkinter as tk
from tkinter.constants import *
from tkinter import filedialog, messagebox, ttk

__all__ = ['BaseWindow']

_GRID_KEYWORDS = {'column', 'columnspan', 'in', 'ipadx', 'ipady', 'padx', 'pady', 'row', 'rowspan', 'sticky'}


def _bind_to_mousewheel(_, frame):
    frame.bind_all("<MouseWheel>", lambda event: frame.yview_scroll(-1 * (event.delta // 120), 'units'))


def _unbind_to_mousewheel(_, frame):
    frame.unbind_all("<MouseWheel>")


def _embed_component(component_func):
    """ Handles labels and scrollbars for any decorated widget function. """

    @wraps(component_func)
    def component_with_label(self, frame=None,
                             label='', label_font_type=None, label_font_size=None, label_position=None,
                             label_fg=None, label_bg=None, scrollbar=False, **kwargs):

        grid_kwargs = self.grid_defaults.copy()
        grid_kwargs.update({key: kwargs.pop(key) for key in list(kwargs.keys()) if key in _GRID_KEYWORDS})

        for dim in {'row', 'column'}:
            current_dim = getattr(self, 'current_' + dim)
            if dim not in grid_kwargs:
                if current_dim is None:
                    grid_kwargs[dim] = 0
                else:
                    grid_kwargs[dim] = current_dim
                    setattr(self, 'current_' + dim, current_dim + 1)
            elif current_dim is not None:
                raise ValueError(f"You cannot specify {dim} with a keyword while auto_{dim}s is in effect.")

        if frame is None:
            frame = self.master_frame if self.current_frame is None else self.current_frame

        if label_position is None:
            if component_func.__name__ in {'Checkbutton', 'Entry'}:
                label_position = 'left'
            else:
                label_position = 'above'

        if label:
            if label_bg is None:
                label_bg = kwargs.get('bg', self.STYLE_DEFAULTS['bg'])
            if label_fg is None:
                label_fg = kwargs.get('text_fg', self.STYLE_DEFAULTS['text_fg'])
            if label_font_type is None:
                label_font_type = self.FONT_DEFAULTS['label_font_type']
            if label_font_size is None:
                label_font_size = self.FONT_DEFAULTS['label_font_size']
            inherit_bg = frame.cget('bg')
            frame = tk.Frame(frame, bg=inherit_bg)
            label = tk.Label(frame, text=label, font=(label_font_type, label_font_size), fg=label_fg, bg=label_bg)

        if scrollbar:
            inherit_bg = frame.cget('bg')
            frame_with_scrollbar = tk.Frame(frame, bg=inherit_bg)
            component = component_func(self, frame=frame, **kwargs)
            scrollbar = tk.Scrollbar(frame, command=component.yview)
            component.grid(row=0, column=0)
            scrollbar.grid(row=0, column=1, sticky=NS)
            component.config(bd=0, yscrollcommand=scrollbar.set)
            component.bind('<Enter>', lambda _, f=component: _bind_to_mousewheel(_, f))
            component.bind('<Leave>', lambda _, f=component: _unbind_to_mousewheel(_, f))
            if label:
                if label_position == 'left':
                    label.grid(row=0, column=0, padx=(0, 1))
                    frame_with_scrollbar.grid(row=0, column=1)
                elif label_position == 'right':
                    label.grid(row=0, column=1, padx=(-10, 0))
                    frame_with_scrollbar.grid(row=0, column=0)
                elif label_position == 'above':
                    label.grid(row=0, column=0)
                    frame_with_scrollbar.grid(row=1, column=0)
                elif label_position == 'below':
                    label.grid(row=1, column=0)
                    frame_with_scrollbar.grid(row=0, column=0)
                else:
                    raise ValueError(f"Invalid label position {label_position}. "
                                     f"Must be 'left', 'right', 'above', 'below'.")
                if grid_kwargs:
                    frame.grid(**grid_kwargs)
            elif grid_kwargs:
                frame_with_scrollbar.grid(**grid_kwargs)
        else:
            component = component_func(self, frame=frame, **kwargs)
            if label:
                if label_position == 'left':
                    label.grid(row=0, column=0, padx=(0, 2))
                    component.grid(row=0, column=1)
                elif label_position == 'right':
                    label.grid(row=0, column=1, padx=(2, 0))
                    component.grid(row=0, column=0)
                elif label_position == 'above':
                    label.grid(row=0, column=0)
                    component.grid(row=1, column=0)
                elif label_position == 'below':
                    label.grid(row=1, column=0)
                    component.grid(row=0, column=0)
                else:
                    raise ValueError(f"Invalid label position {label_position}. "
                                     f"Must be 'left', 'right', 'above', 'below'.")
                if grid_kwargs:
                    frame.grid(**grid_kwargs)
            elif grid_kwargs:
                component.grid(**grid_kwargs)

        return component

    return component_with_label


# noinspection PyPep8Naming
class BaseWindow(tk.Toplevel):
    FONT_DEFAULTS = {
        'label_font_type': 'Roboto',
        'label_font_size': 12,
        'heading_font_type': 'Roboto',
        'heading_font_size': 15,
    }

    FileDialog = filedialog

    STYLE_DEFAULTS = {
        'bg': '#222',
        'text_fg': '#FFF',
        'text_cursor_fg': '#FFF',
        'disabled_fg': '#888',
        'disabled_bg': '#444',
        'readonly_bg': '#444',
    }

    def __init__(self, window_title, master=None):
        """ Base class for a simple interactive tkinter window, with simplified methods for adding and arranging
        elements and command functions. """

        # List of variables (so they aren't destroyed).
        self._variables = []

        # Initialize window.
        super().__init__(master)
        self.title(window_title)
        self.iconname(window_title)
        self.focus_force()

        self.style = ttk.Style()
        self.set_notebook_style()
        self.grid_defaults = {}
        self.current_row = None
        self.current_column = None

        # Current frame tracked, defaults to master frame.
        self.master_frame = self.current_frame = self.Frame(frame=self, row=0, column=0)

        # Disable default root if used.
        if master is None:
            self.master.withdraw()

    def set_geometry(self, master=None, dimensions=None, absolute_position=None, relative_position=None,
                     transient=False):
        """ Set the size and position of this window. Should be called in your window's constructor after all widgets
        have been initialized, unless you already know the exact dimensions you want.

        'dimensions' should be (width, height) in pixels, and will default to the dimensions requested by the window.

        'absolute_position' should be used to specify coordinates in pixels on the screen (where 0, 0 is the bottom-left
        corner), and 'relative_position' should be used to specify coordinates as a proportion of the size of the
        window's master (where 0, 0 is the top-left corner). You cannot use both arguments. If the master does not have
        a mapped size, and 'relative_position' has been requested, an error will be raised.

        If neither type of position is given, the window will default to the middle of the screen. And no matter what
        you specify, the window will attempt to remain fully visible.

        A 'transient' window won't show up in the task bar on Windows, is always drawn on top of its master, and is
        automatically hidden when the master is iconified or withdrawn.
        """
        if master is None:
            master = self.master

        if absolute_position is not None and relative_position is not None:
            raise ValueError("You cannot specify both 'absolute_position' and 'relative_position' of the window.")
        self.withdraw()  # Remain invisible while we figure out the geometry
        if transient:
            self.transient(master)
        self.update_idletasks()  # Actualize geometry information

        w_width, w_height = dimensions if dimensions is not None else self.winfo_reqwidth(), self.winfo_reqheight()

        if relative_position is not None and master.winfo_ismapped():
            rel_x, rel_y = relative_position
            m_width = master.winfo_width()
            m_height = master.winfo_height()
            m_x = master.winfo_rootx()
            m_y = master.winfo_rooty()
            w_x = int(m_x + (m_width - w_width) * rel_x)
            w_y = int(m_y + (m_height - w_height) * rel_y)
        else:
            m_width = master.winfo_screenwidth()
            m_height = master.winfo_screenheight()
            if absolute_position is None:
                absolute_position = (m_width / 2, m_height / 2)
            w_x = int(absolute_position[0] - (w_width / 2))
            w_y = int(absolute_position[1] - (w_height / 2))

        # Ensure that this window does not go off the screen.
        if w_x + w_width > master.winfo_screenwidth():
            w_x = master.winfo_screenwidth() - w_width
        elif w_x < 0:
            w_x = 0
        if w_y + w_height > master.winfo_screenheight():
            w_y = master.winfo_screenheight() - w_height
        elif w_y < 0:
            w_y = 0
        self.geometry(f'{w_width:d}x{w_height:d}+{w_x:d}+{w_y:d}')
        self.deiconify()  # Become visible at the desired location

    def set_notebook_style(self):
        self.style.theme_use('alt')
        self.style.configure(
            'TNotebook', background=self.STYLE_DEFAULTS['bg'], tabmargins=[2, 10, 2, 0], tabposition=N)
        self.style.configure(
            'TNotebook.Tab', background='#555555', foreground='#FFFFFF', padding=[15, 1],
            font=('Roboto', 16))
        self.style.map(
            'TNotebook.Tab', background=[('selected', '#774444')], expand=[('selected', [5, 3, 3, 0])])

    def start_auto_rows(self, start=0):
        self.current_row = start

    def stop_auto_rows(self):
        self.current_row = None

    def start_auto_columns(self, start=0):
        self.current_column = start

    def stop_auto_columns(self):
        self.current_column = None

    def set_style_defaults(self, kwargs_dict, text=False, cursor=False, entry=False):
        kwargs_dict.setdefault('bg', self.STYLE_DEFAULTS.get('bg', None))
        if text:
            kwargs_dict.setdefault('fg', self.STYLE_DEFAULTS.get('text_fg', None))
        if cursor:
            kwargs_dict.setdefault('insertbackground', self.STYLE_DEFAULTS.get('text_cursor_fg', None))
        if entry:
            kwargs_dict.setdefault('disabledforeground', self.STYLE_DEFAULTS.get('disabled_fg', None))
            kwargs_dict.setdefault('disabledbackground', self.STYLE_DEFAULTS.get('disabled_bg', None))
            kwargs_dict.setdefault('readonlybackground', self.STYLE_DEFAULTS.get('readonly_bg', None))

    # VARIABLES

    def BooleanVar(self, master=None, **kwargs):
        if master is None:
            master = self
        return tk.BooleanVar(master, **kwargs)

    def IntVar(self, master=None, **kwargs):
        if master is None:
            master = self
        return tk.IntVar(master, **kwargs)

    def DoubleVar(self, master=None, **kwargs):
        if master is None:
            master = self
        return tk.DoubleVar(master, **kwargs)

    def StringVar(self, master=None, **kwargs):
        if master is None:
            master = self
        return tk.StringVar(master, **kwargs)

    # WIDGETS

    def Toplevel(self, frame=None, title="Window Title", **kwargs):
        kwargs.setdefault('bg', self.STYLE_DEFAULTS['bg'])
        toplevel = tk.Toplevel(frame, **kwargs)
        toplevel.title(title)
        return toplevel

    @_embed_component
    def Notebook(self, frame=None, **kwargs):
        return ttk.Notebook(frame, **kwargs)

    @_embed_component
    def Frame(self, frame=None, **kwargs):
        self.set_style_defaults(kwargs)
        frame = tk.Frame(frame, **kwargs)
        return frame

    @_embed_component
    def Canvas(self, frame=None, **kwargs):
        self.set_style_defaults(kwargs)
        canvas = tk.Canvas(frame, **kwargs)
        return canvas

    @_embed_component
    def Button(self, command, frame=None, text=None, text_padx=None, text_pady=None,
               font_type=None, font_size=None, style=None, **kwargs):
        self.set_style_defaults(kwargs, text=True)
        if font_type is None:
            font_type = self.FONT_DEFAULTS['label_font_type']
        if font_size is None:
            font_size = self.FONT_DEFAULTS['label_font_size']
        if text is not None:
            text_var = tk.StringVar(value=text)
            self._variables.append(text_var)
        else:
            text_var = None
        if style is not None:
            button = ttk.Button(frame, command=command, textvariable=text_var, padx=text_padx, pady=text_pady,
                                style=style)
        else:
            button = tk.Button(frame, command=command, textvariable=text_var, padx=text_padx, pady=text_pady,
                               font=(font_type, font_size), **kwargs)
        button.var = text_var
        return button

    @_embed_component
    def Checkbutton(self, frame=None, command=None, initial_state=False, **kwargs):
        self.set_style_defaults(kwargs)
        boolean_var = tk.BooleanVar(value=initial_state)
        self._variables.append(boolean_var)
        checkbutton = tk.Checkbutton(frame, text='', variable=boolean_var, command=command, **kwargs)
        checkbutton.var = boolean_var
        return checkbutton

    @_embed_component
    def Combobox(self, frame=None, values=None, initial_value=None, readonly=True, width=20, on_select_function=None,
                 **kwargs):
        self.set_style_defaults(kwargs, text=True)
        state = 'readonly' if readonly else ''
        if initial_value is None:
            initial_value = values[0] if values else ''
        string_var = tk.StringVar(frame, value=initial_value)
        self._variables.append(string_var)
        combobox = ttk.Combobox(frame, textvariable=string_var, values=values, state=state, width=width)
        combobox.var = string_var
        if on_select_function is not None:
            combobox.bind('<<ComboboxSelected>>', on_select_function)
        return combobox

    @_embed_component
    def Entry(self, frame=None, initial_text='', integers_only=False, numbers_only=False, **kwargs):
        self.set_style_defaults(kwargs, text=True, cursor=True, entry=True)
        text_var = tk.StringVar(value=initial_text)
        self._variables.append(text_var)
        entry = tk.Entry(frame, textvariable=text_var, **kwargs)
        entry.var = text_var
        if integers_only:
            if numbers_only:
                raise ValueError("Use 'integers_only' or 'numbers_only', but not both.")
            v_cmd = (self.master.register(self._validate_entry_integers), '%P')
            entry.config(validate='key', validatecommand=v_cmd)
        elif numbers_only:
            v_cmd = (self.master.register(self._validate_entry_numbers), '%P', '%S')
            entry.config(validate='key', validatecommand=v_cmd)
        return entry

    @staticmethod
    def _validate_entry_integers(new_value):
        """ Callback invoked whenever the Entry contents change.

        Checks the new value of the Entry ('%P') is a valid integer.
        """
        return str.isdigit(new_value) or new_value == ""

    @staticmethod
    def _validate_entry_numbers(new_value, new_input):
        """ Callback invoked whenever the Entry contents change.

        Checks the new input ('%S') is an allowed symbol and ensures the new value of the Entry ('%P') can be
        interpreted as a float.
        """
        if new_value == "":
            return True
        if new_input not in '0123456789.+-':
            return False
        try:
            float(new_value)
        except ValueError:
            return False
        return True

    @_embed_component
    def Label(self, text='', frame=None, font_type=None, font_size=None, **kwargs):
        self.set_style_defaults(kwargs, text=True)
        if font_type is None:
            font_type = self.FONT_DEFAULTS['label_font_type']
        if font_size is None:
            font_size = self.FONT_DEFAULTS['label_font_size']
        if isinstance(text, str):
            string_var = tk.StringVar(value=text)
        elif isinstance(text, tk.StringVar):
            string_var = text
        else:
            raise ValueError("Text must be a string or StringVar.")
        self._variables.append(string_var)
        label = tk.Label(frame, textvariable=string_var, font=(font_type, font_size), **kwargs)
        label.var = string_var
        return label

    @_embed_component
    def Listbox(self, frame=None, values=(), on_select_function=None, **kwargs):
        self.set_style_defaults(kwargs, text=True)
        listbox = tk.Listbox(frame, **kwargs)
        for value in values:
            listbox.insert(END, value)
        if on_select_function is not None:
            listbox.bind('<<ListboxSelect>>', on_select_function)
        return listbox

    @_embed_component
    def Radiobutton(self, frame=None, command=None, variable=None, **kwargs):
        self.set_style_defaults(kwargs)
        if variable is None:
            variable = tk.IntVar()
        self._variables.append(variable)
        radiobutton = tk.Radiobutton(frame, text='', variable=variable, command=command, **kwargs)
        radiobutton.var = variable
        return radiobutton

    @_embed_component
    def Separator(self, frame=None, orientation=HORIZONTAL, **kwargs):
        self.set_style_defaults(kwargs)
        return ttk.Separator(frame, orient=orientation)

    @_embed_component
    def Text(self, frame=None, initial_text='', **kwargs):
        self.set_style_defaults(kwargs, text=True, cursor=True, entry=False)
        text = tk.Text(frame, **kwargs)
        text.insert(CURRENT, initial_text)
        return text

    @staticmethod
    def reset_canvas_scroll_region(canvas):
        """Sets scrollable canvas region to the entire bounding box."""
        canvas.configure(scrollregion=canvas.bbox("all"))

    @staticmethod
    def link_to_scrollable(scrollable_widget, *widgets):
        """Registers <Enter> and <Leave> events that enable the scrollbar for the second widget."""
        for widget in widgets:
            widget.bind('<Enter>', lambda _, f=scrollable_widget: _bind_to_mousewheel(_, f))
            widget.bind('<Leave>', lambda _, f=scrollable_widget: _unbind_to_mousewheel(_, f))

    @staticmethod
    def info_dialog(title, message, **kwargs):
        messagebox.showinfo(title, message, **kwargs)

    @staticmethod
    def warning_dialog(title, message, **kwargs):
        return messagebox.showwarning(title, message, **kwargs)

    @staticmethod
    def error_dialog(title, message, **kwargs):
        messagebox.showerror(title, message, **kwargs)

    @staticmethod
    def yesno_dialog(title, message, **kwargs):
        return messagebox.askyesno(title, message, **kwargs)

    def custom_dialog(self, title, message, font_size=None, font_type=None,
                      button_names=('OK',), button_kwargs=(), style_defaults=None,
                      default_output=None, cancel_output=None):
        if style_defaults is None:
            style_defaults = self.STYLE_DEFAULTS
        dialog = CustomDialog(master=self, title=title, message=message, font_size=font_size, font_type=font_type,
                              button_names=button_names, button_kwargs=button_kwargs, style_defaults=style_defaults,
                              default_output=default_output, cancel_output=cancel_output)
        return dialog.go()  # Returns index of button clicked (or default/cancel output).

    @contextmanager
    def set_master(self, master=None, auto_rows=None, auto_columns=None, grid_defaults=None, **kwargs):
        previous_frame = self.current_frame

        if master is None:
            self.current_frame = self.Frame(**kwargs)
        else:
            if isinstance(master, str):
                master = getattr(self, master)
            if master in {self.Frame, self.Toplevel, self.Notebook, self.Canvas}:
                self.current_frame = master(**kwargs)
            elif isinstance(master, (tk.Toplevel, ttk.Notebook, tk.Frame, tk.Canvas)):
                if kwargs:
                    raise ValueError("Cannot use keyword arguments when setting an existing master instance.")
                self.current_frame = master
            else:
                raise TypeError("Master can only be set to a Toplevel, Notebook, Frame, or Canvas.")

        previous_auto_row = self.current_row
        previous_auto_column = self.current_column
        self.current_row = auto_rows
        self.current_column = auto_columns

        if grid_defaults is not None:
            previous_grid_defaults = self.grid_defaults.copy()
            self.grid_defaults = grid_defaults
        else:
            previous_grid_defaults = {}

        yield self.current_frame

        self.current_row = previous_auto_row
        self.current_column = previous_auto_column
        if grid_defaults is not None:
            self.grid_defaults = previous_grid_defaults
        self.current_frame = previous_frame


class CustomDialog(BaseWindow):

    def __init__(self, master, title='Custom Dialog', message='', font_size=None, font_type=None,
                 button_names=(), button_kwargs=(), style_defaults=None,
                 default_output=None, cancel_output=None):
        if style_defaults:
            self.STYLE_DEFAULTS = style_defaults
        if isinstance(button_names, str):
            button_names = (button_names,)
        if isinstance(button_kwargs, dict):
            button_kwargs = (button_kwargs,)
        if button_kwargs and len(button_names) != len(button_kwargs):
            raise ValueError("Number of button_kwargs dicts (if any are given) must match number of buttons.")
        super().__init__(window_title=title, master=master)
        self.output = default_output
        self.cancel = cancel_output
        self.default = default_output
        self.bind('<Return>', self.return_event)

        with self.set_master(auto_rows=0, padx=20, pady=20):
            self.message = self.Label(text=message, font_size=font_size, font_type=font_type, pady=40)
            with self.set_master(auto_columns=0, pady=20):
                for i in range(len(button_names)):
                    button_text = button_names[i]
                    b_kwargs = button_kwargs[i] if button_kwargs else {}
                    b = self.Button(text=button_text, command=lambda s=self, output=i: s.done(output),
                                    padx=5, **b_kwargs)
                    if i == default_output:
                        b.config(relief=RIDGE)

        self.protocol('WM_DELETE_WINDOW', self.wm_delete_window)
        self.resizable(width=False, height=False)
        self.set_geometry(relative_position=(0.5, 0.3))

    def go(self):
        self.wait_visibility()
        self.grab_set()
        self.mainloop()
        self.destroy()
        return self.output

    def return_event(self, _):
        """ Event that occurs when the user presses the Enter key. """
        if self.default is None:
            self.bell()
        else:
            self.done(self.default)

    def wm_delete_window(self):
        """ Function that occurs when the user closes the window using the corner X, Alt-F4, etc. """
        if self.cancel is None:
            self.bell()
        else:
            self.done(self.cancel)

    def done(self, num):
        self.output = num
        self.quit()
