from datetime import datetime

class Business:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.date_added = datetime.now()

    def display_info(self):
        return f"{self.name} - {self.category} (Added on {self.date_added.strftime('%Y-%m-%d %H:%M:%S')})"


class BusinessDirectory:
    def __init__(self):
        self.businesses = []
        self.recently_added = []  # Stack (LIFO)

    def add_business(self, business):
        self.businesses.append(business)
        self.recently_added.append(business)

    def get_recent(self):
        return self.recently_added[-5:]