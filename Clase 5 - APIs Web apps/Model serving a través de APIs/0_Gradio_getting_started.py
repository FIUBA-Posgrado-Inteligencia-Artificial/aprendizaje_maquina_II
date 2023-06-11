import gradio as gr

def greet(name):
    return "Hello " + name + ", welcome to the AMq2 course!"

demo = gr.Interface(fn = greet, inputs = gr.Textbox(lines = 2, placeholder = "Name here..."),
                    outputs = "text")

demo.launch()
