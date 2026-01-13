from config import GOLD_PER_GLASS, WOOD_PER_GLASS, ORE_PER_GLASS


def calculate_resources(glasses: int) -> dict:
    """Calculate resources earned from drinking water."""
    return {
        "gold": glasses * GOLD_PER_GLASS,
        "wood": glasses * WOOD_PER_GLASS,
        "ore": glasses * ORE_PER_GLASS,
    }


def get_resources_display(gold: int, wood: int, ore: int) -> str:
    """Generate a display string for resources."""
    return f" {gold}   {wood}   {ore}"


def get_detailed_resources_display(gold: int, wood: int, ore: int) -> str:
    """Generate a detailed display string for resources."""
    return (
        f" Gold: {gold}\n"
        f" Wood: {wood}\n"
        f" Ore: {ore}"
    )
