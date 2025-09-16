from member import member
class StaffMember(member):

   def __init__(self, name, staff_id, add_book):
    self.name=name
    self.staff_id=staff_id
    self.add_book=add_book

   def add_book(self):
            if self.staff_id ==111 :
                 print("allowed to add books to library")