class Rang_sus(object):
    def __init__(self, note):
      self.note = note
      if self.note > 84.0:
          self.rang = "A+"
          self.percentile = "96%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "#0D6600"
      elif self.note > 80.7:
          self.rang = "A"
          self.percentile = "90%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "#378206"
      elif self.note > 78.8:
          self.rang = "A-"
          self.percentile = "85%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "#6C9E10"
      elif self.note > 77.1:
          self.rang = "B+"
          self.percentile = "80%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "#C8C224"
      elif self.note > 74.0:
          self.rang = "B"
          self.percentile = "70%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "#E4B135"
      elif self.note > 72.5:
          self.rang = "B-"
          self.percentile = "65%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "#F2A63E"      
      elif self.note > 71.0:
          self.rang = "C+"
          self.percentile = "60%"
          self.color = "#FFC100"
          self.comment = "L'utilisabilité perçue est supérieur à {} des systèmes évalués ".format(self.percentile)
      elif self.note > 64.9:
          self.rang = "C"
          self.percentile = "41%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "#F58632"
      elif self.note > 62.6:
          self.rang = "C-"
          self.percentile = "35%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "#F76126"
      elif self.note > 51.6:
          self.rang = "D"
          self.percentile = "15%"
          self.comment = "L'utilisabilité perçue est supérieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "#FA3819"
      else:
          self.rang = "F"
          self.percentile = "14%"
          self.comment = "L'utilisabilité perçue est inférieure à {} des systèmes évalués ".format(self.percentile)
          self.color = "#FF0028"



class Item(object):
      def __init__(self,note, number, SUS, rangSUS, inv):
          self.number = number
          self.note = note
          self.SUS = SUS
          self.rangSUS = rangSUS
          self.inv = inv
          if self.inv == True:
            self.note = 6 - self.note

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
          if self.prdt_SUS > 99:
              self.prdt_SUS = 100
          if self.prdt_SUS < 5:
              self.prdt_SUS = 5

          new_rank = Rang_sus(self.prdt_SUS)
          if self.number % 2 == 1:
              if self.note > self.prdt_note:
                  self.commentitem = "Votre systeme est mieux perçu sur cet item ! \n + {} que la moyenne des systèmes ayant le même score SUS ({})".format(round(self.note-self.prdt_note,2),round(self.SUS,2))
                  if new_rank.rang == "F":
                      self.precision = "La note a cet item correspond à un system noté {} (<b><span style='color:{}'>{}</span></b>, < {})".format(self.prdt_SUS,new_rank.color,new_rank.rang,new_rank.percentile)
                  else:
                      self.precision = "La note a cet item correspond à un system noté {} (<b><span style='color:{}'>{}</span></b>, > {})".format(self.prdt_SUS,new_rank.color, new_rank.rang,new_rank.percentile)
              elif self.note < self.prdt_note:
                  self.commentitem = "Votre system est moins bien perçu sur cet item... \n {} que la moyenne des systèmes ayant le même score SUS ({})".format(round(self.note-self.prdt_note,2),round(self.SUS,2))
                  if new_rank.rang == "F":
                      self.precision = "La note a cet item correspond à un system noté {} (<b><span style='color:{}'>{}</span></b>, < {})".format(self.prdt_SUS,new_rank.color,new_rank.rang,new_rank.percentile)
                  else:
                      self.precision = "La note a cet item correspond à un system noté {} (<b><span style='color:{}'>{}</span></b>, > {})".format(self.prdt_SUS,new_rank.color,new_rank.rang,new_rank.percentile)
              else:
                  self.commentitem = "La note est dans la moyenne"


          if self.number % 2 == 0:
              if self.note > self.prdt_note:
                self.commentitem = "Votre system est moins bien perçu sur cet item... \n +{} que la moyenne des systèmes ayant le même score SUS ({})".format(round(self.note-self.prdt_note,2),round(self.SUS,2))
                if new_rank.rang == "F":
                    self.precision = "La note a cet item correspond à un system noté {} (<b><span style='color:{}'>{}</span></b>, < {}) C'est un item inversé. Une différence positive montre une moins bonne utilisabilité perçue.".format(self.prdt_SUS,new_rank.color, new_rank.rang,new_rank.percentile)
                else:
                    self.precision = "La note a cet item correspond à un system noté {} (<b><span style='color:{}'>{}</span></b>, > {}) C'est un item inversé. Une différence positive montre une moins bonne utilisabilité perçue.".format(self.prdt_SUS,new_rank.color, new_rank.rang,new_rank.percentile)
              elif self.note < self.prdt_note:
                self.commentitem = "Votre systeme est mieux perçu sur cet item ! \n {} que la moyenne des systèmes ayant le même score SUS ({})".format(round(self.note-self.prdt_note,2),round(self.SUS,2))
                if new_rank.rang == "F":
                    self.precision = "La note a cet item correspond à un system noté {} (<b><span style='color:{}'>{}</span></b>, < {}) \n \n C'est un item inversé. Une différence négative montre une meilleure utilisabilité perçue.".format(self.prdt_SUS,new_rank.color, new_rank.rang,new_rank.percentile)
                else:
                    self.precision = "La note a cet item correspond à un system noté {} (<b><span style='color:{}'>{}</span></b>, > {}) \n \n C'est un item inversé. Une différence négative montre une meilleure utilisabilité perçue.".format(self.prdt_SUS,new_rank.color, new_rank.rang,new_rank.percentile)
              else:
                self.commentitem = "La note est dans la moyenne"
 

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

