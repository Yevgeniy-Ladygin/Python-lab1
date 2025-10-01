import random

MAIN_INGREDIENTS: list[str] = [
    "курица",
    "говядина",
    "рыба",
    "свинина",
    "тофу",
]

SIDES: list[str] = [
    "рис",
    "картофель",
    "гречка",
    "макароны",
    "овощи на гриле",
]

SAUCES: list[str] = [
    "томатный",
    "сырный",
    "грибной",
    "соевый",
    "белый винный",
]

SPICES: list[str] = [
    "соль",
    "перец",
    "паприка",
    "куркума",
    "орегано",
]

ADJECTIVES: list[str] = [
    "аппетитное",
    "нежное",
    "пикантное",
    "ароматное",
    "сочное",
]

NOUNS: list[str] = [
    "наслаждение",
    "удовольствие",
    "искушение",
    "мечта",
    "восторг",
]

def generate_name() -> str:
    """Генерирует случайное название блюда."""
    adjective = random.choice(ADJECTIVES).capitalize()
    noun = random.choice(NOUNS).capitalize()
    return f"{adjective} {noun}"

def generate_recipe() -> str:
    """Создает случайный рецепт с одним ингредиентом из каждой категории."""
    
    main = random.choice(MAIN_INGREDIENTS)
    side = random.choice(SIDES)
    sauce = random.choice(SAUCES)
    spice = random.choice(SPICES)
    
    steps = [
        f"1. Подготовьте {main}.",
        f"2. Приготовьте {side}.",
        f"3. Обжарьте {main} с {spice}.",
        f"4. Приготовьте {sauce} соус.",
        "5. Подавайте блюдо с соусом и украсьте зеленью!"
    ]
    
    recipe_name = generate_name()
    
    recipe = (
        f"=== {recipe_name} ===\n\n"
        f"Ингредиенты:\n"
        f"- Основной продукт: {main}\n"
        f"- Гарнир: {side}\n"
        f"- Соус: {sauce}\n"
        f"- Специя: {spice}\n\n"
        f"Способ приготовления:\n"
        + "\n".join(steps)
    )
    
    return recipe

if __name__ == "__main__":
    print(generate_recipe())