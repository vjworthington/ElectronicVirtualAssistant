################################
# Electronic Virtual Assistant #
#        also known as         #
#            E V A             #
################################

from openai import OpenAI
from tkinter import *

client = OpenAI()

# Your API: enter command below into terminal
# to set your OpenAI API key
#export OPENAI_API_KEY="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"

# Create EVA
def EVA(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
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

# Sample Text Message
#msg = Message(frame1, text="Long text to see how it's justified",
#    font=("helvetica", 12),
#    aspect=150,)
#msg.pack(pady=10, padx=10)

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