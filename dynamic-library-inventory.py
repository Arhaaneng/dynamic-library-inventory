maktaba_inventory=["Sealed nector","kitab al tawheed","bulugh al maram"]
print("INITIAL LIBRARY:",maktaba_inventory)
new_book= input("stories of prophets:")

maktaba_inventory.append(new_book)
print("\nUPDATED LIBRARY:")
print(maktaba_inventory)

maktaba_inventory.remove("Sealed nector")

print("\n FINAL INVENTORY:")
print(maktaba_inventory)

print("\nBook sucessfully lent to your friend!")
