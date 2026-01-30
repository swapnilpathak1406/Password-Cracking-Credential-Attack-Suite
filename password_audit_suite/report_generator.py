def generate_report(results):
    print("\nPASSWORD SECURITY AUDIT REPORT\n")
    for user, data in results.items():
        print(f"User: {user}")
        print(f"Cracked Password: {data['password']}")
        print(f"Strength: {data['strength']}")
        print("-" * 40)
