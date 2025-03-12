import ipywidgets as widgets
from IPython.display import display
import pandas as pd
import teradataml as tdml

def display_dataframes_in_tabs(table_names):
    # Temporarily set pandas display options to ensure all columns are visible
    with pd.option_context('display.max_columns', None):
        # Create a list to hold each tab's contents and their titles
        tab_contents = []
        tab_titles = table_names
        
        for table_name in table_names:
            # Get the first ten rows of the DataFrame
            df_head = tdml.DataFrame(table_name)
            table_output = widgets.Output()  # Create an output widget for the table
            with table_output:
                display(df_head)  # Display the DataFrame inside the output widget
            tab_contents.append(table_output)  # Add to tab contents list

        # Create the tabs widget
        tabs = widgets.Tab(children=tab_contents)
        
        # Set tab titles
        for i, title in enumerate(tab_titles):
            tabs.set_title(i, title)

        # Display the tabs
        display(tabs)