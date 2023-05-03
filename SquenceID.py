import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.core.window import Window
from kivy.resources import resource_add_path
from kivy.uix.image import Image


Window.clearcolor = (0,0,0,5)
Window.size = (800,400)
# Add the path of the font folder
resource_add_path('fonts')

# Define the layout of the app
class DNASequenceLayout(GridLayout):

    def __init__(self, **kwargs):
        super(DNASequenceLayout, self).__init__(**kwargs)
        
        # Set the number of columns for the layout
        self.cols = 1

        # Add a label for the input field
        self.add_widget(Label(text="Enter a genetic sequence:"))

        # Add a text input field for the user to input the DNA/RNA sequence
        self.dna_input = TextInput(multiline=False, on_text_validate=self.on_enter)
        self.add_widget(self.dna_input)

        # Add a button to generate the result
        self.result_button = Button(text="Go!")
        self.result_button.bind(on_press=self.generate_result)
        self.add_widget(self.result_button)

        # Add a label to display the result
        self.result_label = Label(text="", font_size="16sp")
        self.add_widget(self.result_label)

    def on_enter(self, instance):
        self.generate_result(None)

    def generate_result(self, instance):
        # Get the user's input DNA/RNA sequence
        sequence = self.dna_input.text

        # Convert the sequence to uppercase if it's in lowercase
        sequence = sequence.upper()

        # Check if the sequence is DNA or RNA
        if 'U' in sequence:
            sequence_type = 'RNA'
        else:
            sequence_type = 'DNA'

        # Check if the sequence is valid
        if set(sequence) - set("ATCGU") != set():
            # If the sequence contains invalid characters, display an error message
            self.result_label.text = "Please enter a valid DNA/RNA sequence"
        else:
            # If the sequence is valid, display information about it
            length = len(sequence)
            gc_count = sequence.count('G') + sequence.count('C')
            gc_ratio = gc_count / length
            first_base_pair = sequence[0]
            last_base_pair = sequence[-1]
            info = f"Results: \nThis is a {sequence_type} sequence with a length of {length} base pair, its GC ratio is {gc_ratio:.2f}.\n The 1st bp is {first_base_pair} & last one is {last_base_pair}. :)"
            self.result_label.text = info

class DNASequenceApp(App):

    def build(self):
        # Set the title of the app
        self.title = "Genetic Sequence Identifier"
        img = Image(
            source = 'D:\\dna.jpg',
            size_hint = (1,1)
        )
        # Create the layout for the app
        layout = DNASequenceLayout()

        return layout

# Run the app
if __name__ == "__main__":
    DNASequenceApp().run()
