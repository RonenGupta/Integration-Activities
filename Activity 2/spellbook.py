import pandas as pd
import matplotlib.pyplot as plt

# Create an empty DataFrame with specific columns to store spell details
spell_df = pd.DataFrame(columns=['Name', 'Level', 'Index', 'URL'])

# Define a function to display spell information in a readable format
def display_spell(spell_data):
    print(f"Name: {spell_data['name']}")
    print(f"Level: {spell_data['level']}")
    print(f"Index: {spell_data['index']}")
    print(f"URL: {spell_data['url']}")
    print()  

# Define a function to store the selected spell into the DataFrame
def store_spell(spell_data):
    spell_df.loc[len(spell_df)] = {'Name': spell_data['name'], 
                                   'Level': spell_data['level'], 
                                   'Index': spell_data['index'], 
                                   'URL': spell_data['url']}

# Define a function to display all the spells stored so far
def display_stored():
    print('The following are the spells you have searched for so far.')
    spell_df.sort_values(by=['Name', 'Level'], inplace=True) # Sort the DataFrame by spell name and level for easy viewing
    print(spell_df)

# Define a function to visualize the levels of the stored spells
def visualise_level():
    try:
        print('Here is a visual representation of your spell levels: ')
        spell_df.sort_values(by=['Level', 'Name'], inplace=True)  # Sort the DataFrame by level and name to organize the plot

        # Create a bar chart with spell names on the x-axis and levels on the y-axis
        spell_df.plot(
            kind='bar',
            x='Name',
            y='Level',
            color='blue',
            alpha=0.3,
            title='Level of Spells'
        )

        plt.show() #Display the plot
    
    # Catch any error that occurs (such as an empty DataFrame)
    except:
        print('Oops! You need to prepare some spells first!')