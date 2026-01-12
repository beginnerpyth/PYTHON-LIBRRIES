guess_name="jaja"
guess=" "
guess_count=0
guess_limit=3
out_of_guesses=False
while guess_name!=guess and not(out_of_guesses):
    if guess_count<guess_limit:
        print("you have chances")
        guess=input("enter a name")
        guess_count+=1
    else:
        out_of_guesses=True#paila while loop ani if loop sidhera while loop ani else loop ani balla sab sidhera tala ko loop janxa
if out_of_guesses:#yo chai kasto ho vanda out of guesses true jaba hunxa run out of chances ani jaba mlauxa under 3 chances then while ko loop break hunxa ra tala ko loop janxa
    print("you have no more guesses")
else:
    print("you won")
