def form(username, password, fullname = "not set", age = 0):
  print(username, password, fullname, age)

form("abolfazlalz", "1234")
form("ftmwt", "1234", "Fatima Torkamani")
form("armin", "1234", "Armin Hoseininejhad", 21)
form("aida", "1234", age=21)
form("arian", "1234", fullname="Arian Ghodrati")