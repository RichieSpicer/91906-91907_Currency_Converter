from datetime import date

calculations = ['$10.00 NZD is $5.90 USD', '$20.00 NZD is $11.80 USD',
                '$30.00 NZD is $17.70 USD', '$40.00 NZD is $23.60 USD',
                '$50.00 NZD is $29.50 USD']

# ***** Get current date for heading and filename ****
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

file_name = f"currency_{day}_{month}_{year}"
write_to = f"{file_name}.txt"

with open(write_to, 'w') as text_file:

    text_file.write("***** Currency Calculations *****\n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write(f"Here is your calculation history (oldest to newest)... \n")

    # write the item to file
    for item in calculations:
        text_file.write(item)
        text_file.write("\n")
