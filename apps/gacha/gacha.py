# gacha.py

import secrets
import hashlib
import json
import time
import platform
import os
from pathlib import Path


# ============================================================
# CONFIG
# ============================================================

HISTORY_FILE = Path("gacha_history.json")

RARITIES = {
    "COMMON": {
        "chance": 60.0,
        "rewards": [
            "100 Coins",
            "Potion",
            "Small XP Boost",
            "Basic Material"
        ]
    },

    "RARE": {
        "chance": 25.0,
        "rewards": [
            "500 Coins",
            "Rare Material",
            "Rare XP Boost",
            "Small Gem Pack"
        ]
    },

    "EPIC": {
        "chance": 10.0,
        "rewards": [
            "Epic Weapon",
            "Epic Armor",
            "Epic Character",
            "Large Gem Pack"
        ]
    },

    "LEGENDARY": {
        "chance": 4.0,
        "rewards": [
            "Legendary Weapon",
            "Legendary Character",
            "Legendary Armor"
        ]
    },

    "MYTHIC": {
        "chance": 1.0,
        "rewards": [
            "Mythic Character",
            "Mythic Weapon",
            "Mythic Artifact"
        ]
    }
}


# بعد از چند Pull بدون Epic یا بهتر
PITY_LIMIT = 50


# ============================================================
# SYSTEM INFORMATION
# ============================================================

def get_system_entropy():
    """
    اطلاعات مختلف سیستم را جمع می‌کند و
    از آنها برای ساخت entropy استفاده می‌کند.
    """

    data = [
        str(time.time_ns()),
        str(os.getpid()),
        platform.system(),
        platform.release(),
        platform.version(),
        platform.machine(),
        platform.processor(),
        str(os.cpu_count()),
        str(Path.cwd()),
    ]

    raw = "|".join(data)

    return raw


# ============================================================
# SEED GENERATOR
# ============================================================

def generate_seed():
    """
    ساخت یک seed بزرگ برای هر Pull.
    """

    system_data = get_system_entropy()

    # entropy واقعی سیستم
    random_bytes = secrets.token_bytes(32)

    raw = system_data.encode() + random_bytes

    seed_hash = hashlib.sha512(raw).hexdigest()

    return int(seed_hash, 16)


# ============================================================
# GACHA ID
# ============================================================

def generate_gacha_id():
    """
    تولید ID شش رقمی.
    """

    return secrets.randbelow(900000) + 100000


# ============================================================
# LOAD HISTORY
# ============================================================

def load_history():

    if not HISTORY_FILE.exists():
        return []

    try:

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


# ============================================================
# SAVE HISTORY
# ============================================================

def save_history(history):

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
# RARITY ROLL
# ============================================================

def roll_rarity():

    number = secrets.randbelow(10000) / 100

    current = 0

    for rarity, data in RARITIES.items():

        current += data["chance"]

        if number < current:
            return rarity

    return "COMMON"


# ============================================================
# REWARD
# ============================================================

def get_reward(rarity):

    rewards = RARITIES[rarity]["rewards"]

    index = secrets.randbelow(len(rewards))

    return rewards[index]


# ============================================================
# LUCK
# ============================================================

def generate_luck():

    return secrets.randbelow(1001)


# ============================================================
# PITY
# ============================================================

def apply_pity(rarity, pity_counter):

    """
    اگر بازیکن به PITY_LIMIT برسد،
    حداقل EPIC دریافت می‌کند.
    """

    if pity_counter >= PITY_LIMIT:

        high_tier = [
            "EPIC",
            "LEGENDARY",
            "MYTHIC"
        ]

        return high_tier[
            secrets.randbelow(len(high_tier))
        ]

    return rarity


# ============================================================
# GACHA ROLL
# ============================================================

def gacha_roll():

    history = load_history()

    pull_number = len(history) + 1

    seed = generate_seed()

    gacha_id = generate_gacha_id()

    luck = generate_luck()

    # محاسبه pity
    pity_counter = 0

    for result in reversed(history):

        if result["rarity"] in [
            "EPIC",
            "LEGENDARY",
            "MYTHIC"
        ]:
            break

        pity_counter += 1

    pity_counter += 1

    # Roll اصلی
    rarity = roll_rarity()

    # Pity
    rarity = apply_pity(
        rarity,
        pity_counter
    )

    # Reward
    reward = get_reward(rarity)

    # 0 / 1 roll
    binary_roll = secrets.randbelow(2)

    result = {

        "gacha_id": gacha_id,

        "pull": pull_number,

        "binary_roll": binary_roll,

        "seed": seed,

        "luck": luck,

        "pity": pity_counter,

        "rarity": rarity,

        "reward": reward,

        "timestamp": time.time(),

        "system": {
            "os": platform.system(),
            "release": platform.release(),
            "machine": platform.machine()
        }
    }

    history.append(result)

    save_history(history)

    return result


# ============================================================
# DISPLAY
# ============================================================

def display_result(result):

    print()
    print("=" * 45)
    print("             MAZDAK GACHA")
    print("=" * 45)

    print(f"Gacha ID   : {result['gacha_id']}")
    print(f"Pull       : #{result['pull']}")
    print(f"Binary     : {result['binary_roll']}")
    print(f"Luck       : {result['luck']}")
    print(f"Pity       : {result['pity']}/{PITY_LIMIT}")

    print("-" * 45)

    print(f"Rarity     : {result['rarity']}")
    print(f"Reward     : {result['reward']}")

    print("-" * 45)

    print(f"Seed       : {result['seed']}")

    print("=" * 45)
    print()


# ============================================================
# STATISTICS
# ============================================================

def show_statistics():

    history = load_history()

    if not history:

        print("\nNo pulls yet.\n")
        return

    counts = {}

    for result in history:

        rarity = result["rarity"]

        counts[rarity] = counts.get(
            rarity,
            0
        ) + 1

    print()
    print("=" * 45)
    print("             GACHA STATISTICS")
    print("=" * 45)

    print(f"Total Pulls : {len(history)}")

    print()

    for rarity in RARITIES:

        amount = counts.get(
            rarity,
            0
        )

        percentage = (
            amount / len(history)
        ) * 100

        print(
            f"{rarity:<12} "
            f"{amount:>5} "
            f"({percentage:6.2f}%)"
        )

    print("=" * 45)
    print()


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print()
        print("╔══════════════════════════════╗")
        print("║        MAZDAK GACHA          ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Single Pull               ║")
        print("║ 2. 10 Pulls                  ║")
        print("║ 3. Statistics                ║")
        print("║ 4. Exit                      ║")
        print("╚══════════════════════════════╝")

        choice = input("\nSelect: ").strip()

        if choice == "1":

            result = gacha_roll()

            display_result(result)

        elif choice == "2":

            print("\n===== 10 PULL =====")

            for _ in range(10):

                result = gacha_roll()

                display_result(result)

        elif choice == "3":

            show_statistics()

        elif choice == "4":

            print("\nGoodbye 👋")
            break

        else:

            print("\nInvalid option.")


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()