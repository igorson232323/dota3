import time


inventory = []


levels = ("Ерли гейм", "Мид гейм", "Лейт гейм")


items = {
    "Ерли гейм": ["12 танго", "клоретка", "манго"],
    "Мид гейм": ["манта", "этериал", "скади"],
    "Лейт гейм": ["рапира", "даедалус", "сильвер"]
}


puzzles = {
    "Ерли гейм": {"вопрос": "Кто выходит с мида со счетом 0/12?", "ответ": "максим каротаж"},
    "Мид гейм": {"вопрос": "Кто делает рампагу за инвокера?", "ответ": "игорь мусихин"},
    "Лейт гейм": {"вопрос": "Какой счет у Игоря когда враги ломают трон", "ответ": "0/15/2"}
}


loosed_lines = set()


enemies = {
    "Ерли гейм": {"name": "Мидовая бруда", "hp": 50, "damage": 10},
    "Мид гейм": {"name": "Энигма с блинком", "hp": 70, "damage": 20},
    "Лейт гейм": {"name": "Антимаг с брейсерами", "hp": 130, "damage": 30}
}


player_hp = 200


def start_game():
    print("Добро пожаловать в игру 'Dota 2'!")
    print("Ваша цель - затащить катку")
    time.sleep(1.5)
    for level in levels:
        play_level(level)
    print("Поздравляем! Вы затащили катку!")


def play_level(level):
    global player_hp
    enemy = enemies[level]
    print(f"\n=== {level.upper()} ===")
    print(f"Сейчас минута: {level}")
    print(f"На линии вы встречаете врага: {enemy['name']} (HP: {enemy['hp']}, Урон: {enemy['damage']})")
    
    while True:
        if player_hp <= 0:
            print("Вы проиграли! Ваш герой умер.")
            return
        
        # Если враг мертв, игрок может продолжать другие действия
        if enemy['hp'] <= 0:
            print(f"Враг {enemy['name']} побежден, но вы можете продолжать играть на уровне.")
        
        action = input("Что вы хотите сделать? (зайти в магаз/купить/использовать/гангать линии/атаковать врага): ").lower()
        
        if action == "зайти в магаз":
            look_around(level)
        elif action == "купить":
            take_item(level)
        elif action == "использовать":
            use_item(level)
        elif action == "гангать линии":
            if solve_puzzle(level):
                break
            else:
                print("Вы добили недостаточно крипов, пофармите еще")
        elif action == "атаковать врага":
            # Если враг мертв, атака невозможна
            if enemy['hp'] <= 0:
                print(f"Враг {enemy['name']} уже побежден. Вы не можете его атаковать.")
            else:
                attack_enemy(level)
        else:
            print("Научись играть узник рекрутов")
        
        # Проверяем, жив ли враг, перед атакой
        if enemy['hp'] > 0:
            enemy_attack(enemy)



def look_around(level):
    print(f"Вы зашли в лавку, на нафармленные копейки можно купить только фигню..")
    for item in items[level]:
        print(f"- {item}")


def take_item(level):
    item = input("Какой предмет вы хотите купить? ").lower()
    if item in items[level]:
        inventory.append(item)
        items[level].remove(item)
        print(f"Вы купили {item}. Ваш инвентарь: {inventory}")
    else:
        print("Научись играть пж")


def use_item(level):
    item = input("Какой предмет вы хотите использовать? ").lower()
    if item in inventory:
        print(f"Вы использовали {item}.")
        if item == "12 танго" and level == "Ерли гейм":
            loosed_lines.add("тиммейты недовольны")
            print("Максим разозлился и начинает орать зачем ты купил 12 танго")
        elif item == "манта" and level == "Мид гейм":
            print("Ты прожал в тайминг манту и увернулся от ульты снайпера, научи играть гений доты")
        elif item == "рапира" and level == "Лейт гейм":
            print("Ты купил рапиру но сразу умер и потерял ее. Все тиммейты кинули тебе репорты :(")
        else:
            print("Зачем против такого пика этот предмет?")
    else:
        print("У вас нет такого предмета в инвентаре.")


def solve_puzzle(level):
    print("Чтобы пройти дальше, вы должны апнуть титана и знать все тонкости игры:")
    print(puzzles[level]["вопрос"])
    answer = input("Ваш ответ: ").lower()
    if answer == puzzles[level]["ответ"]:
        print("Правильно! Линии пушатся, крипы фармятся.")
        return True
    else:
        print("Неправильно. Отдыхай.")
        return False


def attack_enemy(level):
    global player_hp
    enemy = enemies[level]
    print(f"Вы атакуете {enemy['name']}!")

    # Уменьшаем HP врага
    enemy['hp'] -= 30
    if enemy['hp'] <= 0:
        print(f"Вы победили врага {enemy['name']}!")
        enemy['hp'] = 0  # Устанавливаем HP врага на 0, чтобы не было отрицательных значений
        return True  # Возвращаем True, чтобы отметить победу
    else:
        print(f"HP {enemy['name']}: {enemy['hp']}")
        return False  # Враг еще жив


def enemy_attack(enemy):
    global player_hp
    print(f"{enemy['name']} атакует вас! Вы получаете {enemy['damage']} урона.")
    player_hp -= enemy['damage']
    print(f"Ваше HP: {player_hp}")


if __name__ == "__main__":
    start_game()
