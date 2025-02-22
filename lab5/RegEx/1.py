txt = """Hopefully your reading of the 3M case makes it clear why IT enterprise
architecture is critical for the globalising business. We are going to use
the article by Kettinger et al. (2010) to clarify types of enterprise IT
architecture and how they fit with the international business strategies we
discussed in Chapter 7.
We know from Chapter 7 that global competitiveness increasingly requires
optimisation of both business flexibility and business standardisation.
Bartlett and Ghoshal (1998) identify four alternative approaches to
operating globally. Bear in mind that their typology is slightly different
from the one we use in the rest of this chapter.
• The multinational Approach seeks to establish and maximise
business flexibility around the world, managing a portfolio of multiple
distinct business units (BUs).
• The international approach introduces business standardisation
for adapting and transferring parent company knowledge to foreign
markets while maintaining business flexibility, often in terms of
regional infrastructure support.
• The transnational approach further leverages regionalisation
of processes to create business standardisation in the core business
processes and establishes BUs as strategic partners that must exchange
knowledge and capabilities across the entire company.
• The global approach treats the world market as an integrated
whole, maximising business standardisation while maintaining needed
business flexibility for competing globally
COVID-19 and after: COVID-19 and the economic slowdown created a
people-based crisis, both at work and at home. Going forward, IHRM
had to recognise and adjust its policies to the volatile, uncertain,
complex, and ambiguous environments worldwide described in
Chapter 1 of this guide (see also Willcocks, 2021b, Chapter 1). 
abbb
lol_kek apple_banana odin_dva Tri_tree pol_Lava"""
import re

#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
print("#1")
print(re.findall(r"ab*", txt))

#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
print("#2")
print(re.findall(r"ab{2,3}", txt))

#3 Write a Python program to find sequences of lowercase letters joined with a underscore.
print("#3")
print(re.findall(r"\b[a-z]+_[a-z]+\b", txt))

#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
print("#4")
print(re.findall(r"[A-Z][a-z]+", txt))

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
print("#5")
print(re.findall(r"a.*b", txt))

#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.
print("#6")
textik = "Malenkoe predlozhenie, kotoroe bla bla bla"
print(re.sub(r"[ ,.]", ":", textik))

#7 Write a python program to convert snake case string to camel case string.
print("#7")
text = "odin_dva_tri_chetire_pyat"
print(re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text))

#8 Write a Python program to split a string at uppercase letters.
print("#8")
text2 = "CamelCaseStringExample"
print(re.sub(r"([A-Z])", r" \1", text2))

#9 Write a Python program to insert spaces between words starting with capital letters.
print("#9")
text3 = "CamelCaseStringExample"
x = re.sub(r"([a-z])([A-Z])", r"\1 \2", text3)
print(x)

#10 Write a Python program to convert a given camel case string to snake case.
print("#10")
text3 = "CamelCaseStringExample"
x = re.sub(r"([a-z])([A-Z])", r"\1_\2", text3)
x = x.lower()
print(x)