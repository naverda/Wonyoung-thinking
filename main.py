import os
import google.generativeai as genai

genai.configure(api_key='AIzaSyCyuumlJbq6cQ36Ln5ZPKtENeDoCdsdGic')

model = genai.GenerativeModel(model_name="gemini-pro")


def make_novel(text):
    response = model.generate_content(
        f"Wonyoung thinking is an internet meme and buzzword derived from the super-positive mindset of Jang Won-young, a member of the girl group IVE. The key is the firm optimism that 'the goddess of luck is on my side.' Simply put, the belief is that everything that happens to me is good after all. The expression 'Lucky Vicky' and 'Lucky' is a combination of Jang Won-young's English names, Vicky, and 'Lucky', which emphasizes the good fortune of Wonyoung thinking. For example, if you have to do Wonyoung thinking when there is only half of the water left, it's too much to eat all, too little to eat less. So I thought it would be nice to have only half, but it's totally Lucky Vicky, that's Wonyoung thinking. Please describe {text} as Wonyoung thinking. The answer should start with Wonyoung Thinking: Please write about 2 sentences. And at the end, you have to end with a realiy luckybikiy. You must only think positive thoughts."
    )
    return response.text


text = input("Enter story(Only one sentence, english): ")
print()
novel = make_novel(text)
print(novel)
