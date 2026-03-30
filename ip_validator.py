ipv4=input(" please enter IPv4 address")

parts=ipv4.split(" . ")

if len(parts)!=4:
    print(" invalid IPv4 address format")
else:
    valid=true