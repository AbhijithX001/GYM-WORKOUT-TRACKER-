class GymManagementSystem:

    def __init__(self):
        self.members = {}
        self.workouts = {}

    def welcome_message(self):
        print("HEYY BUDDIES! 💪🔥 ---Muscles grow and excuses DIE!")

    def add_member(self, member_id, name):
        print(f"So you’ve decided to change your life, {name}? Bold move!")
        self.members[member_id] = name
        self.workouts[member_id] = []
        print(f"Member {name} added! Now no skipping workouts!")
        print("WELCOME TO THE CLUB! 🏋️")

    def remove_member(self, member_id):
        if member_id in self.members:
            print(f"Oh, leaving already? {self.members[member_id]} removed! Hope your BED is comfy!")
            del self.members[member_id]
            del self.workouts[member_id]
        else:
            print("Nice try, but that member doesn’t even exist!")

    def view_members(self):
        if not self.members:
            print("No members found. Just an empty gym, huh?")
        else:
            print("\nGym Members:")
            for member_id, name in self.members.items():
                print(f"ID: {member_id}, Name: {name}")

    def record_workout(self, member_id):
        if member_id not in self.workouts:
            print("Member not found! Maybe they ran away from leg day?")
            return

        muscle_group = input("\nWhich muscles are you training today? 🏋️‍♂️: ")
        print(f"Oh, {muscle_group}? Finally! Let’s do this right!")
        print("\n✅ Maintain proper form\n✅ Stay hydrated\n✅ Warm up before lifting\n✅ Don’t forget cool-down stretches")

        start_workout = input("\nShall I start? (yes/no): ")
        
        if start_workout.lower() == 'yes':
            print("\n🔥 NISSAARAM! LET'S GO! 🔥")
            activity = input("\nEnter Workout Activity: ")
            duration = input("Enter Duration (mins): ")
            self.workouts[member_id].append((activity, duration))
            print("\nWorkout recorded! Keep pushing! 💪")
        else:
            print("\nSkipping today? Fine, but don’t blame me when your gains disappear!")

    def view_workout_history(self, member_id):
        if member_id in self.workouts and self.workouts[member_id]:
            print(f"\nWorkout History for {self.members[member_id]}:")
            for activity, duration in self.workouts[member_id]:
                print(f"Activity: {activity}, Duration: {duration} mins")
        else:
            print("\nNO RECORDS, Looks like someone prefers couch workouts over gym workouts!")


def main():
    gym = GymManagementSystem()
    gym.welcome_message()
    
    while True:
        print("\n1. Add Member\n")
        print("2. Remove Member\n")
        print("3. View Members\n")
        print("4. Record Workout\n")
        print("5. View Workout History\n")
        print("6. Exit\n")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            gym.add_member(input("\nID: "), input("Name: "))
        
        elif choice == '2':
            gym.remove_member(input("\nID: "))
        
        elif choice == '3':
            gym.view_members()
        
        elif choice == '4':
            gym.record_workout(input("\nMember ID: "))
        
        elif choice == '5':
            gym.view_workout_history(input("\nMember ID: "))
        
        elif choice == '6':
            print("\nAlright. See you next time....")
            break
        
        else:
            print("\nThat wasn’t even an option....")


if __name__ == "__main__":
    main()
