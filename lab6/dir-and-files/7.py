
def copy_file(src, dst):
    with open(src, "rb") as fsrc:
        content = fsrc.read()
    with open(dst, "wb") as fdst:
        fdst.write(content)

if __name__ == "__main__":
    src = input("Источник (source): ")
    dst = input("Назначение (destination): ")
    try:
        copy_file(src, dst)
        print(f"Файл {src} скопирован в {dst}.")
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except Exception as e:
        print("Ошибка копирования:", e)

r""" Источник C:\Users\User\OneDrive\Рабочий стол\promo_codes.txt
Назначение C:\Users\User\OneDrive\Рабочий стол\promo_copy.txt
C:\Users\User\OneDrive\Рабочий стол\pp22025\lab6\for-dir-7py\promo_copy.txt """
