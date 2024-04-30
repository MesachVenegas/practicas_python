from tkinter import Menu, Tk, ttk
from operations import Calculator as cal
from logger import log
import tkinter as tk
import sys

class InfoApp(Tk):
    default_msn = '''Calculadora Creada para practicar el uso del modulo tkinter de python.
E implementando el uso de la Programación Orientada a Objetos.

        Version: 1.1.0
        Python Version : 3.10
        Made With \u2665 & Tkinter
        \u00A9 2021-2022 Mesach Venegas'''

    def __init__(self, mensaje:str = None):
        """InfoAPP 
        Permite generar una ventana con un mensaje con información sobre la aplicación, con
        un mensaje predefinido.

        Args:
            mensaje (str, optional): Mensaje a mostrar en pantalla. Defaults to None.
        """
        super().__init__()
        icon = r'C:\Users\mesas\OneDrive\Calculadora\Calculator.ico'
        self._mensaje = mensaje
        self.geometry("550x250+400+300")
        self.title("Acerca de Calculadora")
        self.iconbitmap("Calculator.ico")
        self.resizable(0, 0)
        self.check()
        self.info_win()

    @property
    def mensaje(self):
        return self._mensaje

    @mensaje.setter
    def mensaje(self, new_mensaje:str):
        self._mensaje = new_mensaje

    def check(self):
        if self.mensaje == None:
            self.mensaje = InfoApp.default_msn

    def info_win(self):
        logo = tk.PhotoImage(master=self, file=r"C:\Users\mesas\OneDrive\Calculadora\python_logo.png")
        logo_label = ttk.Button(self, image=logo, command= lambda: logo.cget('file'))
        content = ttk.Label(self, font=16, text=self.mensaje, justify=tk.CENTER)
        logo_label.grid(row=0, column=0, pady=3)
        content.grid(row=1, column=0, padx=20)

class Calculadora(Tk):
    def __init__(self):
        super().__init__()
        # Windows Layout
        icon = r'C:\Users\mesas\OneDrive\Calculadora\Calculator.ico'
        self.geometry("300x400+500+150")
        self.resizable(0,0)
        self.title("Calculadora")
        self.iconbitmap(icon)
        # Lineas
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, weight=2)
        self.rowconfigure(5, weight=2)
        # Columnas
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=3)
        self._display_calculator()
        self._main_menu()

    def _display_calculator(self):
        # Botonera
        self.display = tk.Entry(self, justify=tk.RIGHT, font=('Fira Code',26, 'bold'))
        num_1 = ttk.Button(self, text="7", command=lambda: self.display.insert(tk.END, "7"))
        num_2 = ttk.Button(self, text="8", command=lambda: self.display.insert(tk.END, "8"))
        num_3 = ttk.Button(self, text="9", command=lambda: self.display.insert(tk.END, "9"))
        num_4 = ttk.Button(self, text="4", command=lambda: self.display.insert(tk.END, "4"))
        num_5 = ttk.Button(self, text="5", command=lambda: self.display.insert(tk.END, "5"))
        num_6 = ttk.Button(self, text="6", command=lambda: self.display.insert(tk.END, "6"))
        num_7 = ttk.Button(self, text="1", command=lambda: self.display.insert(tk.END, "1"))
        num_8 = ttk.Button(self, text="2", command=lambda: self.display.insert(tk.END, "2"))
        num_9 = ttk.Button(self, text="3", command=lambda: self.display.insert(tk.END, "3"))
        num_0 = ttk.Button(self, text="0", command=lambda: self.display.insert(tk.END, "0"))
        punto = ttk.Button(self, text=".", command=lambda: self.display.insert(tk.END, "."))

        # Botonera Operaciones
        ac = tk.Button(self, text="AC", command=lambda: self.display.delete(0, tk.END))
        raiz = ttk.Button(self, text="\u221A", command=lambda: self.display.insert(0, "\u221A"))
        multi = ttk.Button(self, text="x", command=lambda: self.display.insert(tk.END, "x"))
        div = ttk.Button(self, text="\u00F7", command=lambda: self.display.insert(tk.END, "\u00F7"))
        suma = ttk.Button(self, text="+", command=lambda: self.display.insert(tk.END, "+"))
        resta = ttk.Button(self, text="-", command=lambda: self.display.insert(tk.END, "-"))
        igual = tk.Button(self, text="=", command=self._resultados)

        # Configuración de botones especiales.
        ac.config(bg="skyblue", relief=tk.GROOVE, font='bold')
        igual.config(bg="skyblue", relief=tk.GROOVE, font='bold')

        # Deploy Grid
        self.display.grid(row=0, column=0, sticky="NSEW", columnspan=4)
        ac.grid(row=1, column=0, sticky="NSEW")
        raiz.grid(row=1, column=1, sticky="NSEW")
        div.grid(row=1, column=2, sticky="NSEW")
        multi.grid(row=1, column=3, sticky="NSEW")
        num_1.grid(row=2, column=0, sticky="NSEW")
        num_2.grid(row=2, column=1, sticky="NSEW")
        resta.grid(row=2, column=3, sticky="NSEW")
        num_3.grid(row=2, column=2, sticky="NSEW")
        num_4.grid(row=3, column=0, sticky="NSEW")
        num_5.grid(row=3, column=1, sticky="NSEW")
        num_6.grid(row=3, column=2, sticky="NSEW")
        suma.grid(row=3, column=3, sticky="NSEW")
        num_7.grid(row=4, column=0, sticky="NSEW")
        num_8.grid(row=4, column=1, sticky="NSEW")
        num_9.grid(row=4, column=2, sticky="NSEW")
        igual.grid(row=4, column=3, sticky="NSEW", rowspan=2)
        num_0.grid(row=5, column=0, sticky="NSEW", columnspan=2)
        punto.grid(row=5, column=2, sticky="NSEW")

    # -------------------- Menu funciones  --------------------#
    def _info_app(self):
        info = InfoApp()
        info.mainloop()

    def _main_menu(self):
        menu_principal = Menu()
        sub_archivo = Menu(menu_principal, tearoff=0)
        sub_edit = Menu(menu_principal, tearoff=0)
        sub_info = Menu(menu_principal, tearoff=0)
        sub_archivo.add_command(label="Salir", command=lambda: sys.exit())
        sub_edit.add_command(
            label="Borrar", command=lambda: self.display.delete(0, tk.END)
        )
        sub_edit.add_command(
            label="Seleccionar",
            command=lambda: (
                self.display.select_range(0, tk.END),
                self.display.focus(),
            ),
        )
        sub_info.add_command(label="Sobre Calculadora...", command=self._info_app)
        menu_principal.add_cascade(menu=sub_archivo, label="Archivo")
        menu_principal.add_cascade(menu=sub_edit, label="Editar")
        menu_principal.add_cascade(menu=sub_info, label="Acerca de")
        self.config(menu=menu_principal)

    # ----------------------- Lectura de datos y Funcionalidad ---------------------------------#
    def _leer_dat(self):
        data = self.display.get()
        operation = cal.checking(data)
        valor = str(cal.operaciones(operation))
        return valor

    def _resultados(self):
        rest = self._leer_dat()
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, rest)


if __name__ == "__main__":
    try:
        calculadora = Calculadora()
        calculadora.mainloop()
    except Exception as ex:
        log.error(ex)