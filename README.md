🏢 **DFA-based Smart Building Access Control System**

📄 **Description**  
This project implements a **Deterministic Finite Automaton (DFA)** based **Access Control System** for a smart building. Each restricted zone is secured by a 🔒 **unique sequence of authentication methods**, ensuring step-by-step verification. The system validates user authentication and strictly enforces sequence rules, rejecting any incorrect, missing, or extra steps.  

Implemented in **Python**, this project includes:  
- 📌 **DFA design** for each building zone  
- 📌 **Transition tables** for all input symbols and states  
- 📌 **State diagrams** for visualization  
- 📌 **Test cases** covering normal, edge, and invalid inputs  

✨ **Features**  
- 🏷️ **Zone-specific access control:** Each zone has a predefined authentication sequence  
- ✅ **Strict sequence enforcement:** Access granted only when the exact sequence is followed  
- ⚠️ **Error handling:** Invalid symbols, wrong order, missing steps, and extra inputs are rejected  
- 🔧 **Dynamic scalability:** Add new zones or authentication methods without major redesign  
- 🖥️ **User-friendly interface:** Shows authentication symbols and available zones  

🔑 **Authentication Symbols**  
| Symbol | Authentication Method        |
|--------|-----------------------------|
| C      | Card Swipe                  |
| F      | Fingerprint                 |
| R      | Retina Scan                 |
| S      | Face Recognition            |
| V      | Voice Recognition           |
| P      | PIN Entry                   |
| B      | Biometric Combo             |
| A      | Admin Override              |

🏢 **Available Zones**  
- Lobby  
- Server Room  
- Laboratory  
- Executive Lounge  
- Research Wing  
- Conference Hall  
- Data Center  
- Admin Office  

🛠 **How to Run**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/YourUsername/DFA_SmartBuildingAccess.git
   ```
2. Navigate to the project folder:  
   ```bash
   cd DFA_SmartBuildingAccess
   ```
3. Run the Python program:  
   ```bash
   python access_control.py
   ```
4. Follow the on-screen prompts to select a zone and enter the authentication sequence  
5. Type `exit` to quit the program  

🖥 **Sample Usage**  

Correct Sequence Example:  
```
Enter Zone Name (or type 'exit' to quit): Lobby
Enter authentication sequence (symbols separated by space, e.g., C F R B): C F R B

✅ Access Granted ✅
```

Invalid Sequence Example:  
```
Enter Zone Name: Server Room
Enter authentication sequence: C F R B

❌ Access Denied ❌
```

📊 **DFA Design Overview**  
- **States (Q):** Represent progress of authentication  
- **Start State (q0):** No authentication done  
- **Intermediate States:** Each represents successful completion of a step  
- **Accept State:** Full sequence completed, access granted  
- **Reject State (qr):** Any invalid input, incorrect order, missing steps, or extra input  
- **Input Alphabet (Σ):** {C, F, R, S, V, P, B, A}  

🧪 **Testing**  
Tested with multiple real-world scenarios:  

| Test Case | Zone             | Input Sequence | Expected Output                    | Actual Output                  | Pass/Fail |
| --------- | ---------------- | -------------- | --------------------------------- | ------------------------------ | --------- |
| 1         | Lobby            | C F R B        | ✅ Access Granted                  | ✅ Access Granted              | Pass      |
| 2         | Server Room      | C F R B        | ❌ Access Denied (wrong final step)| ❌ Access Denied               | Pass      |
| 3         | Laboratory       | C F R          | ❌ Access Denied (partially complete)| ❌ Access Denied              | Pass      |
| 4         | Executive Lounge | C F R S P      | ❌ Access Denied (extra input)    | ❌ Access Denied               | Pass      |
| 5         | Research Wing    | C X B P        | ❌ Invalid Symbol → Access Denied | ❌ Invalid Symbol → Access Denied | Pass      |

🎯 **Conclusion**  
This **DFA-based smart building access control system** ensures **secure, deterministic, and scalable authentication** for multiple zones. Python implementation provides:  
- 🔄 **Dynamic sequence validation**  
- 📈 Clear **state transitions**  
- ⚡ **Robust error handling**  

It demonstrates a practical application of **formal automata theory** in modern security systems.
