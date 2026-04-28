from rich.console import Console
from rich.prompt import Prompt, Confirm
console = Console()


class data:
    
    def __init__(self):
        self.urls = []
    
    def get_url(self):
        while True:
            url  = Prompt.ask("Enter the urls : " )
            if url == 'Exit':
                confirmation = Confirm.ask("are you sure ? ")
                if(confirmation):
                    break
                else:
                    pass
            self.urls.append(url)
     
     
    def send_data(self):
        if not self.urls:
            self.get_url()
        return self.urls
