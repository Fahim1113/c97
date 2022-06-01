variable = input('Enter your introduction: ')
characterCount = 0
wordCount = 1
sentenceCount = 1
vowelCount = 0

print(variable)

for i in variable:
  characterCount+=1
  if(i == ' '):
    wordCount+=1
  if(i == '.'):
    sentenceCount+=1
  if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
    vowelCount+=1
print('Character count: ',characterCount)
print('Word count: ',wordCount)
print('Sentence count: ',sentenceCount)
print('Vowel count: ',vowelCount)