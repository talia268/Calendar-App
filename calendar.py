import datetime

class Calendar:
    def __init__(self):
        self.events = {}
    
    def add_event(self, date, event):
        if date in self.events:
            self.events[date].append(event)
        else:
            self.events[date] = [event]
    
    def view_events(self, date):
        if date in self.events:
            print(f"Events for {date}:")
            for event in self.events[date]:
                print(event)
        else:
            print(f"No events on {date}")
    
    def delete_event(self, date, event):
        if date in self.events and event in self.events[date]:
            self.events[date].remove(event)
        else:
            print("Event not found")
    
    def view_month(self, year, month):
        start_date = datetime.date(year, month, 1)
        end_date = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
        for date in (start_date + datetime.timedelta(n) for n in range(int((end_date - start_date).days)+1)):
            if date in self.events:
                print(f"{date.strftime('%d %B %Y')}:")
                for event in self.events[date]:
                    print(f"\t- {event}")
            else:
                print(date.strftime('%d %B %Y'))
