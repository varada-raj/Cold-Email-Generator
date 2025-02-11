# Cold-Email-Generator

Cold Email Generator: 
https://colab.research.google.com/drive/1hq1XoYaUP1W10CTJOWIhzd39NcQJs2cB#scrollTo=U_2XpLkhFuRo


B to B , companies hire people from other companies for a projects
Ex: Kittu , where he got placed in delloite, but works in uber. So here uber addresses uber that they will provide people to uber for work, so for that delloite sends a COLD EMAIL for uber to address the requirement , where delloite searches for in their official website.


- [ ] So here we are going to uses llm to generate cold mail.

Project flow (we are using NIKE)
- [ ] Extract text from the career , web based loader using langchain
- [ ] We pass it to llm to generate a json of job role, job skills etc
- [ ] Store it in Chromadb 
- [ ] So now we are going to use llm for generating cold email, where we will pass information from db , for a particular job role or description.


Code Build:
- [ ] Build a langchain llm call for chatGroq
- [ ] Extract text from Nike website using Webbed loader provided by langchain
- [ ] Prompt Template the extracted data, pass it to llm to extract job roles and form it as a JSON formate for further use.
- [ ] So here for prompt templating and passing it to llm we use a technique “CHAINING” :


Chaining :
chain_extract = prompt_template | llm
res = chain_extract.invoke({"page_data": content})


- [ ] Now create a vector db ie - chromadb
- [ ] Now in the chromdb we add our skills with their respective portfolios.
- [ ] Now we use this chroma db for vector search for the particular skills in the web extracted data skills.

links = collection.query(query_texts=job["skills"], n_results=2).get('metadatas', [])
links


- [ ] Now using PromptTemplate.from_template
- [ ] We formate a template with a prompt , links, job description


chain_email = prompt_email | llm
res = chain_email.invoke({"job_description": str(job), "link_list": links})
print(res.content)

Now we have Cold Email

——————————————————————————————————————————————————————————————————————————————
