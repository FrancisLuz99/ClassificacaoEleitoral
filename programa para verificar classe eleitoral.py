idade =int( input("informar idade"))

if idade<16:
        print("Não Eleitor")
        
if idade >=18 and idade <=65:
        print("Eleitor obrigatório")
        
if  idade >=16 and idade <18 or idade >65:
        print(" Facultativo")
    
