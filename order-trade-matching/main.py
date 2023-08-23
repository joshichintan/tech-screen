import pprint

from domain import (
    TARGET_MATCHES,
    ORDERS_TO_MATCH,
    TRADES_TO_MATCH,
    match_orders_trades,
)


def main():
    matches = match_orders_trades(ORDERS_TO_MATCH, TRADES_TO_MATCH)
    try:
        assert matches == TARGET_MATCHES, "Orders and trades did not match"
    except AssertionError as e:
        print(e)
        # pp = pprint.PrettyPrinter(width=120, indent=2)
        # pp.pprint("TARGET MATCHES:")
        # pp.pprint(TARGET_MATCHES)
        # pp.pprint("matches:")
        # pp.pprint(matches)


if __name__ == "__main__":
    # Run the main function
    main()
