import gradio as gr
import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from technical_content_writer.main import ContentGeneraterFlow, ContentState

generator_flow = ContentGeneraterFlow()

def generate_content_gradio(topic, audience_level):
    # Set up state
    state = ContentState(topic=topic, audience_level=audience_level)
    # Run the flow steps manually
    state = generator_flow.generate_content(state)
    # Process the content
    content = generator_flow.serve_content(state)
    return content

# Using the stream_content method directly from the flow
def generate_content_streaming(topic, audience_level):
    # Set up state
    state = ContentState(topic=topic, audience_level=audience_level)
    # Run the flow and get streaming content
    state = generator_flow.generate_content(state)
    # Return a generator that yields strings, not the generator object directly
    for chunk in generator_flow.stream_content(state, delay=0.2):
        yield chunk

# Create a simpler Gradio interface
with gr.Blocks(title="Technical Content Writer") as demo:
    gr.Markdown("# Technical Content Writer")
    gr.Markdown("Generate technical content by specifying a topic and audience level.")
    
    with gr.Tab("Regular Generation"):
        with gr.Row():
            with gr.Column(scale=1):
                topic_input = gr.Textbox(label="Topic")
                audience_level = gr.Radio(
                    choices=["beginner", "intermediate", "advanced"], 
                    label="Audience Level",
                    value="intermediate"  # Default value
                )
                generate_btn = gr.Button("Generate Content")
            
            with gr.Column(scale=2):
                gr.Markdown("## Generated Content")
                output = gr.Markdown("*Content will appear here after generation*")
        
        generate_btn.click(
            fn=generate_content_gradio,
            inputs=[topic_input, audience_level],
            outputs=output
        )
    
    with gr.Tab("Streaming Generation"):
        with gr.Row():
            with gr.Column(scale=1):
                topic_input_stream = gr.Textbox(label="Topic")
                audience_level_stream = gr.Radio(
                    choices=["beginner", "intermediate", "advanced"], 
                    label="Audience Level",
                    value="intermediate"  # Default value
                )
                generate_stream_btn = gr.Button("Generate Content (Streaming)")
            
            with gr.Column(scale=2):
                gr.Markdown("## Generated Content (Streaming)")
                output_stream = gr.Markdown("*Content will appear here as it's generated*")
        
        generate_stream_btn.click(
            fn=generate_content_streaming,
            inputs=[topic_input_stream, audience_level_stream],
            outputs=output_stream
        )

if __name__ == "__main__":
    demo.launch()