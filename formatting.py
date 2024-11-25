poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print (poem_title_fixed)

print(poem_title)
print(poem_author)

poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

print(poem_author)
print(poem_author_fixed)

Spring Storm
spring storm
William Carlos Williams
WILLIAM CARLOS WILLIAMS
William Carlos Williams
WILLIAM CARLOS WILLIAMS

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"


author_names = authors.split(',')
print(author_names)

#This part was to split last name and to save it in new list
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
print(author_last_names)
