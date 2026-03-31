ipv4=input(" please enter IPv4 address:")

parts=ipv4.split(".")

if len(parts)!=4:
   print(" invalid IPv4 address format")
else:
    valid=True
    for part in parts:
        if not part.isdigit():
          valid=False
        num=int(part)
        if num< 0 or num >255:
          valid=False
    if valid:
        print("correct IPv4 format")
    else:
        print("invalid IPv4 address format")        



