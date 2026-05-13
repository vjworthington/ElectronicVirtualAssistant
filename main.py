################################
# Electronic Virtual Assistant #
#        also known as         #
#            E V A             #
################################

from openai import OpenAI
from tkinter import *

# OLD - client = OpenAI()
# read API key from file
try:
    with open("config.txt", "r") as file:
        api_key = file.read().strip()

    client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
    )

except FileNotFoundError:
    print("config.txt not found")
    exit()

except Exception as e:
    print("Error loading API key:", e)
    exit()

# Your API: enter command below into terminal
# to set your OpenAI API key
# NEW OPENROUTER.AI KEY
# export OPENAI_API_KEY="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"

# Create EVA
def EVA(prompt):
    try:
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-super-120b-a12b:free",
            messages=[
                {"role": "system", "content": "Helpful AI"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"An error occured: {str(e)}")
        return "Error. Please try again."
    
# Tkinter Text Bubbles
root = Tk()
root.title("EVA")
root.geometry("900x400")

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="Avatar", width=65)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="Chat", bg="#363636", height=20)
m2.add(top)

bottom = Label(m2, text="User Input", bg="white")
m2.add(bottom)

root.mainloop()

# Main function
if __name__ == "__main__":
    while True:
        #User input
        user_input = input ("Ask something >> ")

        if user_input.lower() in ["bye", "quit", "exit"]:
            break

        response = EVA(user_input)
        # EVA output
        print("EVA >> ", response)

###########
# ENJOY!! #
###########