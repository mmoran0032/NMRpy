# Isotope - Stores information on desired isotope taken from masstable


class Isotope(object):
  """
  From desired isotope name (XXX### or similar), we get values for the
  charge state and mass of that isotope from our desired mass table
  dictionary. Name is checked before we try to get the information
  """
  def __init__(self, name, masstable={"H1": (1, 1)}):
    """
    Creates the isotope. masstable defaults to dummy Hydrogen-1 if no table
    provided to make sure we have some information after starting.
    """
    self.name = name
    self.mass = 0.0
    self.Z = 0
    self.reformatName()
    self.fillValues(masstable)


  def reformatName(self):
    from re import findall
    iso = self.name.upper()
    # splits name into symbol and number
    isoList = findall("[A-Z]+|[0-9]+", iso)
    if len(isoList) == 2:
      if isoList[0].isdigit() and isoList[1].isalpha():
        num, sym = isoList
        self.name = self._createName(sym, num)
      elif isoList[1].isdigit() and isoList[0].isalpha():
        sym, num = isoList
        self.name = self._createName(sym, num)
    else:
      print("Isotope {0} not valid, defaulting to H1".format(self.name))
      self.changeName()


  def fillValues(self, masstable):
    """
    Takes values from preprocessed masstable (dictionary) and saves them.
    Requires to already have checked and reformated the isotope.
    """
    if self.name in masstable:
      self.mass = masstable[self.name][1]
      self.Z = masstable[self.name][0]
    else:
      print("Isotope {0} not found in masstable".format(self.name))


  def changeName(self, newName="H1"):
    self.name = newName
    self.reformatName()


  def _createName(self, symbol, number):
    return "{0}{1}".format(symbol, number)


def main():
  # Testing with different isotope names
  i = Isotope("he4")
  i.changeName("97ZR")
  i.changeName("INVALID-NAME-1")
  i.changeName("12-C")


if __name__ == "__main__":
  main()
