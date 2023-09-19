import pprint

from domain import ORDERS_TO_MATCH, TARGET_MATCHES, TRADES_TO_MATCH, match_orders_trades


def main():
    matches = match_orders_trades(ORDERS_TO_MATCH, TRADES_TO_MATCH)
    try:
        assert sorted(matches) == sorted(TARGET_MATCHES), "Not a match!"
    except AssertionError as e:
        print(e)
        pp = pprint.PrettyPrinter(width=120, indent=2)
        pp.pprint("Missing solution matches:")
        for m in (match for match in matches if match not in TARGET_MATCHES):
            print(m)

        pp.pprint("Missing target matches:")
        for m in (match for match in TARGET_MATCHES if match not in matches):
            print(m)


if __name__ == "__main__":
    # Run the main function
    main()
