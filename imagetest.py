from subprocess import call, Popen, PIPE
cmd = False
while cmd==False:
    cmd = Popen(["bash", "image.sh"], stdout=PIPE)