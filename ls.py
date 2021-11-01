import subprocess

# define the ls command
dir = subprocess.Popen(["ls", "-p", "."],
                      stdout=subprocess.PIPE,
                     )

# define the grep command
grep = subprocess.Popen(["grep", "-v", "/$"],
                        stdin=dir.stdout,
                        stdout=subprocess.PIPE,
                        )

# read from the end of the pipe (stdout)
endOfPipe = grep.stdout

# output the files line by line
def ls():
  for line in endOfPipe:
    print (line)
