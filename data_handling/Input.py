from exception import *
from data_handling.config import VALIDMAILIST
class Input:
    
    def __init__(self, name, contact, Email) -> None:
        self.name = name
        self.contact = contact
        self.Email = Email
        
    @property
    def contact(self):
            return self._contact
    @contact.setter
    def contact(self, value):
        if value.isdigit():
            if len(value) == 10:
                self._contact = value
            else:
                raise InvalidContactLength(f"The length of the contact is Invalid : length = {len(value)}")
        else:
            raise InvalidContactFormat("Contact must be in digits.")
        
    @property
    def Email(self):
        return self._Email
    @Email.setter
    def Email(self, Email):
        if '@' in Email:
            parts = Email.split('@')
            if(len(parts) == 2):
                if parts[0] and parts[1]:
                    if(parts[1] in VALIDMAILIST):
                        self._Email = Email
                    else:
                        raise InvalidEmailExtension(f"The Mail has an Invalid extension  {parts[1]}")
                else:
                    raise InvalidEmailFormat("Email can't have a empty local or domain part")
            else:
                raise InvalidEmailFormat("Email must have a local-part and domain part")
        else:
            raise InvalidEmailFormat("No @ in Email.")
