from openai import OpenAI

class OpenAIService:
    client = OpenAI()

    def __init__(self):
        pass
    
    def generateImage(self, imageName):
        generateImage = self.client.images.generate(
        model="dall-e-3",
        prompt="A picture of a " + imageName + ".",
        n=1,
        size="1024x1024"
        )
        return generateImage.data[0].url
        

    def generateWords(self, motherLanguage, learningLanguage, wordCount, subjects):
        response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a language teacher which gives vocabularies and their translations to students. The response has to be a csv compatible list."},
            {"role": "user", "content": f"I want to learn {learningLanguage}. My mother language is {motherLanguage}. I want to learn {wordCount} words for following subjects {subjects}."}
        ]
        )
        return response.choices[0].message.content