import random
import time
import sys

# ===== ASSETS (ASCII ART) =====
def get_monster_art(m_type):
    arts = {
        "Slime": "\n      (o o)\n     (  -  )\n    (       )",
        "Zombie": "\n      [o_o]\n      /| |\\\n      / \\",
        "Shadow": "\n     .----.\n    /  O O \\\n    |  _   |\n     '----'",
        "Boss": "\n      <[💀]>\n     /|___|\\\n    /_|   |_\\"
    }
    return arts.get(m_type, "")

# ===== SYSTEM FUNCTIONS =====
def show_status(name, hp, max_hp, level, exp, inv):
    print(f"\n" + "="*30)
    print(f"👤 ชื่อ: {name} | ⚔️ LV: {level}")
    print(f"❤️ HP: {hp}/{max_hp} | ⭐ EXP: {exp}/10")
    print(f"🎒 กระเป๋า: {inv}")
    print("="*30)

def combat(p_hp, p_max_hp, m_name, m_hp, inv):
    print(get_monster_art(m_name))
    print(f"⚠️ {m_name} (HP: {m_hp}) ปรากฏตัว!")
    
    while m_hp > 0 and p_hp > 0:
        print(f"\n❤️ เลือดคุณ: {p_hp}/{p_max_hp} | 👾 เลือดศัตรู: {m_hp}")
        action = input("จะ [A]ttack หรือ [H]eal: ").lower().strip()
        
        if action == 'a' or action == 'attack':
            dmg = 5 if random.randint(1, 5) == 1 else 2
            if dmg == 5: print("💥 CRITICAL HIT!")
            m_hp -= dmg
            print(f"⚔️ คุณโจมตี! ดาเมจ: {dmg}")
        elif action == 'h' or action == 'heal':
            if "ยา" in inv:
                inv.remove("ยา")
                p_hp = min(p_hp + 5, p_max_hp)
                print(f"💊 ใช้ยา! HP กลายเป็น: {p_hp}")
            else:
                print("❌ ไม่มียา!")
        
        if m_hp > 0:
            enemy_dmg = 3 if m_name == "Boss" else 1
            print(f"💥 {m_name} โจมตีสวนกลับ! ดาเมจ: {enemy_dmg}")
            p_hp -= enemy_dmg
            
    return p_hp  # ส่งเลือดที่เหลือกลับไป

# ===== MAIN GAME LOOP =====
def start_game():
    # Player Initial Data
    name = input("นายชื่ออะไร: ")
    hp, max_hp = 10, 10
    level, exp = 1, 0
    inventory = []

    print("\n--- THE QUIET WORLD: DEFINITIVE EDITION ---")
    time.sleep(1)
    
    # --- ฉากเปิด ---
    choice = input("\n[1] ออกไปข้างนอก [2] นอนต่อ: ")
    if choice != "1":
        print("💤 นายหลับไปตลอดกาล... [BAD END]")
        return

    # --- สุ่มเหตุการณ์ ---
    event = random.randint(1, 3)
    
    if event == 1:
        m_type = random.choice(["Slime", "Zombie", "Shadow"])
        hp = combat(hp, max_hp, m_type, 8, inventory)
        
        if hp <= 0:
            print("💀 นายตายในการรบ... [GAME OVER]")
            return
        
        print(f"🏆 ชนะแล้ว!")
        exp += 10 # บังคับเลเวลอัพเพื่อไปสู้บอส
        if exp >= 10:
            level += 1
            max_hp += 5
            hp = max_hp
            print(f"🆙 LEVEL UP! เลือดเพิ่มเป็น {max_hp}")
            hp = combat(hp, max_hp, "Boss", 20, inventory)
            if hp > 0:
                print("🌟 นายกอบกู้โลกที่เงียบงันได้สำเร็จ! [TRUE END]")
                return
            else:
                print("💀 บอสแข็งแกร่งเกินไป... [BAD END]")
                return

    elif event == 2:
        print("\n💊 นายเจอยาฟื้นฟู!")
        inventory.append("ยา")
    
    # --- ฉากจบตรอกมืด ---
    show_status(name, hp, max_hp, level, exp, inventory)
    print("\n👂 มีเสียงเรียกจากตรอกมืด...")
    if input("จะเข้าไปดูไหม (y/n): ").lower() == 'y':
        print("🔪 เด็กผู้หญิงแทงนาย! แต่เธอร้องไห้และบอกว่า 'ขอบคุณที่มา'...")
        print("🎭 [MYSTERY END]")
    else:
        print("🏃 นายวิ่งหนีไปสุดชีวิต... [CHASE END]")

# รันเกม
if __name__ == "__main__":
    start_game()
