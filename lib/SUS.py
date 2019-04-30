class Rang_sus(object):
    def __init__(self, note):
      self.note = note
      if self.note > 84.0:
          self.rang = "A+"
          self.percentile = "96%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "darkgreen"
      elif self.note > 80.7:
          self.rang = "A"
          self.percentile = "90%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "green"
      elif self.note > 78.8:
          self.rang = "A-"
          self.percentile = "85%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "blue"
      elif self.note > 77.1:
          self.rang = "B+"
          self.percentile = "80%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "blue"
      elif self.note > 74.0:
          self.rang = "B"
          self.percentile = "70%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "blue"
      elif self.note > 72.5:
          self.rang = "B-"
          self.percentile = "65%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "blue"      
      elif self.note > 71.0:
          self.rang = "C+"
          self.percentile = "60%"
          self.color = "blue"
          self.comment = "L'utilisabilité perçue est supérieur à {} des systèmes évalués ".format(self.percentile)
      elif self.note > 64.9:
          self.rang = "C"
          self.percentile = "41%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "orange"
      elif self.note > 62.6:
          self.rang = "C-"
          self.percentile = "35%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "blue"
      elif self.note > 51.6:
          self.rang = "D"
          self.percentile = "15%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "blue"
      else:
          self.rang = "F"
          self.percentile = "14%"
          self.comment = "L'utilisabilité perçue est inférieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "blue"

class New_rang_sus(object):
  def __init__(self,Rang_sus):
      self.note = float(Rang_sus)
      if self.note > 84.0:
          self.rang = "A+"
          self.percentile = "96%"
          self.comment = "The perceived usability of this system is better than {} of systems ".format(self.percentile)
      elif self.note > 80.7:
          self.rang = "A"
          self.percentile = "90%"
          self.comment = "The perceived usability of this system is better than {} of systems ".format(self.percentile)
      elif self.note > 78.8:
          self.rang = "A-"
          self.percentile = "85%"
          self.comment = "The perceived usability of this system is better than {} of systems ".format(self.percentile)
      elif self.note > 77.1:
          self.rang = "B+"
          self.percentile = "80%"
          self.comment = "The perceived usability of this system is better than {} of systems ".format(self.percentile)
      elif self.note > 74.0:
          self.rang = "B"
          self.percentile = "70%"
          self.comment = "The perceived usability of this system is better than {} of systems ".format(self.percentile)
      elif self.note > 72.5:
          self.rang = "B-"
          self.percentile = "65%"
          self.comment = "The perceived usability of this system is better than {} of systems ".format(self.percentile)
      elif self.note > 71.0:
          self.rang = "C+"
          self.percentile = "60%"
          self.comment = "The perceived usability of this system is better than {} of systems ".format(self.percentile)
      elif self.note > 64.9:
          self.rang = "C"
          self.percentile = "41%"
          self.comment = "The perceived usability of this system is better than {} of systems ".format(self.percentile)
      elif self.note > 62.6:
          self.rang = "C-"
          self.percentile = "35%"
          self.comment = "The perceived usability of this system is better than {} of systems ".format(self.percentile)
      elif self.note > 51.6:
          self.rang = "D"
          self.percentile = "15%"
          self.comment = "The perceived usability of this system is better than {} of systems ".format(self.percentile)
      else:
          self.rang = "F"
          self.percentile = "14%"
          self.comment = "The perceived usability of this system is worse than {} of systems ".format(self.percentile)


def inv():
  x = input("Avant que vous ne renseignez les scores moyens de vos items... \n Avez-vous inversé les scores des items impaires ? (o/n) : ")
  if x == "o":
    return True
  if x == "n":
    return False

class Item(object):
      def __init__(self,number, item):
          self.number = number
          self.item = item
          if self.number % 2 == 1:
              self.note = float(input("Note à l'item n°{} : ".format(self.number)))
              self.inv = False
          else:
              self.inv= True
              if usr_inv == False:
                self.note =float(input("Note à l'item n°{} (Brute) : ".format(self.number)))
              elif usr_inv == True:
                self.note =float(input("Note à l'item n°{} (Note brute inversée) : ".format(self.number)))
                self.note = 6 - self.note

          
      def predict(self,SUS,usr_inv):
          self.SUS = SUS
          self.usr_inv = usr_inv
          if self.number == 1:
              self.prdt_SUS = round((self.note - 1.073927)/0.034024,2)
              self.prdt_note = round(1.073927 + 0.034024*self.SUS,2)
          if self.number == 2:
              self.prdt_SUS = round((5.834913 - self.note)/0.04980485, 2)
              self.prdt_note = round(5.834913 - 0.04980485*self.SUS,2)
          if self.number == 3:
              self.prdt_SUS = round((self.note - 0.4421485)/0.04753406, 2)
              self.prdt_note = round(0.4421485 + 0.04753406*self.SUS,2)
          if self.number == 4:
              self.prdt_SUS = round((3.766087 - self.note)/0.02816776, 2)          
              self.prdt_note = round(3.766087 - 0.02816776*self.SUS,2)
          if self.number == 5:
              self.prdt_SUS = round((self.note - 1.18663)/0.03470129, 2)
              self.prdt_note = round(1.18663 + 0.03470129*self.SUS,2)
          if self.number == 6:
              self.prdt_SUS = round((4.589912 - self.note)/0.03519522, 2)
              self.prdt_note = round(4.589912 - 0.03519522*self.SUS,2)              
          if self.number == 7:
              self.prdt_SUS = round((self.note - 0.9706981)/0.04027653, 2)
              self.prdt_note = round(0.9706981 + 0.04027653*self.SUS,2)
          if self.number == 8:
              self.prdt_SUS = round((5.575382 - self.note)/0.04896754, 2)
              self.prdt_note = round(5.575382 - 0.04896754*self.SUS,2)
          if self.number == 9:
              self.prdt_SUS = round((self.note - 0.6992487)/0.04435754, 2)
              self.prdt_note = round(0.6992487 + 0.04435754*self.SUS,2)
          if self.number == 10:
              self.prdt_SUS = round((4.603949 - self.note )/0.03692307, 2)
              self.prdt_note = round(4.603949 - 0.03692307*self.SUS,2)

