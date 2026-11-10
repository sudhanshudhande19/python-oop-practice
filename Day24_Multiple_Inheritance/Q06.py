# Create a Teacher class and a Researcher class. Inherit both into a Professor class.

# Concept: Combining Two Independent Roles.

# Requirements:

    # Teacher stores subject and experience.
    # Researcher stores research topic and publication count.
    # Professor stores professor name.
    # Professor should access all parent attributes.
    # Display complete professor information.

#------------------------------------------------------------------------------------------------------------

class Teacher:

    def __init__(self,subject,experience):
        self.subject = subject
        self.experience = experience

class Researcher:
    def __init__(self,topic,pub_count):
        self.topic = topic 
        self.pub_count = pub_count 

class Perofessor(Teacher,Researcher):
    def __init__(self, subject, experience,name):
        super().__init__(subject, experience)
        self.name = name 


s= Perofessor('Python',5,'sudhanshu')
d = Researcher('Funcation',2)

print(f'Subject           = {s.subject}')
print(f'Experience        = {s.experience} year')
print(f'Topic             = {d.topic}')
print(f'publication count = {d.pub_count}')
print(f'Name              = {s.name}')