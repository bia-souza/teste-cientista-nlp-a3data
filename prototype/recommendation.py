import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class Recommender:
    def __init__(self, dataframe):
        self.df = dataframe

    def filter_complaints(self):
        """
        Retorna as linhas do dataframe onde o campo 'Número de Reclamações' é maior que 0,
        categorizado por 'Tipo de serviço'.
        """
        filtered_data = self.df[self.df['Número de Reclamações'] > 0]
        return filtered_data

    def generate_text(self, categoria):
        prompt = "Me dê soluções para resolver o problema de churn em contratos de {categoria}"
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
        model = GPT2LMHeadModel.from_pretrained("gpt2-medium")

        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(input_ids, max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text