def eval_odd(note,note_predite,noteSUS,prdtSUS):
      new_rank = New_rang_sus(prdtSUS)
      if note > note_predite:
        print(Fore.GREEN + "Votre systeme est mieux perçu sur cet item !")
        print(Fore.WHITE + "\n +{} que la moyenne des systèmes ayant le même score SUS ({})".format(round(note-note_predite,2),round(noteSUS,2)))
        if new_rank.rang == "F":
            print("La note a cet item correspond à un system noté colored({}) ({}, < {})".format(prdtSUS,new_rank.rang,new_rank.percentile))
        else:
            print("La note a cet item correspond à un system noté colored({}) ({}, > {})".format(prdtSUS, new_rank.rang,
                                                                                                new_rank.percentile))
      elif note < note_predite:
        print(Fore.RED +"Votre system est moins bien perçu sur cet item...")
        print(Fore.WHITE + "\n {} que la moyenne des systèmes ayant le même score SUS ({})".format(round(note-note_predite,2),round(noteSUS,2)))
        if new_rank.rang == "F":
            print("La note a cet item correspond à un system noté colored({}) ({}, < {})".format(prdtSUS,new_rank.rang,new_rank.percentile))
        else:
            print("La note a cet item correspond à un system noté {} ({}, > {})".format(prdtSUS,new_rank.rang,new_rank.percentile))
      else:
        print("La note est dans la moyenne")
        return note - note_predite

def eval_even(note,note_predite,noteSUS,prdtSUS):
  new_rank = New_rang_sus(prdtSUS)
  if note > note_predite:
    print(Fore.RED +"Votre system est moins bien perçu sur cet item...")
    print(Fore.WHITE + " \n +{} que la moyenne des systèmes ayant le même score SUS ({})".format(round(note-note_predite,2),round(noteSUS,2)))
    if new_rank.rang == "F":
        print("La note a cet item correspond à un system noté colored({}) ({}, < {})".format(prdtSUS, new_rank.rang,
                                                                                            new_rank.percentile))
    else:
        print("La note a cet item correspond à un system noté {} ({}, > {})".format(prdtSUS,new_rank.rang,new_rank.percentile))
    print("C'est un item inversé. Une différence posiive montre une moins bonne utilisabilité perçue.")
  elif note < note_predite:
    print(Fore.GREEN + "Votre systeme est mieux perçu sur cet item !")
    print(Fore.WHITE + "\n {} que la moyenne des systèmes ayant le même score SUS ({})".format(round(note-note_predite,2),round(noteSUS,2)))
    if new_rank.rang == "F":
        print("La note a cet item correspond à un system noté colored({}) ({}, < {})".format(prdtSUS, new_rank.rang,
                                                                                            new_rank.percentile))
    else:
        print("La note a cet item correspond à un system noté {} ({}, > {})".format(prdtSUS,new_rank.rang,new_rank.percentile))
    print("C'est un item inversé. Une différence négative montre une meilleure utilisabilité perçue.")
  else:
    print("La note est dans la moyenne")
    return note - note_predite
    

#note_sus = Rang_sus()
#print("\n Note : {} \n {} \n".format(note_sus.rang,note_sus.comment))
#usr_inv = inv()
#item1 = Item(1,"I think that I would like to use this system frequently")
#item2 = Item(2,"I found the system unnecessarily complex")
#item3 = Item(3,"I thought the system was easy to use")
#item4 = Item(4,"I think that I would need the support of a technical person to be able to use this system")
#item5 = Item(5,"I found the various functions in this system were well integrated")
#item6 = Item(6,"I thought there was too much inconsistency in this system")
#item7 = Item(7,"I would imagine that most people would learn to use thissystem very quickly")
#item8 = Item(8,"I found the system very awkward to use")
#item9 = Item(9,"I felt very confident using the system")
#item10 = Item(10,"I needed to learn a lot of things before I could get going with this system")


#lst_items = [item1,item2,item3,item4,item5,item6,item7,item8,item9,item10]

#for i in lst_items:
#      print('\n \n ___________\n')
#      print("****** Item n°{} : {} \n ".format(i.number,i.item))
#      i.predict(note_sus.note,usr_inv)
#      if i.number %2 == 1:
#        eval_odd(i.note,i.prdt_note,i.SUS,i.prdt_SUS)
#      else:
#        eval_even(i.note,i.prdt_note,i.SUS,i.prdt_SUS)

