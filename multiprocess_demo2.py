# python 3 
# ref 
# https://medium.com/@leportella/how-to-run-parallel-processes-8939dafae81e


import os                                                                       
from multiprocessing import Pool                                                
                                                                                                                                                      

def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
 

# ---------------------- V1  ----------------------
# Running 3 processes in parallel
print ('---------------------- V1  ----------------------')                                                                             

processes = ('process1.py', 'process2.py', 'process3.py')                                    
  

pool = Pool(processes=3)                                                        
pool.map(run_process, processes)    


# ---------------------- V2  ----------------------
# Running multiple processes in parallel and in sequence
print ('---------------------- V2  ----------------------')                                                                             
# the first two processes running in parallel until both are finished and only then process3 is executed.
                                                                                                                                        
processes2 = ('process1.py', 'process2.py')                                    
other = ('process3.py',)
                                                  
                                                                                                                                                                                                                                      
pool = Pool(processes=3)                                                        
pool.map(run_process, processes2) 
pool.map(run_process, other) 

