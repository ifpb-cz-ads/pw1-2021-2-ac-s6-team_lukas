import time 

tempo = 10 

while tempo: 
    minuto, segundo = divmod(tempo, 60) 
    print(tempo) 
    time.sleep(1) 
    tempo -= 1
    
print('Fogo!!') 
  

  
