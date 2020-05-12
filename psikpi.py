temp = input("Input the  temperature you like to convert? (e.g., 1.2bar, 17.5psi etc.) : ")
degree = int(temp[:-3])
i_convention = temp[-1]

#i_convention.upper() == "i"
#print (i_convention)

#psi - bar convention
#if i_convention.upper() == "i":
#  result = int(round((9 * degree) / 5 + 32))
#  o_convention = "bar"
#bar - psi convention
#elif i_convention.upper() == "bar":
#  result = int(round((degree - 32) * 5 / 9))
#  o_convention = "psi"
#else:
#  print("Input proper convention.")
#  quit()
#print("The temperature in", o_convention, "is", result, "degrees.")
