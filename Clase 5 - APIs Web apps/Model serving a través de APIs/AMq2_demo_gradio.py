from Model import IrisModel
import gradio as gr

model = IrisModel()

# Defino sliders para controlar las features de entrada
sepal_length = gr.inputs.Slider(minimum=0, maximum=10, default=5, label='sepal_length')
sepal_width = gr.inputs.Slider(minimum=0, maximum=10, default=5, label='sepal_width')
petal_length = gr.inputs.Slider(minimum=0, maximum=10, default=5, label='petal_length')
petal_width = gr.inputs.Slider(minimum=0, maximum=10, default=5, label='petal_width')

gr.Interface(model.predict_species_to_gradio, 
             inputs=[sepal_length, sepal_width, petal_length, petal_width], 
             outputs='label',
             title='Predictions:',
             capture_session=True,
             live=True).launch()