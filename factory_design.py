class StudentIDCard:
    def issue_card(self):
        print("Student id card issued")
        
class FacultyIDCard:
    def issue_card(self):
        print("Faculty ID card issued")

class StaffIDCard:
    def issue_card(self):
        print("Staff id card issued")
        
class IDCardFactory:
    def get_card(self, card_type):
        
        if card_type=="student":
            return StudentIDCard()
        
        elif card_type=="faculty":
            return FacultyIDCard()
        
        elif card_type=="staff":
            return StaffIDCard()
        
        else:
            print("Invalid card type")
            return None

factory= IDCardFactory()     

card= factory.get_card("student")   
card.issue_card()

card= factory.get_card("faculty")
card.issue_card()

card= factory.get_card("staff")
card.issue_card()

        