from src.prompt_template import restaurant_name_chain, menu_items_chain

def get_restaurant_name_chain():
    """Returns the chain for generating restaurant names."""
    return restaurant_name_chain

def get_menu_idea_chain():
    """Returns the chain for generating menu ideas."""
    return menu_items_chain