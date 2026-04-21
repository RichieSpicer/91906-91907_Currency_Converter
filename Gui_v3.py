from tkinter import *
import all_constants as c


class Converter:
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
        self.answer_error = Label(self.currency_frame, text=error,
                                  fg="#9C0000", font=("Arial", "14", "bold"))
        self.answer_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.currency_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg colour | command | row | column)
        button_details_list = [
            ["To NZD", "#990099", lambda: self.check_currency("usd_to_nzd"), 0, 0],
            ["To USD", "#009900", lambda: self.check_currency("nzd_to_usd"), 0, 1],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        # List to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)

    def check_currency(self, conversion_type):
        """
        Checks input is valid and either invokes calculation
        function or shows a custom error
        """

        # Retrieve amount to be converted
        to_convert = self.currency_entry.get()

        # Reset label and entry box (if we have error)
        self.answer_error.config(fg="#004C99")
        self.currency_entry.config(bg="#FFFFFF")

        # checks that amount to be converted is a valid number
        try:
            to_convert = float(to_convert)
            error = ""
            self.convert(conversion_type)
        except ValueError:
            error = "Please enter a number!"

        # display error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.currency_entry.config(bg="#F4CCCC")
            self.currency_entry.delete(0, END)

    def convert(self, conversion_type):

        if conversion_type == "nzd_to_usd":
            self.answer_error.config(text="Converting to USD")
        else:
            self.answer_error.config(text="Converting to NZD")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()
