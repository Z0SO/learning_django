

# best fist

best_partition= 300 # tomo 300 porque quiero evaluar la mejor particion, y necesito tener almacenado por momentos la particion mas grande

memory = {
    'part1': {
        'part_id': 1,
        'tam': 110,
        'frag_int': 0,
        'busy': False,
        'busy_for':None
    },

    'part2': {
        'part_id': 2,
        'tam': 160,
        'frag_int': 0,
        'busy': False,
        'busy_for':None
    },

    'part3': {
        'part_id': 3,
        'tam': 300,
        'frag_int': 0,
        'busy': False,
        'busy_for':None
    },
}


process = {
    'p1': {
        'pid': 1,
        'inic': 0,
        'tam': 100,
    },
    'p2': {
        'pid': 2,
        'inic': 0,
        'tam': 150,
    },

    'p3': {
        'pid': 3,
        'inic': 0,
        'tam': 250,
    }
}

for proc, proc_map in process.items():
    print('--'*32)
    print(f'Ingresa Proceso {proc_map["pid"]}')

    for mem, mem_map in memory.items():
        print(f'El proceso {proc_map["pid"]} se encuentra recorriendo la particion {mem}')

        # preguntar si la particion esta ocupada, si esta en falso esta libre...
        if mem_map["busy"] == False:
            
            # pregunta por si el proceso entra en memoria
            if (mem_map["tam"] - proc_map["tam"]) >= 0:     # puede entrar
                
                # es la best?
                if mem_map["tam"] < best_partition:  
                    best_partition = mem_map["tam"]



    # una vez obtenido el mejor tamaño, se le asignara a la particion de memoria correspondiente
    
    print(f'Estado actual de memoria: ')
    print('#######'*16)

    for mem, mem_map in memory.items():
        if best_partition == mem_map["tam"]:

            mem_map["frag_int"]= (mem_map["tam"]) - (proc_map["tam"])
            mem_map["busy"]= True
            mem_map["busy_for"]= proc
            
        print(f'Particion: {mem}')
        print(f'Tamaño: {mem_map["tam"]}')
        print(f'Fragmentacion interna: {mem_map["frag_int"]}')
        print(f'Ocupado: {mem_map["busy"]}')
        print(f'Ocupado por: {mem_map["busy_for"]}')
        
        print('#######'*16)

 
    best_partition=300

    print('--'*32)
    input()