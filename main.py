def acces_netmiko():
    from netmiko import ConnectHandler
    device = {
        "device_type": "cisco_xr",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
    }
    with ConnectHandler(**device) as conn:
        print(conn.send_command("show clock"))
        interfaces = conn.send_command("show interfaces")
        with open("interfaces.txt", "w", encoding="utf-8") as f:
            f.write(interfaces)

def dire_bonjour():
    print("Bonjour, Git!")

print("Hello, Git!")
dire_bonjour()
def dire_salut():
    print("Salut, Git!")
dire_salut()