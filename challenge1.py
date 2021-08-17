print("Hello, Would you like to continue?")
print("Click 1 for yes or 2 for no")
resposta = int(input())
if resposta ==  1 or resposta =="yes":
    print("Continuing...")
elif resposta == 2 or resposta == "no":
    print("Exiting")
else:
    print("Please try again and respond with yes or no.")

