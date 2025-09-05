events = {
    'C': 'Card Swipe',
    'F': 'Fingerprint',
    'R': 'Retina Scan',
    'S': 'Face Recognition',
    'V': 'Voice Recognition',
    'P': 'PIN Entry',
    'B': 'Biometric Combo',
    'A': 'Admin Override'
}

dfa_zones = {
    'Lobby': ['C', 'F', 'R', 'B'],
    'ServerRoom': ['C', 'F', 'R', 'P'],
    'Laboratory': ['C', 'F', 'R', 'V'],
    'ExecutiveLounge': ['C', 'F', 'R', 'S'],
    'ResearchWing': ['C', 'F', 'B', 'P'],
    'ConferenceHall': ['C', 'F', 'B', 'V'],
    'DataCenter': ['C', 'F', 'B', 'S'],
    'AdminOffice': ['C', 'F', 'B', 'A']
}

def create_transitions(sequence):
    transitions = {}
    n = len(sequence)
    for i in range(n+1):
        state = f'q{i}'
        transitions[state] = {}
        for e in events:
            transitions[state][e] = f'q{i+1}' if i < n and e == sequence[i] else 'qrej'
    transitions['qrej'] = {e: 'qrej' for e in events}
    return transitions

dfa_tables = {zone: create_transitions(seq) for zone, seq in dfa_zones.items()}
accept_states = {zone: f'q{len(seq)}' for zone, seq in dfa_zones.items()}

def check_access(zone, input_sequence):
    zone = zone.strip()
    if zone not in dfa_zones:
        return "❌ Zone not found. Please select a valid zone."
    
    current_state = 'q0'
    transitions = dfa_tables[zone]
    accept_state = accept_states[zone]
    
    print("\n🔹 Authentication Steps:")
    for event in input_sequence:
        event = event.upper()
        if event not in events:
            return f"❌ Invalid event symbol: {event}"
        print(f"   → {event} : {events[event]}")
        current_state = transitions[current_state][event]
    
    return "\n✅ Access Granted ✅" if current_state == accept_state else "\n❌ Access Denied ❌"

def show_symbol_legend():
    print("🔑 Authentication Symbols:")
    for k, v in events.items():
        print(f"   {k} : {v}")
    print()

if __name__ == "__main__":
    print("══════════════════════════════════════════════")
    print("      🏢 Smart Building Access Control 🏢      ")
    print("══════════════════════════════════════════════\n")
    
    show_symbol_legend()
    print("🏷️ Available Zones:")
    for zone in dfa_zones:
        print(f"   • {zone}")
    print("\n══════════════════════════════════════════════\n")
    
    while True:
        zone_name = input("Enter Zone Name (or type 'exit' to quit): ").strip()
        if zone_name.lower() == 'exit':
            print("\n👋 Exiting program. Goodbye!")
            break
        
        seq_input = input("Enter authentication sequence (symbols separated by space, e.g., B R F C): ")
        seq_list = seq_input.strip().upper().split()
        
        result = check_access(zone_name, seq_list)
        print(result)
        print("\n──────────────────────────────────────────────")
