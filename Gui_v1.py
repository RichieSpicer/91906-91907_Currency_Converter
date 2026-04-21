from tkinter import *


class Converter():
    """
    Currency conversion tool (NZD to USD or USD to NZD)
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.currency_heading = Label(self.currency_frame,
                                      text="Currency Converter",
                                      font=("Arial", "16", "bold")
                                      )
        self.currency_heading.grid(row=0)

        instructions = "Please enter a price below and then press " \
                       "one of the buttons to convert it from NZD " \
                       "to USD or USD to NZD"
        self.currency_instructions = Label(self.currency_frame,
                                           text=instructions,
                                           wraplength=250, width=40,
                                           justify="left")
        self.currency_instructions.grid(row=1)

        self.currency_entry = Entry(self.currency_frame,
                                    font=("Arial", "14")
                                    )
        self.currency_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.currency_error = Label(self.currency_frame, text=error,
                                    fg="#9C0000")
        self.currency_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.currency_frame)
        self.button_frame.grid(row=4)

        self.to_nzd_button = Button(self.button_frame,
                                    text="To NZD",
                                    bg="#990099",
                                    fg="#ffffff",
                                    font=("Arial", "12", "bold"), width=12)
        self.to_nzd_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_usd_button = Button(self.button_frame,
                                    text="To USD",
                                    bg="#009900",
                                    fg="#ffffff",
                                    font=("Arial", "12", "bold"), width=12)
        self.to_usd_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_button = Button(self.button_frame,
                                  text="Help / Info",
                                  bg="#CC6600",
                                  fg="#ffffff",
                                  font=("Arial", "12", "bold"), width=12)
        self.help_button.grid(row=1, column=0, padx=5, pady=5)

        self.history_button = Button(self.button_frame,
                                     text="History / Export",
                                     bg="#004C99",
                                     fg="#ffffff",
                                     font=("Arial", "12", "bold"), width=12)
        self.history_button.grid(row=1, column=1, padx=5, pady=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()
