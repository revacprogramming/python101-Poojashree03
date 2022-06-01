

def get_cs():
    """get string input"""


def cs_to_lot(cs):
    """convert connected string to list of strings"""


def lot_to_cs(lot):
    """convert list of strings to connected string"""


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
