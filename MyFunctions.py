
def saveOutput(fun,y):
    save=input("do you wanna save output ?(yes/no):")
    if str(save).lower()=='yes':
        print('Done')
        with open("output.txt","w") as file:
            file.write("--CHERIBET CHERIF Chouaib--\n")
            file.write("----------------------------\n")
            file.write(f"{fun}\n")
            file.write(f"y'={y}\n\n\n")
    else:
        print("Goodbye ...")
        exit()
