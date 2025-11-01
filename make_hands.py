from collections import deque

def convert_rank_to_number(rank_str):
    """
    Converts a card rank string to its numerical value.
    """
    if rank_str.isdigit():
        return int(rank_str)
    rank_map = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    if rank_str in rank_map:
        return rank_map[rank_str]
    raise ValueError(f"Unsupported rank character: {rank_str}")

def organize_cards(cards_container, suit_ranking):
    """
    Organizes cards in the container by ascending rank, then by ascending suit rank.
    Handles both deques and lists.
    """
    def sorting_criterion(card_pair):
        rank_num, suit_num = card_pair
        return (rank_num, suit_ranking[suit_num])
    
    if isinstance(cards_container, deque):
        temp_list = sorted(cards_container, key=sorting_criterion)
        cards_container.clear()
        cards_container.extend(temp_list)
    else:
        cards_container.sort(key=sorting_criterion)

def run_game():
    """
    Main function to handle input, setup, and game simulation.
    """
    num_cards = int(input().strip())

    vaishnavi_cards = deque()
    suraj_cards = deque()

    for _ in range(num_cards):
        input_parts = input().strip().split()
        vaish_rank, vaish_suit_str, suraj_rank, suraj_suit_str = input_parts
        vaish_suit = int(vaish_suit_str)
        suraj_suit = int(suraj_suit_str)
        vaish_value = convert_rank_to_number(vaish_rank)
        suraj_value = convert_rank_to_number(suraj_rank)
        vaishnavi_cards.append((vaish_value, vaish_suit))
        suraj_cards.append((suraj_value, suraj_suit))

    priority_input = input().strip().split()
    suit_order = [int(val) for val in priority_input]
    suit_priority_map = {
        suit_order[0]: 3,
        suit_order[1]: 2,
        suit_order[2]: 1,
        suit_order[3]: 0
    }

    organize_cards(vaishnavi_cards, suit_priority_map)
    organize_cards(suraj_cards, suit_priority_map)

    central_pile = []
    active_turn = 1

    while True:
        if len(vaishnavi_cards) == 0 and len(suraj_cards) == 0:
            print("TIE")
            return

        if active_turn == 1:
            if len(vaishnavi_cards) == 0:
                print("LOSER")
                return
            current_hand = vaishnavi_cards
            victorious_hand = vaishnavi_cards
        else:
            if len(suraj_cards) == 0:
                print("WINNER")
                return
            current_hand = suraj_cards
            victorious_hand = suraj_cards

        played_card = current_hand.popleft()
        played_rank, played_suit = played_card

        if len(central_pile) == 0:
            central_pile.append(played_card)
            active_turn = 3 - active_turn
            continue

        pile_top_rank, pile_top_suit = central_pile[-1]
        can_win = (played_rank == pile_top_rank) and (suit_priority_map[played_suit] > suit_priority_map[pile_top_suit])

        if can_win:
            central_pile.append(played_card)
            organize_cards(central_pile, suit_priority_map)
            for card_in_pile in central_pile:
                victorious_hand.append(card_in_pile)
            central_pile.clear()
        else:
            central_pile.append(played_card)
            active_turn = 3 - active_turn

if __name__ == "__main__":
    run_game()