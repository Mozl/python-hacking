import hashlib
import argparse

parser = argparse.ArgumentParser(description="MD5 cracker")
parser.add_argument("-md5", dest="hash",help="md5 hash", required=True)
parser.add_argument("-w", dest="wordlist", help="wordlist", required=True)
parsed_args = parser.parse_args()

def main():
  hash_cracked = ""
  with open(parsed_args.wordlist) as file:
    for line in file:
      line = line.strip()
      if hashlib.md5(bytes(line,encoding="utf-8")).hexdigest() == parsed_args.hash:
        hash_cracked = line
        print("\nmd5-hash has been cracked. The password is: %s."%line)
  if hash_cracked == "":
    print("\nFailed to crack the hash, try using a bigger/different dictionary")

if __name__ == '__main__': # if file is run in the terminal
  main()
