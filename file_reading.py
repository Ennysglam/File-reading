def read_file (filename):
 open_file = open("./reading_text_files/story.txt", "r") 
 read_file = open_file.read()
 print(read_file)
 text = read_file.split()
 count = dict()
 for i in text:
      if i in count:
        count [i] += 1
      else:
        count[i] = 1
 return count
print (read_file("./reading_text_files/story.txt"))
