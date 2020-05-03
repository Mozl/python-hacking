import requests
import sys
import multiprocessing
from joblib import Parallel, delayed
from tqdm import tqdm

sub_list = open('subdomains-1000.txt').read()
subs = sub_list.splitlines()

num_cores = multiprocessing.cpu_count()
inputs = tqdm(subs)

def findSubs(subdomain):
  url_to_check = f"https://{subdomain}.{sys.argv[1]}"

  try:
    requests.get(url_to_check)
  
  except requests.ConnectionError:
    print("Nothing found")

  else:
    print("Valid domain: " + url_to_check)
    with open('subDomains.txt', 'a') as f:
      print('Valid domain: ', url_to_check, file=f)

if __name__ == "__main__":
    processed_list = Parallel(n_jobs=num_cores)(delayed(findSubs)(i) for i in inputs)





