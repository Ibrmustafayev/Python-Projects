import json
import requests
from datetime import *

class Session:
    def __init__(self, duration, note):
        self.duration = duration
        self.note = note
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {"duration": self.duration, "note": self.note, "date": self.date}

class Subject:
    def __init__(self, name):
        self.name = name
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def to_dict(self):
        return {"name": self.name, "sessions": [s.to_dict() for s in self.sessions]}
    
class Tracker:
    def __init__(self):
        self.subjects = {}
        self.load()

    def load(self):
        try:
            with open("sessions.json", "r") as f:
                data = json.load(f)
                for subject_data in data:
                    subject = Subject(subject_data["name"])
                    for session_data in subject_data["sessions"]:
                        s = Session(session_data["duration"], session_data["note"])
                        s.date = session_data["date"]  # restore saved date instead of generating new one
                        subject.add_session(s)
                    self.subjects[subject.name] = subject
        except:
            self.subjects = {}

    def save(self):
        with open("sessions.json", "w") as f:
            json.dump([s.to_dict() for s in self.subjects.values()], f, indent=4)
        
    def add_session(self, subject_name, duration, note):
        if subject_name not in self.subjects:
            self.subjects[subject_name] = Subject(subject_name)
        self.subjects[subject_name].add_session(Session(duration, note))
        self.save()

    def view_all_sessions(self):
        for subject in self.subjects.values():
            print(f"\n{subject.name}")
            for session in subject.sessions:
                print(f"\t{session.date} | {session.duration} min | {session.note}")

    def view_stats_per_subject(self):
        for subject in self.subjects.values():
            total_time_per_subject = 0
            for session in subject.sessions:
                total_time_per_subject += session.duration
            print(f"{subject.name}\t[Total time: {total_time_per_subject} min | Session count: {len(subject.sessions)} | Average: {total_time_per_subject / len(subject.sessions) if subject.sessions else 0} min]")

    def view_overall_summary(self):
        if not self.subjects:
            print("No data yet.")
            return
        else:
            total_times = []
            for subject in self.subjects.values():
                total_time_per_subject = 0
                for session in subject.sessions:
                    total_time_per_subject += session.duration
                total_times.append(total_time_per_subject)
            print(f"Total time for all subjects: {sum(total_times)}\nMost studied subject: {list(self.subjects.values())[total_times.index(max(total_times))].name} ({max(total_times)} min)")   

    def get_quote(self):
        try:
            response = requests.get("https://zenquotes.io/api/random")
            data = response.json()
            print(f"\n\"{data[0]['q']}\"\n— {data[0]['a']}\n")
        except requests.exceptions.ConnectionError:
            print("No internet connection.")

def main():
    tracker = Tracker()
    while True:
        print("\n=== Study Session Tracker ===")
        print("1. Add a study session")
        print("2. View all sessions")
        print("3. View stats per subject")
        print("4. View overall summary")
        print("5. Get a motivational quote on startup")
        print("6. Exit")
        choice = input("\nChoice: ")
        if choice == "6":
            print("\nGoodbye!!!")
            break
        elif choice == "1":
            subject = input("\nSubject: ")
            try:
                duration = int(input("Duration in minutes: "))
            except ValueError:
                print("Error: invalid value!")
                continue
            note = input("Note: ")
            tracker.add_session(subject, duration, note)
        elif choice == "2":
            tracker.view_all_sessions()
        elif choice == "3":
            tracker.view_stats_per_subject()
        elif choice == "4":
            tracker.view_overall_summary()
        elif choice == "5":
            tracker.get_quote()
        else:
            print("Error: invalid choice option!")

main()