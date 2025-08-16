# Import necessary libraries:
import requests  # For making HTTP requests to get data from an API
from spellbook import display_spell, store_spell, display_stored, visualise_level

# Define the main function that will run the program
def main():
    url = "https://www.dnd5eapi.co/api/spells" # Set the API endpoint URL for fetching D&D 5e spell data
    headers = {'Accept': 'application/json'} # Set headers for the API request

    response = requests.get(url, headers=headers) # Send a GET request to the API to retrieve the spell data

    # Check if the request was successful (status code 200 means OK)
    if response.status_code == 200:
        spells_data = response.json() # Parse the response data as JSON
        spells = spells_data['results'] # Extract the list of spells from the data
        print("Welcome to the D&D 5e Spellbook!")
        print(f"Total Spells: {spells_data['count']}\n")

        # Start an infinite loop to prompt the user for input
        while True:
            print("Commands:")
            print("1 - List all spells")  
            print("2 - Search for a spell by name")  
            print("3 - Display stored spells")  
            print("4 - Visualise Spells")  
            print("5 - Exit")

            # Prompt the user to input their choice
            choice = input("Enter your choice: ")

            # If the user chooses to list all spells
            if choice == '1':
                print("\nList of Spells:")
                # Iterate over all spells and display their details
                for spell in spells:
                    display_spell(spell)
            
            # If the user wants to search for a spell by name
            elif choice == '2':
                spell_name = input("Enter the spell name: ").lower() # Ask the user for a spell name (case-insensitive)
                matching_spells = [spell for spell in spells if spell_name in spell['name'].lower()] # Find all spells that contain the entered name
                print("\nMatching Spells:")

                # Display details of each matching spell
                for spell in matching_spells:
                    display_spell(spell)
                    choice = input('Would you like to prepare the spell? Y/N: ') # Ask the user if they want to store the spell
                    
                    if choice.lower() == 'y':
                        store_spell(spell)
                        print('Spell prepared.')
                    
                    elif choice.lower() == 'n':
                        print('Spell not prepared.')

                    else:
                        print('Invalid option. Spell not stored.')
            
            # If the user wants to display the stored spells
            elif choice == '3':
                display_stored()
            
            # If the user wants to visualize the spell levels
            elif choice == '4':
                visualise_level()
            
            # If the user wants to exit the program
            elif choice == '5':
                print("Goodbye!")
                break  # Exit the loop and end the program
            
            # If the user enters an invalid option
            else:
                print("Invalid choice. Please select a valid option.")

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    main()