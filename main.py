rules = [
    {"id": "R1", "if": ["Mesin Mati Total"], "then": "Cek Kelistrikan", "priority": 1},        
    {"id": "R2", "if": ["Mesin Berputar Lambat"], "then": "Aki Lemah", "priority": 2},        
    {"id": "R3", "if": ["Lampu Redup"], "then": "Aki Lemah", "priority": 2},                  
    {"id": "R4", "if": ["Aki Lemah", "Tidak Ada Karat pada Terminal"], "then": "Ganti Aki", "priority": 4}, 
    {"id": "R5", "if": ["Suara Klik saat Start"], "then": "Aki Lemah", "priority": 2},         
    {"id": "R6", "if": ["Mesin Mati Total", "Tidak Ada Suara"], "then": "Fungsi Kelistrikan Terputus", "priority": 4},
    {"id": "R7", "if": ["Aki Lemah"], "then": "Mesin Sulit Start", "priority": 1},               
    {"R8", "if": ["Cek Kelistrikan"], "then": "Isolasi Kelistrikan", "priority": 5},       
    ]

facts = {"Mesin Mati Total", "Suara Klik saat Start", "Tidak Ada Karat pada Terminal"}

