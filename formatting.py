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

# Below is exercise of using JOIN method
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)


Output-only Terminal
Output:
Black reapers with the sound of steel on stones

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']



love_maybe_lines_stripped = []
for word in love_maybe_lines:
 love_maybe_lines_stripped.append(word.strip())
print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)


['Always', 'in the middle of our bloodiest battles', 'you lay down your arms', 'like flowering mines', '', 'to conquer me home.']
Always
in the middle of our bloodiest battles
you lay down your arms
like flowering mines

to conquer me home.
