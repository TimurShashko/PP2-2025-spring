import csv
import psycopg2
from config import load_config

# ─────────────────────────────────────────────────────────────
def add_contact(full_name: str, phone: str) -> None:
    """Добавить одну запись, введённую с консоли."""
    sql = """
        INSERT INTO phonebook (full_name, phone)
        VALUES (%s, %s)
        ON CONFLICT (phone) DO NOTHING;
    """
    _execute(sql, (full_name, phone))
    print("Contact added (or skipped if phone existed).")


def add_from_csv(csv_path: str) -> None:
    """Загрузить контакты из CSV: имя,телефон в каждой строке."""
    with open(csv_path, newline="", encoding="utf‑8") as f:
        reader = csv.reader(f)
        for full_name, phone in reader:
            add_contact(full_name, phone)


def update_contact(old_phone: str, new_fullname: str | None = None,
                   new_phone: str | None = None) -> None:
    """Обновить имя или номер (или то и другое) по старому номеру."""
    sets, params = [], []
    if new_fullname:
        sets.append("full_name = %s")
        params.append(new_fullname)
    if new_phone:
        sets.append("phone = %s")
        params.append(new_phone)

    if not sets:
        print("Nothing to update."); return

    params.append(old_phone)
    sql = f"UPDATE phonebook SET {', '.join(sets)} WHERE phone = %s"
    _execute(sql, tuple(params))
    print("Contact updated (if phone existed).")


def find_contacts(mask: str = "") -> None:
    """Показать все записи, содержащие mask в имени или телефоне."""
    sql = """
        SELECT id, full_name, phone
        FROM phonebook
        WHERE full_name ILIKE %s OR phone ILIKE %s
        ORDER BY full_name;
    """
    rows = _fetchall(sql, (f"%{mask}%", f"%{mask}%"))
    print("─"*40)
    for r in rows:
        print(f"{r[0]:>3}  {r[1]:30}  {r[2]}")
    print("─"*40, f"{len(rows)} rows")


def delete_contact_choose(by_value: str) -> None:
    """
    Ищет записи по точному имени *или* телефону.
    Если найдено несколько, даёт выбрать конкретный id для удаления.
    """
    sql_select = """
        SELECT id, full_name, phone
        FROM phonebook
        WHERE full_name = %s OR phone = %s
        ORDER BY id;
    """
    rows = _fetchall(sql_select, (by_value, by_value))

    if not rows:
        print("Записи не найдены.")
        return

    # ─── Показываем список ───────────────────────────────
    print("\nНайдены записи:")
    for r in rows:
        print(f"[{r[0]}]  {r[1]:30}  {r[2]}")
    print("Выберите id для удаления "
          "(ENTER — отмена, 0 — удалить все найденные).")

    # ─── Считываем выбор пользователя ────────────────────
    choice = input("id → ").strip()
    if choice == "":
        print("Удаление отменено.")
        return

    # Хотим удалить все найденные
    if choice == "0":
        ids = tuple(r[0] for r in rows)           # (2, 5, 9)
        placeholders = ", ".join(["%s"] * len(ids))
        sql_delete = f"DELETE FROM phonebook WHERE id IN ({placeholders})"
        _execute(sql_delete, ids)
        print(f"Удалено: {len(ids)} запись(ей).")
        return

    # Удаляем одну выбранную запись
    try:
        choice_id = int(choice)
    except ValueError:
        print("Неверный ввод. Отмена.")
        return

    if choice_id not in [r[0] for r in rows]:
        print("Такого id нет в списке. Отмена.")
        return

    _execute("DELETE FROM phonebook WHERE id = %s", (choice_id,))
    print("Запись удалена.")


# ─────────── низкоуровневые вспомогательные ───────────
def _execute(sql: str, params: tuple | None = None) -> None:
    cfg = load_config()
    with psycopg2.connect(**cfg) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)


def _fetchall(sql: str, params: tuple | None = None):
    cfg = load_config()
    with psycopg2.connect(**cfg) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()

# ─────────── простейший CLI‑интерфейс ───────────
if __name__ == "__main__":
    while True:
        cmd = input(
            "\n(a)dd  (csv)import  (u)pdate  (f)ind  (d)elete  (q)uit : "
        ).strip().lower()

        if cmd in ("a", "add"):
            name = input("Full name : ")
            phone = input("Phone     : ")
            add_contact(name, phone)

        elif cmd == "csv":
            path = input("CSV path  : ")
            add_from_csv(path)

        elif cmd in ("u", "update"):
            old_phone = input("Existing phone to update : ")
            new_name  = input("New name   (blank ‑ keep) : ").strip() or None
            new_phone = input("New phone  (blank ‑ keep) : ").strip() or None
            update_contact(old_phone, new_name, new_phone)

        elif cmd in ("f", "find"):
            mask = input("Filter (substring) : ")
            find_contacts(mask)

        elif cmd in ("d", "delete"):
            val = input("Exact name OR phone to search : ")
            delete_contact_choose(val)

        elif cmd in ("q", "quit"):
            break
