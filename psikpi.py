temp = input("Input from what you want to convert (1,2bar, 18,7psi) : ")
press1 = int(temp[:-3])
i_convention = temp[-1]

if i_convention() == "psi":
  result = int(round(degree * 0,0689)
  o_convention = "Bar"
elif i_convention.upper() == "bar":
  result = int(round(press1 * 14,5038)
  o_convention = "Psi"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")