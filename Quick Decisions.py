attendees = int(input( "Enter number of attendees: "))       # Convert input to integer
venue = "large hall" if attendees > 100 else "conference room"   #Proper use of short-hand if-else
print(venue)

equipment = "projector" if attendees > 50 else "audio system"   # Short hand if-else usage
print(f"Recommended equipment: {equipment}")

vegeterian = input("Do you want vegetarian food? (yes/no):").lower    # User input and convert it to lower case
caterer = "Veggie Delight Caterers" if vegeterian == "yes" else "Gourmet Meal Caterers"  # Shorthand if-else usage
print(f"Recommeded caterer: {caterer}")