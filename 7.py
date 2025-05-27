# DAC - Discretionary Access Control
class DAC:
    acl = {
        "alice": {"file1.txt": "rw"},
        "bob": {"file1.txt": "r"},
        "charlie": {"file2.txt": "rw"}
    }

    def has_perm(self, u, f, op):
        return u in self.acl and f in self.acl[u] and op in self.acl[u][f]

    def access(self, u, f, op):
        if not self.has_perm(u, f, op):
            print("Access Denied")
            return
        try:
            if op == 'r':
                print(open(f).read())
            elif op == 'w':
                with open(f, 'a') as file:
                    file.write(f"\nUpdated by {u}")
                print("Write successful")
        except FileNotFoundError:
            print("File not found.")

dac = DAC()
u = input("User: ")
f = input("File: ")
op = input("Operation (r/w): ")
dac.access(u, f, op)

# MAC - Mandatory Access Control
class MAC:
    clearance = {"alice": 3, "bob": 2, "eve": 1}
    labels = {"top_secret.txt": 3, "confidential.txt": 2, "public.txt": 1}

    def access(self, u, f):
        c = self.clearance.get(u)
        l = self.labels.get(f)
        if c is None or l is None:
            print("Invalid user or file.")
        elif c >= l:
            try:
                print("Access granted:\n", open(f).read())
            except FileNotFoundError:
                print("File not found.")
        else:
            print("Access denied. Clearance too low.")

mac = MAC()
user = input("User: ")
file = input("File: ")
mac.access(user, file)