import gradio as gr
from dotenv import load_dotenv
from deep_researcher import DeepResearcher

load_dotenv(override=True)

async def execute(user_input: str):
    async for data_chunk in DeepResearcher().run(user_input):
        yield data_chunk


with gr.Blocks(theme=gr.themes.Default(primary_hue="blue")) as app_ui:
    gr.Markdown("# Advanced Research Tool")
    
    input_box = gr.Textbox(label="Enter a topic to explore")
    start_btn = gr.Button("Start", variant="primary")
    
    output_display = gr.Markdown(label="Generated Report")
    
    start_btn.click(fn=execute, inputs=input_box, outputs=output_display)
    input_box.submit(fn=execute, inputs=input_box, outputs=output_display)

app_ui.launch(inbrowser=True)