import math

def calculate_chess_probabilities(wrating, brating, white_advantage=35, draw_width_factor=None):
    """
    Calculates the Win, Draw, and Loss probabilities for a chess game.
    
    Args:
        wrating (int): Elo rating of the player with White pieces.
        brating (int): Elo rating of the player with Black pieces.
        white_advantage (int): Bonus Elo added to White's rating (default 35).
        draw_width_factor (int): Manual override for draw width (w). 
                                 If None, it scales based on average rating.
                                 
    Returns:
        dict: Probabilities for {'win': P_w, 'draw': P_d, 'loss': P_l}
    """
    
    # 1. Adjust for White Advantage
    d = (wrating + white_advantage) - brating
    
    # 2. Determine Draw Width (w)
    # Scales linearly with skill: higher ratings = higher draw probability.
    if draw_width_factor is None:
        avg_rating = (wrating + brating) / 2
        draw_width_factor = max(50, 0.1 * avg_rating - 50)

    # 3. Calculate Win and Loss using the Logistic Draw Model
    # These formulas represent the probability of exceeding the draw margin.
    def win_prob(diff, w):
        return 1 / (1 + 10**((w - diff) / 400))
    
    def loss_prob(diff, w):
        return 1 / (1 + 10**((w + diff) / 400))

    p_win = win_prob(d, draw_width_factor)
    p_loss = loss_prob(d, draw_width_factor)
    
    # Draw probability is the remaining area of the probability distribution
    p_draw = max(0, 1.0 - p_win - p_loss)

    return {
        "win": round(p_win, 4),
        "draw": round(p_draw, 4),
        "loss": round(p_loss, 4)
    }

if __name__ == "__main__":
    # This section only runs if the script is executed directly.
    # It will not run if the function is imported elsewhere.
    
    def print_example(w, b, label):
        res = calculate_chess_probabilities(w, b)
        print(f"--- {label} ---")
        print(f"White ({w}) vs Black ({b})")
        print(f"Win:  {res['win']*100:>5.2f}%")
        print(f"Draw: {res['draw']*100:>5.2f}%")
        print(f"Loss: {res['loss']*100:>5.2f}%\n")

    print("Chess Outcome Probabilities (Using Variable Draw Width)\n")
    
    # Example 1: Beginners - Low draw rate
    print_example(1200, 1200, "Novice Level")

    # Example 2: Club Players - Moderate draw rate
    print_example(1800, 1800, "Club Level")

    # Example 3: Grandmasters - High draw rate
    print_example(2700, 2700, "Elite GM Level")
    
    # Example 4: Large Rating Gap
    print_example(2400, 2000, "Large Gap (IM vs Club)")
