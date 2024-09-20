import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json
import random

# Global variables to track the dataset and which entries have been used
dataset = None
dataset_size = 0
used_indices = set()
current_entry = None
yes_count = 0
cfprompt_response = ""

# Global variables for UI elements
prompts_header = None
prompt_labels = []
follow_up_header = None
cfprompt_label = None
yes_button = None
no_button = None
root = None

def load_json_data(filepath):
    """
    Load JSON data from a specified filepath.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {filepath}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def save_json_data(filepath, data):
    """
    Save JSON data to a specified filepath.
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def start_evaluation():
    """
    Begins the evaluation stage and calls all UI functions
    """
    global dataset, current_entry, yes_count, root, dataset_size
    prompts = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]
    cfprompt = StringVar()

    # Debug to ensure dataset is loaded and evaluated properly
    print(f"Dataset size: {dataset_size}")
    if not dataset:
        print("Dataset is empty.")
        messagebox.showinfo("Info", "Dataset is empty.")
        return

    # Filter for entries without a 'human_score' field
    unattempted_entries = [entry for entry in dataset if 'human_score' not in entry]

    if not unattempted_entries:
        print("All entries have been used or answered.")  # For debugging
        messagebox.showinfo("Info", "All entries have been used or answered.")
        return

    # Selecting a non-repeating random entry from the filtered dataset
    current_entry = random.choice(unattempted_entries)

    # Setup UI and initialize first entry
    setup_ui(prompts, cfprompt)
    for i, prompt in enumerate(current_entry['prompts']):
        prompts[i].set(prompt)
        if i != 0:
            prompt_labels[i].pack_forget()
    cfprompt.set(current_entry['cfprompt'])

    dataset_size-=1


def reset():
    global prompts_header, prompt_labels, follow_up_header, cfprompt_label, yes_button, no_button, used_indices, current_entry, yes_count, cfprompt_response
    
    # Calculate the final score and cfprompt response before reinitialization
    human_score = (yes_count + 1)/5
    human_cf = cfprompt_response

    # Update the current entry with human_score and human_cf
    if current_entry is not None:
        current_entry['human_score'] = human_score
        current_entry['human_cf'] = human_cf

    # Save the updated dataset back to the JSON file
    save_json_data("test.json", dataset)

    # Clear the screen
    for widget in root.winfo_children():
        widget.destroy()

    # Reinitialize global variables
    current_entry = None
    yes_count = 0
    cfprompt_response = ""
    prompt_labels = []  # It's important to reset this list so old references are not kept

    # Re-setup the UI and reinitialize the evaluation
    start_evaluation()


def cfprompt_evaluation():
    global yes_button, no_button
    yes_button.config(command=lambda: yes_onClick_alt())
    no_button.config(command=lambda: no_onClick_alt())

    follow_up_header.pack()
    cfprompt_label.pack()

def yes_onClick_alt():
    global cfprompt_response
    cfprompt_response = "yes"
    reset()

def no_onClick_alt():
    global cfprompt_response
    cfprompt_response = "no"
    reset()  

def yes_onClick():
    global yes_count
    if yes_count < len(prompt_labels) - 1:
        yes_count += 1
        prompt_labels[yes_count].pack()
    elif yes_count == len(prompt_labels) - 1:
        cfprompt_evaluation()

def no_onClick():
    cfprompt_evaluation()

def setup_ui(prompts, cfprompt):
    global prompts_header, prompt_labels, follow_up_header, cfprompt_label, yes_button, no_button, root

    # Create the header for prompts
    prompts_header = tk.Label(root, text="Prompts", font=("Arial", 24))
    prompts_header.pack(pady=(10, 0))

    # Create text boxes for prompts
    prompt_labels = []
    for i in range(5):  # Assuming 5 prompts
        text_box = tk.Label(root, textvariable=prompts[i], font=("Arial", 11), height=3, width=75, wraplength=600)
        text_box.pack(pady=5)
        prompt_labels.append(text_box)

    # Create the header for follow-up
    follow_up_header = tk.Label(root, text="Follow-up", font=("Arial", 24))
    follow_up_header.pack_forget()

    # Create text box for cfprompt
    cfprompt_label = tk.Label(follow_up_header, textvariable=cfprompt, font=("Arial", 11), height=3, width=75, wraplength=600)
    cfprompt_label.pack(side=BOTTOM,pady=60)

    # Create a frame for Yes/No buttons
    button_field = tk.Frame(root)
    button_field.pack(side=BOTTOM,pady=(20, 10))

    # Create Yes and No buttons within the frame
    yes_button = tk.Button(button_field, text="Yes", height=1, width=6, font=("Arial", 15), bg="#ADE6D8", fg="#004A00", command=lambda: yes_onClick())
    no_button = tk.Button(button_field, text="No", height=1, width=6, font=("Arial", 15), bg="#E6ADD8", fg="#6B0000", command=lambda: no_onClick())
    yes_button.pack(side=tk.LEFT, padx=10)
    no_button.pack(side=tk.RIGHT, padx=10)

def main():
    # Load the JSON dataset
    filepath = "test.json"
    global dataset, root, dataset_size
    dataset = load_json_data(filepath)
    if dataset is None:
        print("Error loading dataset. Exiting program.")
        return
    dataset_size = len(dataset)

    # Initialize the Tkinter window
    root = tk.Tk()
    root.title("Cultural Sensitivity Evaluation")
    start_evaluation()

    # Set the window size
    root.geometry("900x600")

    # Run the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
