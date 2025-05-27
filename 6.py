#User Management System
r = {
    "admin": ["cu", "du", "vu", "ar"],
    "editor": ["ec", "vu"],
    "viewer": ["vc"]
}

u = {"admin": {"p": "Admin123", "r": "admin"}}

def vp(p):
    return len(p) >= 8 and any(c.isupper() for c in p) and any(c.islower() for c in p) and any(c.isdigit() for c in p)

def cu():
    n = input("Username: ")
    if n in u: return print("❌ Exists.")
    pw = input("Password: ")
    if not vp(pw): return print("❌ Weak password.")
    rl = input("Role (admin/editor/viewer): ")
    if rl not in r: return print("❌ Invalid role.")
    u[n] = {"p": pw, "r": rl}
    print(f"✅ User '{n}' created.")

def du():
    n = input("Delete user: ")
    if n in u: del u[n]; print(f"✅ '{n}' deleted.")
    else: print("❌ Not found.")
1
def ar():
    n = input("User: ")
    if n not in u: return print("❌ Not found.")
    rl = input("New role: ")
    if rl not in r: return print("❌ Invalid role.")
    u[n]["r"] = rl
    print(f"✅ Role updated to '{rl}'.")

def vu():
    print("\n📋 Users:")
    for k, v in u.items():
        print(f"- {k}: {v['r']}")

def login():
    n = input("Username: ")
    pw = input("Password: ")
    if n not in u or u[n]["p"] != pw: return print("❌ Invalid login.")
    print(f"\n🔓 Welcome {n} ({u[n]['r']})")
    acts = r[u[n]["r"]]
    while True:
        print("\nActions:")
        for i, a in enumerate(acts, 1): print(f"{i}. {a}")
        print("0. Logout")
        ch = input("Choice: ")
        if ch == "0": break
        elif ch == "1" and "cu" in acts: cu()
        elif ch == "2" and "du" in acts: du()
        elif ch == "3" and "vu" in acts: vu()
        elif ch == "4" and "ar" in acts: ar()
        elif ch == "1" and "ec" in acts: print("📝 Edited.")
        elif ch == "1" and "vc" in acts: print("📄 Viewing...")
        else: print("❌ Not allowed.")

while True:
    print("\n=== Menu ===\n1. Login\n0. Exit")
    op = input("Option: ")
    if op == "1": login()
    elif op == "0": break
    else: print("❌ Invalid.")