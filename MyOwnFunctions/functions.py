def getInputBetween(startval: int, endval: int) -> int:
    while True:
        try:
            val = int(input("Mata in:"))
            if val >= startval and val <= endval:
                return val
            print(f"Ogiltigt val, mellan {startval} och {endval}, tack")
        except:
            print("Ange ett tal tack!")


def getBestPlayer() -> str:
    print("bla")


# Osynliga variabler i python: __name__ finns alltid men syns ej!
# Detta komma bara köras om vi kallar på denna som huvudfil, dvs F5:ar specifikt den här filen.
# Detta kan vara användbart vid testning!
if __name__ == "__main__":
    x = getInputBetween(100, 200)
    print(x)
