from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-", "^"]
        self.last_was_operator = None
        self.last_button = None
        self.result = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        layout.add_widget(self.result)

        button_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.6))

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "C", "+"
        ]

        for button_text in buttons:
            button = Button(
                text=button_text,
                background_color=(0.2, 0.7, 0.7, 1),  # Turquoise button color
            )
            button.bind(on_press=self.on_button_press)
            button_layout.add_widget(button)

        equals_button = Button(
            text="=",
            background_color=(0.7, 0.2, 0.2, 1),  # Red button color
        )
        equals_button.bind(on_press=self.on_solution)
        button_layout.add_widget(equals_button)

        layout.add_widget(button_layout)

        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == "C":
            self.result.text = ""
        else:
            new_text = current + button_text
            self.result.text = new_text

    def on_solution(self, instance):
        text = self.result.text
        try:
            # Replace "^" with "**" for exponentiation
            text = text.replace("^", "**")
            answer = str(eval(text))
            self.result.text = answer
        except ZeroDivisionError:
            self.result.text = "Cannot divide by zero"
        except Exception as e:
            self.result.text = "Error"

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
