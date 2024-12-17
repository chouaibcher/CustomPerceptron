
def saveOutput(fun,y):
    save=input("do you wanna save output ?(yes/no):")
    if str(save).lower()=='yes':
        print('Done')
        with open("output.txt","w") as file:
            file.write("--CHERIBET CHERIF Chouaib--\n")
            file.write("----------------------------\n")
            file.write(f"{fun}\n")
            file.write(f"y'={y}\n\n\n")
            file.write("Neural networks are not just for solving complex problems;\n they are also tools for gaining a deeper understanding of patterns and relationships within data.\n - Sebastian Thrun\n")
    else:
        print("Goodbye ...")
        exit()