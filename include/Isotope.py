# Isotope - Stores information on desired isotope taken from masstable


class Isotope(object):
  def __init__(self, name, masstable={"H1": (1, 1.0)}):
    self.name = name
    self.mass = 0
    self.Z = 0
    self.valid = False
    self.masstable = masstable
    self.processName()


  def __str__(self):
    return "Isotope: {0.name} (Z = {0.Z}, mass = {0.mass} amu)".format(self)


  def processName(self):
    from re import findall
    iso = self.name.upper()
    # splits name into symbol and number
    isoList = findall("[A-Z]+|[0-9]+", iso)
    if len(isoList) == 2:
      self.createName(isoList)
    else:
      print("Isotope {0} not valid, defaulting to H1".format(self.name))
      self.changeName()
      self.processName()
    self.fillValues()


  def fillValues(self):
    if self.name in self.masstable:
      self.mass = self.masstable[self.name][1]
      self.Z = self.masstable[self.name][0]
      self.valid = True
    else:
      print("Isotope {0} not found in masstable".format(self.name))


  def changeName(self, newName="H1"):
    self.name = newName
    self.processName()


  def createName(self, isoList):
    if isoList[0].isdigit() and isoList[1].isalpha():
      number, symbol = isoList
    elif isoList[1].isdigit() and isoList[0].isalpha():
      symbol, number = isoList
    else:
      symbol, number = "H", "1"
    self.name = "{0}{1}".format(symbol, number)


  def getMass(self):
    return self.mass


  def getZ(self):
    return self.Z


  def getName(self):
    return self.name


if __name__ == "__main__":
  i = Isotope("H1")
  print(i)
