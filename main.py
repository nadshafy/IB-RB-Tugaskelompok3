rules = [
    {"id": "R1", "if": ["Mesin Mati Total"], "then": "Cek Kelistrikan", "priority": 1},        
    {"id": "R2", "if": ["Mesin Berputar Lambat"], "then": "Aki Lemah", "priority": 2},        
    {"id": "R3", "if": ["Lampu Redup"], "then": "Aki Lemah", "priority": 2},                  
    {"id": "R4", "if": ["Aki Lemah", "Tidak Ada Karat pada Terminal"], "then": "Ganti Aki", "priority": 4}, 
    {"id": "R5", "if": ["Suara Klik saat Start"], "then": "Aki Lemah", "priority": 2},         
    {"id": "R6", "if": ["Mesin Mati Total", "Tidak Ada Suara"], "then": "Fungsi Kelistrikan Terputus", "priority": 4},
    {"id": "R7", "if": ["Aki Lemah"], "then": "Mesin Sulit Start", "priority": 1},               
    {"id": "R8", "if": ["Cek Kelistrikan"], "then": "Isolasi Kelistrikan", "priority": 5},  
    ]

facts = {"Mesin Mati Total", "Suara Klik saat Start", "Tidak Ada Karat pada Terminal"}

def forward_chaining(facts, rules):
    new_facts = set(facts)
    applied_rules = []
    changed = True
    
    while changed:
        changed = False
        # Urutkan berdasarkan prioritas (tinggi ke rendah)
        sorted_rules = sorted(rules, key=lambda r: r["priority"], reverse=True)

        for rule in sorted_rules:
            # Cek apakah semua kondisi dalam "if" ada di fakta
            if all(cond in new_facts for cond in rule["if"]) and rule["then"] not in new_facts:
                new_facts.add(rule["then"])
                applied_rules.append(rule["id"])
                print(f"Aktivasi {rule['id']}: {rule['if']} → {rule['then']}")
                changed = True

    print("\n=== HASIL FORWARD CHAINING ===")
    print("Aturan yang diaktifkan:", applied_rules)
    print("Fakta akhir:", new_facts)
    print("==============================\n")
    return new_facts

def backward_chaining(goal, facts, rules, depth=0):
    indent = "  " * depth

    if goal in facts:
        print(f"{indent}- {goal} ditemukan di fakta.")
        return True

    # Cari aturan yang menghasilkan goal
    applicable_rules = [r for r in rules if r["then"] == goal]

    for rule in applicable_rules:
        print(f"{indent}Menguji {rule['id']}: Jika {rule['if']} maka {rule['then']}")
        all_true = True
        for condition in rule["if"]:
            if not backward_chaining(condition, facts, rules, depth + 1):
                all_true = False
                break
        if all_true:
            print(f"{indent} Aturan {rule['id']} terpenuhi, menambah '{goal}' ke fakta.")
            facts.add(goal)
            return True

    print(f"{indent} {goal} tidak dapat dibuktikan dengan aturan yang ada.")
    return False

print("=== SISTEM PAKAR: DIAGNOSA KERUSAKAN MOBIL ===")
print("Fakta awal:", facts)
print("\n--- Proses Forward Chaining ---")
final_facts = forward_chaining(facts, rules)

print("\n--- Proses Backward Chaining ---")
goal = "Ganti Aki"
print(f"Membuktikan tujuan: {goal}")
result = backward_chaining(goal, set(facts), rules)

if result:
    print(f"\nKesimpulan: '{goal}' TERBUKTI berdasarkan fakta dan aturan yang ada.")
else:
    print(f"\nKesimpulan: '{goal}' TIDAK TERBUKTI dari fakta yang ada.")
