import gradio as gr
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_text(prompt, temperature=1.0, max_length=100, top_k=50):
    inputs = tokenizer.encode(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(inputs, max_length=max_length, temperature=temperature, top_k=top_k, do_sample=True)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

# Create Gradio interface
demo = gr.Interface(fn=generate_text, 
                    inputs=["text", gr.Slider(0, 2, 0.1, label="Temperature"), 
                            gr.Slider(50, 500, 1, label="Max Length"),
                            gr.Slider(1, 100, 1, label="Top-k Sampling")],
                    outputs="text")

# Launch the interface
demo.launch(share=True)
