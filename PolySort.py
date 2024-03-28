print("""                                                           
                                                           
                                                          
@@@@@@@   @@@ @@@   @@@@@@    @@@@@@   @@@@@@@   @@@@@@@  
@@@@@@@@  @@@ @@@  @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@  
@@!  @@@  @@! !@@  !@@       @@!  @@@  @@!  @@@    @@!    
!@!  @!@  !@! @!!  !@!       !@!  @!@  !@!  @!@    !@!    
@!@@!@!    !@!@!   !!@@!!    @!@  !@!  @!@!!@!     @!!    
!!@!!!      @!!!    !!@!!!   !@!  !!!  !!@!@!      !!!    
!!:         !!:         !:!  !!:  !!!  !!: :!!     !!:    
:!:         :!:        !:!   :!:  !:!  :!:  !:!    :!:    
 ::          ::    :::: ::   ::::: ::  ::   :::     ::    
 :           :     :: : :     : :  :    :   : :     :     
""")

# By: Nandan R
# Date: 28/03/2024
# Version: 1.0

def sort_dict_by_value(x):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}

No_of_Wordlists: int = int(input("Enter the number of wordlists: "))
Wordlists = []
print("Wordlists must be saved in the WordLists folder.")
for i in range(No_of_Wordlists):
    Wordlist = input("Enter the name of wordlist: ")
    if Wordlist[-4:] != ".txt":
        Wordlist += ".txt"
    Wordlist = "WordLists/" + Wordlist
    Wordlists.append(Wordlist)
def sort_dict_by_value(x):
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
output = input("Enter the name of output file: ")
output = "Output/" + output

temptxt = "TempFiles/temp0.txt"

with open(Wordlists[0],"r",encoding="iso-8859-1") as r:
    lines = r.readlines()
with open(temptxt,"w",encoding="iso-8859-1") as w:
    w.writelines(lines)

for i in range(No_of_Wordlists - 1):
    with open(Wordlists[i+1],"r",encoding="iso-8859-1") as r:
        lines = r.readlines()
    with open(temptxt,"r",encoding="iso-8859-1") as r2:
        lines2 = r2.readlines()
    temptxt = "TempFiles/"+"temp"+str(i+1)+".txt"
    with open(temptxt,"w",encoding="iso-8859-1") as w:
        freq = {}
        for line in lines:
            if line in freq:
                freq[line] += 1
            else:
                freq[line] = 1
        for line in lines2:
            if line in freq:
                freq[line] += 1
            else:
                freq[line] = 1
        freq = sort_dict_by_value(freq)
        for key in freq:
            w.write(key)

with open(temptxt,"r",encoding="iso-8859-1") as r:
    lines = r.readlines()
with open(output,"w",encoding="iso-8859-1") as w:
    w.writelines(lines)
