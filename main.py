from pypresence import Presence

def main():
    print("Hello from nscpot-discord-rich-presence!")
    RPC = Presence("1345518060727177347")
    RPC.connect()

if __name__ == "__main__":
    main()
