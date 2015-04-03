# Isotope - Stores information on desired isotope taken from masstable


class Isotope(object):
  def __init__(self, name, masstable=None):
    self.name = name
    self.mass = 0
    self.Z = 0
    self.masstable = masstable
    self.processName()


  def __str__(self):
    return "Isotope: {0.name} (Z = {0.Z}, mass = {0.mass} amu)".format(self)


  def processName(self):
    self.adjustNameforTable()
    if self.checkNameInTable():
      self.fillValuesFromTable()


  def adjustNameForTable(self):
    from re import findall
    iso = self.name.upper()
    isoNameSplit = join(findall("[A-Z]+|[0-9]+", iso))
    self.createName(isoNameSplit)


  def createName(self, isoList):
    if isoList[0].isdigit() and isoList[1].isalpha():
      number, symbol = isoList
    elif isoList[1].isdigit() and isoList[0].isalpha():
      symbol, number = isoList
    self.name = "{0}{1}".format(symbol, number)


  def checkNameInTable(self):
    return self.name in self.masstable


  def fillValuesFromTable(self):
    self.mass = self.masstable[self.name][1]
    self.Z = self.masstable[self.name][0]


  def getMass(self):
    return self.mass


  def getZ(self):
    return self.Z


  def getName(self):
    return self.name
