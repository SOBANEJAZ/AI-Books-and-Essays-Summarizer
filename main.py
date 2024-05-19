# Large Text Summary and key notes maker program
import openai
import PyPDF2
import docx
import os
# import time

# Set up your OpenAI API credentialsimport os
my_secret = os.environ['openaiapikey']
API_KEY = my_secret
openai.api_key = API_KEY
# my_secret = os.environ['openaiapikey']
# openai.api_key = my_secret

# docx / pdf / txt

#please note now the pdf/docx/txt files could be added in filpath

file_path = 'userinput.txt'


# This function extracts text from a pdf
def extract_text_from_pdf(file_path):
  with open(file_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
      text += page.extract_text()
    return text


# This function extracts text from a document file
def extract_text_from_docx(file_path):
  doc = docx.Document(file_path)
  text = ''
  for paragraph in doc.paragraphs:
    text += paragraph.text
  return text


# This function extracts text from a .txt file
def extract_text_from_txt(file_path):
  with open(file_path, 'r') as file:
    text = file.read()
  return text


# This function detects the file format
def extract_text(file_path):
  if file_path.endswith('.pdf'):
    return extract_text_from_pdf(file_path)
  elif file_path.endswith('.docx'):
    return extract_text_from_docx(file_path)
  elif file_path.endswith('.txt'):
    return extract_text_from_txt(file_path)
  else:
    print('Unsupported file format')
    return ''


ex_text = extract_text(file_path)
print(ex_text)  # Prints the text given by the user


# Step 1 and Step 2
def process_text(text):
  """This is the step 2 which summaries the chunks of text"""
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role":
      "user",
      "content":
      """Can you please create a short and meaningfull summary for the following text: """
      + text + """
Please ensure that the accuracy is accurate and captures the intended meaning.

Good luck!!"""
    }])
  print("723 words analyzed.....")
  return completion.choices[0].message.content.strip()


# Step 1: This chunks the actual text into words of around 700 limit
def text_chunker(text):
  words = text.split()
  processed_text = ''
  for i in range(0, len(words), 723):
    chunk = ' '.join(words[i:i + 723])
    response = process_text(chunk, )
    # time.sleep(18)
    processed_text += response.strip() + ' '
  return processed_text.strip()


chunked_summary = text_chunker(text=ex_text)
print(chunked_summary)

### Step 3: Joins all the chunked summaries and puts in a file in folder

# Extract the file name without the extension
file_name = os.path.splitext(file_path)[0]
# Create a folder with the same name as the file
folder_name = file_name
os.makedirs(folder_name, exist_ok=True)

# Create text file inside the folder
file1_path = os.path.join(folder_name, 'chunked_summary.txt')

# You can write content to these files if needed
with open(file1_path, 'w') as file1:
  file1.write(chunked_summary)


# step 4: Creates the final summary from the chunked summary
def process_text_result_summary(text):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role":
      "user",
      "content":
      """Please summarize the following text such that the meaning that is intended is accurate and pressurize more on the main theme of the text and also take things orderwise. the summary should be longer than 10 to 15 lines."""
      + f"{file_name}/chunked_summary.txt" + """Good luck!!"""
    }])
  print("723 words analyzed.....")
  return completion.choices[0].message.content.strip()


def generate_result_summary(text):
  words = text.split()
  processed_text = ''
  for i in range(0, len(words), 723):
    chunk = ' '.join(words[i:i + 723])
    response = process_text_result_summary(chunk, )
    # time.sleep(18)
    processed_text += response.strip() + ' '
  return processed_text.strip()


final_summary = generate_result_summary(
  text=f"{file_name}/chunked_summary.txt")
print(final_summary)

# Create text file inside the folder
file1_path = os.path.join(folder_name, 'conclusion_summary.txt')

# You can write content to these files if needed
with open(file1_path, 'w') as file1:
  file1.write(final_summary)


# Now Step 5: Key Notes + Step 6: adding order and numbering
def process_text_keynotes(text):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role":
      "user",
      "content":
      """Generate key notes from the following text in the file. Make sure to accurately pull the meaning from the text and represent in points in order."""
      + f"{file_name}/conclusion_summary.txt" +
      f"{file_name}/chunked_summary.txt" +
      """Please output the keynotes in numbering""" +
      """Also make a heading of bare essentials at the end which shows the bare essentials from the text"""
    }])
  print("723 words analyzed.....")
  return completion.choices[0].message.content.strip()


def generate_keynotes(text):
  words = text.split()
  processed_text = ''
  for i in range(0, len(words), 723):
    chunk = ' '.join(words[i:i + 723])
    response = process_text_keynotes(chunk, )
    # time.sleep(18)
    processed_text += response.strip() + ' '
  return processed_text.strip()


keynotes = generate_keynotes(text=f"{file_name}/conclusion_summary.txt")
print(keynotes)

# Create text file inside the folder
file1_path = os.path.join(folder_name, 'keynotes.txt')

# You can write content to these files if needed
with open(file1_path, 'w') as file1:
  file1.write(keynotes)


# Step 8: Generate a blog post from the summary
def process_text_blogpost(text):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role":
      "user",
      "content":
      """Generate a blog post from the summary going through every aspect of topic in the summary and making headings"""
      + f"{file_name}/conclusion_summary.txt" + """Good luck!!"""
    }])
  print("723 words analyzed.....")
  return completion.choices[0].message.content.strip()


def generate_blogpost(text):
  words = text.split()
  processed_text = ''
  for i in range(0, len(words), 723):
    chunk = ' '.join(words[i:i + 723])
    response = process_text_blogpost(chunk, )
    # time.sleep(18)
    processed_text += response.strip() + ' '
  return processed_text.strip()


blogposts = generate_blogpost(text=f"{file_name}/conclusion_summary.txt")
print(blogposts)

# Create text file inside the folder
file1_path = os.path.join(folder_name, 'blogpost.txt')

# You can write content to these files if needed
with open(file1_path, 'w') as file1:
  file1.write(blogposts)


# Step 9: Generate midjourney prompts from the summary
def process_text_midjourney(text):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role":
      "user",
      "content":
      """Generate midjourney prompts that can be used to convert into images"""
      + """also make sure the prompts are according to the text""" +
      f"{file_name}/conclusion_summary.txt" +
"""Good luck!!"""
    }])
  print("723 words analyzed.....")
  return completion.choices[0].message.content.strip()


def generate_midjourney(text):
  words = text.split()
  processed_text = ''
  for i in range(0, len(words), 723):
    chunk = ' '.join(words[i:i + 723])
    response = process_text_midjourney(chunk, )
    # time.sleep(18)
    processed_text += response.strip() + ' '
  return processed_text.strip()


midjourney = generate_midjourney(text=f"{file_name}/conclusion_summary.txt")
print(midjourney)

# Create text file inside the folder
file1_path = os.path.join(folder_name, 'midjourneyprompts.txt')

# You can write content to these files if needed
with open(file1_path, 'w') as file1:
  file1.write(midjourney)

# All Steps completed and Program execution ends now.
