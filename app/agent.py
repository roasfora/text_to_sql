from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("tscholak/1zha5ono")
model = T5ForConditionalGeneration.from_pretrained("tscholak/1zha5ono")

def text_to_sql(question: str, schema_prompt: str) -> str:
    input_text = f"{question} | {schema_prompt}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=256)
    sql = tokenizer.decode(output[0], skip_special_tokens=True)
    return sql.split("|")[-1].strip()
