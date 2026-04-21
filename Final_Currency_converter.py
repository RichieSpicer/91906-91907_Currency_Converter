from tkinter import *
from functools import partial
import all_constants as c
import conversion_rounding as cr
from datetime import date


class Converter:
    """
    Currency conversion tool (NZD to USD or USD to NZD)
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        self.all_calculations_list = []

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

        # button list
        button_details_list = [
            ["To NZD", "#990099", lambda: self.check_currency("usd_to_nzd"), 0, 0],
            ["To USD", "#009900", lambda: self.check_currency("nzd_to_usd"), 0, 1],
            ["Help / Info", "#CC6600", self.to_help, 1, 0],
            ["History / Export", "#004C99", self.to_history, 1, 1]
        ]

        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        self.to_help_button = self.button_ref_list[2]

        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    def check_currency(self, conversion_type):
        """
        Checks input is valid and performs conversion
        """

        to_convert = self.currency_entry.get()

        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.currency_entry.config(bg="#FFFFFF")

        error = "Enter a valid number"
        has_errors = "no"

        try:
            to_convert = float(to_convert)
            self.convert(conversion_type, to_convert)
        except ValueError:
            has_errors = "yes"

        if has_errors == "yes":
            self.answer_error.config(text=error, fg="#9C0000")
            self.currency_entry.config(bg="#F4CCCC")
            self.currency_entry.delete(0, END)

    def convert(self, conversion_type, to_convert):
        """
        Converts currency and updates answer label
        """

        if conversion_type == "nzd_to_usd":
            answer = cr.nzd_to_usd(to_convert)
            answer_statement = f"${to_convert} NZD is ${answer} USD"
        else:
            answer = cr.usd_to_nzd(to_convert)
            answer_statement = f"${to_convert} USD is ${answer} NZD"

        self.to_history_button.config(state=NORMAL)

        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)

    def to_help(self):
        DisplayHelp(self)

    def to_history(self):
        """
        Opens history dialogue box and disables history button
        (so that users can't create multiple history boxes).
        """
        HistoryExport(self, self.all_calculations_list)


class DisplayHelp:

    def __init__(self, partner):
        background = "#ffe6cc"
        self.help_box = Toplevel()

        partner.to_help_button.config(state=DISABLED)

        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "Enter an amount and choose a conversion button.\n\n" \
                    "Use 'To USD' to convert NZD to USD.\n" \
                    "Use 'To NZD' to convert USD to NZD.\n\n" \
                    "Click History / Export to save your calculations."

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


def export_history(calculations):

    today = date.today()
    file_name = f"currency_{today}.txt"

    with open(file_name, 'w') as text_file:
        for item in calculations:
            text_file.write(item + "\n")


class HistoryExport:

    def __init__(self, partner, calculations):

        self.history_box = Toplevel()
        partner.to_history_button.config(state=DISABLED)

        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        if len(newest_first_list) <= c.MAX_CALCS:
            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"
            newest_first_string += newest_first_list[-1]
        else:
            for item in newest_first_list[:c.MAX_CALCS - 1]:
                newest_first_string += item + "\n"
            newest_first_string += newest_first_list[c.MAX_CALCS - 1]

        history_label = Label(self.history_box,
                              text=newest_first_string,
                              font=("Arial", "14"),
                              justify="left")
        history_label.grid(row=0)

        Button(self.history_box,
               text="Export",
               command=lambda: export_history(calculations)
               ).grid(row=1)

        Button(self.history_box,
               text="Close",
               command=partial(self.close_history, partner)
               ).grid(row=2)

    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()
