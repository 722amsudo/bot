temp = input("Input the  temperature you like to convert? (e.g., 1.2bar, 17.5psi etc.) : ")
degree = float(temp[:-3])
i_convention = temp[-1]

#i_convention.upper() == "i"
#print (i_convention)

#print (degree)

#psi - bar convention
if i_convention.upper() == "I":
  result = int(round(degree * 0.0689))
  o_convention = "bar"
#bar - psi convention
elif i_convention.upper() == "R":
  result = int(round(degree * 14))
  o_convention = "psi"
else:
  print("Input proper convention.")
  quit()
print("The pressure in", o_convention, "is", result, o_convention)
