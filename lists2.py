url = "http://www.google.com"
domain = url[11:-4]
print (domain)

name = input("Enter your Name ")
name_length = len(name)
screen_width = 80
box_length = name_length * 2
left_margin = (screen_width - box_length)//2
name_start = (box_length//4)
name_end = (box_length//4)

print
print (" " *left_margin + "+" + "-" * box_length + "+")
print (" " *left_margin + "|" + " " * (box_length) + "|")
print (" " *left_margin + "|" + " " * (box_length) + "|")
print (" " *left_margin + "|" + " " * name_start + name + " " * name_end + "|")
print (" " *left_margin + "|" + " " * (box_length) + "|")
print (" " *left_margin + "|" + " " * (box_length) + "|")
print (" " *left_margin + "+" + "-" * box_length + "+")
print
