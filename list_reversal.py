all_calculations = ['$10.00 NZD is $5.90 USD', '$20.00 NZD is $11.80 USD',
                    '$30.00 NZD is $17.70 USD', '$40.00 NZD is $23.60 USD',
                    '$50.00 NZD is $29.50 USD', '$60.00 NZD is $35.40 USD']

newest_first = list(reversed(all_calculations))

print("==== Oldest to Newest for File ====")
for item in all_calculations:
    print(item)

print()

print("==== Most Recent First ===")
for item in newest_first:
    print(item)
