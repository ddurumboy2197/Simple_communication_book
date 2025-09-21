import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("contacts.json")


def load_contacts() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_contacts(items: list[dict]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def add_contact(name: str, phone: str) -> None:
    items = load_contacts()
    items.append({"name": name, "phone": phone})
    save_contacts(items)


def list_contacts() -> None:
    items = load_contacts()
    if not items:
        print("Kontaktlar yo'q.")
        return
    for i, item in enumerate(items, 1):
        print(f"{i}. {item['name']} — {item['phone']}")


def find_contact(q: str) -> None:
    items = load_contacts()
    ql = q.lower()
    for item in items:
        if ql in item["name"].lower() or ql in item["phone"]:
            print(f"Topildi: {item['name']} — {item['phone']}")


def main() -> None:
    print("Kontaktlar: buyruqlar add, list, find <q>, exit")
    while True:
        cmd = input("> ").strip()
        if cmd in {"exit", "quit", "q"}:
            break
        if cmd == "list":
            list_contacts()
        elif cmd.startswith("add"):
            name = input("Ism: ")
            phone = input("Telefon: ")
            add_contact(name, phone)
        elif cmd.startswith("find"):
            q = ' '.join(cmd.split()[1:]) or input("Qidiruv: ")
            find_contact(q)
        else:
            print("Noma'lum buyruq")


if __name__ == "__main__":
    main()


