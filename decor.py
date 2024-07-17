class code:
  def __init__(self,location,corp):
    self.loc=location
    self.corp=corp
  def execute(self):
    print("my location is:",self.location)
    print("i work for:",self.corp)
    
  p1=code(kolkata,amazon)
  p1.execute()
